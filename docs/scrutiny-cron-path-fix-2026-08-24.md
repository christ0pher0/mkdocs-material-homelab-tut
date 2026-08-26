# Scrutiny Collector Cron PATH Fix — 2026-08-24

## Root cause

Cron's default PATH does not include `/usr/sbin`, where `smartctl` lives.
Every cron-triggered run of the Scrutiny collector was dying at the
dependency check (`DependencyMissingError: "smartctl binary is missing"`)
before it ever collected or published data. This was invisible in
`journalctl -u cron` because that only logs that cron *invoked* the
command, not the program's own stdout/stderr.

Affected: maturin, aslan, babar, blaine (all raw-crontab PVE hosts).
Not affected: freenas-bsd (uses TrueNAS's managed Task Scheduler, which
sets a correct PATH).

## Fix (applied identically on all four hosts)

On each host:

```bash
sudo which smartctl
```

Confirm the path (was `/usr/sbin/smartctl` on all four).

```bash
sudo crontab -e
```

Add this as the first line, above the existing job:

```
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
```

Resulting crontab on each host:

```
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
0,30 * * * * /opt/scrutiny/bin/scrutiny-collector-metrics run --config /opt/scrutiny/config/collector.yaml --api-endpoint http://192.168.1.34:8082
```

## Verification (run before trusting the fix to cron itself)

Simulate cron's minimal environment directly:

```bash
sudo env -i PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin /bin/sh -c '/opt/scrutiny/bin/scrutiny-collector-metrics run --config /opt/scrutiny/config/collector.yaml --api-endpoint http://192.168.1.34:8082'
```

A clean run ends with `INFO[000x] Main: Completed`. Confirmed clean on
maturin, aslan, babar, and blaine.

Confirm the crontab actually saved:

```bash
sudo crontab -l
```

## Diagnostic commands used to isolate the issue (for reference / next time)

```bash
sudo crontab -l
```

```bash
ls -la /opt/scrutiny/bin/
```

```bash
sudo systemctl status cron
```

```bash
sudo journalctl -u cron --since "7 days ago" | tail -50
```

```bash
curl -v http://192.168.1.34:8082
```

## Follow-up: bake into build notes

Add a note to the host build/setup docs: any future host using raw
crontab (instead of a managed scheduler like TrueNAS's Task Scheduler)
for a job that shells out to system binaries in `/usr/sbin` or `/sbin`
needs an explicit `PATH=` line in that crontab. Same applies to any
other cron job relying on tools outside `/usr/bin:/bin`.

---

# Drive health findings surfaced during this fix

## aslan /dev/sdb — WDC WD120EMAZ-11BLFA0, 12TB, serial `5PGEVJSC`

Real, ongoing concern — not a reporting artifact. Hub's "Failed" status
is legitimate.

- Reallocated_Sector_Ct: 12 (every other drive checked today: 0)
- Reallocated_Event_Count: 12
- Offline_Uncorrectable: 22
- Current_Pending_Sector: 0
- Lifetime ATA error count: 141
- Temperature: 55°C now, recorded max 56°C
- Most recent 5 logged errors (#137–141) all hit the same LBA
  (`0x003a5970`), all in one session ~6,061 power-on-hours ago (~8
  months back from 38,707 total power-on hours). Nothing newer logged
  since.

Command used:

```bash
sudo smartctl -a /dev/sdb
```

**Action:** plan a replacement; not acutely failing, but genuine
accumulated wear. Open question — what pool/array does this drive sit
in on aslan, and is there redundancy underneath it?

## blaine /dev/sdc — SK hynix SC210 mSATA 256GB

Burst of ATA read/write errors, all clustered within about one hour,
~13 days prior to check (power-on lifetime 741–742h vs. 1054h total).
Nothing recurring since. All actual wear-life metrics clean (0 retired
blocks, 0% lifetime used, 812GB total writes on a 256GB drive).

Command used:

```bash
sudo smartctl -a /dev/sdc
```

**Action:** low urgency. Reseat the mSATA connection/cable next time
the case is open. Watch for recurrence now that reporting is fixed.

## blaine /dev/sdd and /dev/sde — Seagate Constellation ES.3 / ES.2

Both threw smartctl exit code 32 ("attributes crossed threshold in the
past") — driven entirely by attribute 190 (Airflow_Temperature_Cel)
WORST value, not by sector/error attributes. All real failure
predictors (Reallocated_Sector_Ct, Current_Pending_Sector,
Offline_Uncorrectable, Reported_Uncorrect, error log) are clean/zero on
both.

- sdd: recorded max temp 50°C historically, currently 45°C
- sde: recorded max temp 51°C historically, currently 47°C

Commands used:

```bash
sudo smartctl -a /dev/sdd
sudo smartctl -a /dev/sde
```

**Action:** low urgency for the drives themselves. Worth checking
blaine's case airflow/cooling, since two drives in the same chassis
both show a past heat excursion.

## blaine /dev/sda and /dev/sdb — expected stale, not a fault

These are rotating restic backup target drives on blaine; they are
only connected intermittently, so Scrutiny entries for them going
stale/missing is expected behavior, not a monitoring gap.

## Open thread

Cross-referencing drive chart serials `ZL2CVBME` and `ZL2CYHB1` —
context not yet established; unresolved as of end of session.
