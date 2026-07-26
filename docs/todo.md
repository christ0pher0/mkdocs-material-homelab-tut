# Homelab Todo & Roadmap
_Last updated: 2026-07-26 live session with Chris. Scrutiny host-id labeling added across all 5 spoke collectors (maturin/aslan/blaine/babar/freenas-bsd) — dashboard now groups drives by hostname instead of bare device paths, closing out the 2026-07-24 Scrutiny build. Docker & LXC recommendation lists (10 each, not currently running) curated and logged — see new section below. Snipe-IT correctly identified as already deployed, swapped for Stirling-PDF in the LXC list. Starter-batch pick for next deploys: **NetBox and Immich** (Scrutiny already done). **Scrutiny extended to a 6th spoke: amontillado** (native Windows collector, smartmontools via winget, `commands.metrics_smartctl_bin` override needed since the installer doesn't add smartctl to PATH, Task Scheduler every 30 min via `Register-ScheduledTask` — note `[TimeSpan]::MaxValue` breaks the task XML schema, use a long finite duration like 3650 days instead). One SMART flag investigated on amontillado's /dev/sdb (Seagate 3TB, 35,508 power-on hours) — overall health PASSED, all real failure indicators (reallocated sectors, pending sectors, UDMA CRC errors) at 0; the bit-5 trigger was a one-time historical temperature-attribute dip, not a current issue. False alarm, same pattern as the fleet build's earlier flags._

_Prior update — 2026-07-24 Friday one-on-one (scheduled, autonomous run — Chris not present live). Hour 1 Claude School: "scheduled tasks vs. asking Claude directly" taught, using this session itself as the live example. Follow-up on 2026-07-17's assignment (demand a proof-command before marking a specialist's "done" as [x]): partially applied — today's earlier live session corroborated Movies/TV backups against real backup_drives.md data, but STL closure was taken on Chris's word alone, no command cited. New assignment: pick one recurring manual check and classify it (scheduled task vs. Sam automation vs. keep live) — due next Friday. Hour 2: Sunday prep brief generated — see session output, top items are Rack Build Phase 1, Sam's 4 stalled proposals, and the Prometheus retention decision. No infra changes made, no completions confirmed by Chris (not present)._

_Prior update — 2026-07-24 live session with Chris. **Shardik explicitly deprioritized by Chris** — "not an issue till I say it is," babar is the better node and covers the primary use case; stop surfacing shardik as a top item. **Backup rotation confirmed done**: Chris confirmed movies, TV, and both outstanding STL rsyncs (STL_ACCESSORIES_TERRAIN, STL_SOURCE_MATERIAL) are complete — backup_drives.md corroborates Movies/TV with real populated stats and clean SMART; STL closure taken on Chris's word. Chris flagged renewed interest in physically setting up the rack + switch (Rack Build Phase 1) as the next priority. Two new curated lists added this session: Top 10 Big Projects and Top 10 Quick Wins (under 30 min each) — see new sections below._

_Prior update — 2026-07-21 live session with Chris. Major finding: shardik's CPU is confirmed dead — this closes out the weeks-long MCE investigation thread (bank 0 2026-07-06, bank 5 2026-07-08/09, stress-ng soak test that was never pulled) with a real answer. No spare AM4 CPU in reserve; sourcing decision (buy vs. cannibalize urnst-deb or temerant-win, both Ryzen 5 1600X) still pending Chris. Large network/DNS/IP hygiene pass also done this session — see Resolved below. monitor-deb hit 100% disk full mid-session (real, not cosmetic — caused an ansible task to fail with "No space left on device"); freed ~6G (docker image prune + apt clean), now at 88%/3.6G free, but this is not a permanent fix — Prometheus (9G, 30d retention) will keep growing back toward the ceiling, retention/disk-size decision still open._

_Prior update — 2026-07-19 Sunday weekly team meeting (scheduled, autonomous run — Chris not present live. Full 10-person status round held, two-hour format. Top blocker restated and escalated: the shardik LXC 150 stress-ng soak test result (7-hr run finished 2026-07-08/09) still hasn't been pulled — now 10+ days stale with no tmux capture logged, top item blocking further MCE diagnosis. Sam proposed two new projects this session (hw_inv.md auto-diff-audit, shardik MCE watcher) — pending Chris approval alongside the two proposals still open from 2026-07-12. No completions marked [x] on Chris's behalf since he wasn't present to confirm; new action items below need his review/prioritization at the next live session.)_

_Prior update — 2026-07-17 Friday one-on-one (scheduled, autonomous run — Chris not present live. Hour 1 Claude School: "reading Claude's output critically" lesson delivered, tied to the 2026-07-16 babar Ansible-onboarding correction and the aslan/maturin stale-RAM-doc pattern. Assignment: next time a specialist reports a task "done," ask for the one command that proves it before marking [x]. Note: no submission logged for the 2026-07-10 "loaded prompt" assignment — carrying forward, not chasing. Hour 2: Sunday meeting prep brief generated — see session output. No infra changes made this session, no new completions confirmed by Chris.)_

_Prior update — 2026-07-12 Sunday weekly team meeting (scheduled, autonomous run — Chris not present live. Full 10-person status round held. No completions marked [x] on Chris's behalf since he wasn't present to confirm; new action items below need his review/prioritization at the next live session. See action items under each specialist's section and the new items logged this pass.)_

_Prior update — 2026-07-10 Friday one-on-one (Hour 1 Claude School: better-prompts lesson delivered, assignment given — write a "loaded" prompt for the storage.cfg node-scoping risk, due next Friday. Hour 2: Sunday meeting prep brief generated from current backlog — see weekly_meeting notes / session output. No infra changes made this session, no new completions confirmed by Chris.)_

_Prior update — 2026-07-09 end of session (Babar joined the Proxmox cluster as 5th node (192.168.1.12, Dell Pro Tower Plus, Core Ultra 7 265, 128GB DDR5, RTX 5060) — full onboarding to Ansible/Zabbix/node_exporter/Uptime Kuma complete. Qdevice permanently removed — 5 physical nodes is odd-count and self-resolving, Proxmox itself refuses a qdevice now. kasm-2404-deb (VM 111) live-migrated off shardik to babar (hw_inv.md had its location wrong — was on shardik, not aslan as documented). NVIDIA driver installed on babar (610.43.03, open-kernel-module, DKMS, Secure Boot MOK-signed) after a near-miss where the generic Debian nvidia-driver package nearly removed proxmox-ve entirely (blocked by Proxmox's own pve-apt-hook safety mechanism). Ollama deployed in a privileged LXC (102) on babar with full RTX 5060 GPU passthrough, confirmed working with live model inference. Shardik's CPU MCE fault further decoded (bank 5/execution unit, uncorrected/context-corrupting) — RAM ruled out via successful aslan/maturin DIMM audits (both corrected to 64GB in hw_inv.md, were stale at 32GB); a 7-hour isolated stress-ng soak test was kicked off in a fresh LXC on shardik to try to reproduce the fault, result not yet checked. New known gaps: hw_inv.md still needs babar's final NVMe storage config and a correction to aslan's stale storage description; cluster storage.cfg has several dir-storage entries (SDA_store/hdd12tb/hdd3tb/nvme_store) that are unscoped to specific nodes and confirmed live-misbehaving on babar (aliasing local root disk instead of erroring) — needs a "nodes" restriction added before anyone trusts those names fleet-wide.)_

---

## Decisions Made This Session (2026-07-24)

- **Shardik deprioritized.** Chris's ruling: "not an issue till I say it is, I don't miss it really, babar is a better replacement." Not a standing blocker anymore — don't keep surfacing the AM4 CPU sourcing decision as a top item.
- **Movies and TV backup rotation confirmed done.** Verified against backup_drives.md — all active drives show Jun 2026 backup dates, real populated Used/Free stats, clean SMART.
- **STL_ACCESSORIES_TERRAIN and STL_SOURCE_MATERIAL rsyncs confirmed done**, per Chris.
- **Rack + switch physical setup flagged as next priority** — Chris wants to move on Rack Build Phase 1 (place rack, install SG200-50/PDU). See Network / VLAN / Rack Build backlog.

## Resolved This Session (2026-07-24, continued)

- ⚠️ **ConvertX deployed on docker-deb (port 3005) — ran into a real Vaultwarden/Caddy outage while setting it up, now fixed.** Chris couldn't log into the fresh ConvertX account and Bitwarden was throwing "Error saving" on new items. Root cause found via live troubleshooting: Caddy's TLS listener on docker-deb (shared across all 3 site blocks on port 8443/443 internal) was poisoned by an expired unmanaged cert for `docker-deb.taild502ad.ts.net` (a Tailscale-issued cert, referenced by explicit file path in the Caddyfile) — this broke the TLS handshake for every site sharing that listener, including vaultwarden.lan, not just the expired one. Vaultwarden's mount, config, and the container itself were all healthy the whole time; this was purely a shared-listener TLS cert issue. **Fix:** `sudo tailscale cert --cert-file /var/lib/tailscale/certs/docker-deb.taild502ad.ts.net.crt --key-file ... docker-deb.taild502ad.ts.net` to regenerate (Tailscale's background renewal had actually already refreshed the file on disk — Caddy just hadn't reloaded it since), then `docker restart caddy`. Confirmed fixed via `curl --resolve vaultwarden.lan:8443:127.0.0.1 https://vaultwarden.lan:8443` returning real Vaultwarden HTML. **Gotcha for next time:** testing a multi-site Caddy config with curl requires `--resolve` to force the correct SNI — setting only `-H "Host: ..."` doesn't affect the TLS handshake and will misleadingly fail on every site, cert-healthy or not.
- **Correction to Taylor's "Vaultwarden autofill port-matching bug" backlog line (Security & Monitoring section below):** today's Bitwarden "won't save logins" symptom was NOT that bug — it was this Caddy cert issue causing outright write failures, not an autofill-detection quirk. The original port-matching autofill bug is unconfirmed/still separate, not touched today.
- ✅ **ConvertX now fully working over HTTPS at https://convertx.lan:8443.** ConvertX itself couldn't log in over plain HTTP (session cookie has the Secure flag; ConvertX's own docs flag this exact symptom — fixed short-term with `HTTP_ALLOWED=true`, then done properly): added a `convertx.lan` site block to the same Caddyfile (`tls internal`, `reverse_proxy 192.168.1.34:3005` — host-mapped port, not the container name, since ConvertX is a separate compose stack not on Caddy's Docker network), added `192.168.1.34 convertx.lan` to the **router's own `/etc/hosts`** (192.168.1.1, GL-MT6000) — this is a separate DNS source from git-ansible's hosts file and is what actually resolves friendly `.lan` names for Chris's own workstation/phone, since Ansible's hosts-push only reaches the managed Linux fleet. **Confirmed real, pre-existing issue while debugging this:** hitting `convertx.lan` or `vaultwarden.lan` on the *default* ports (80/443, no port specified) returns a generic 404 from something that is NOT our Caddy container — Caddy only publishes 8443/8088 on this host. This lines up exactly with the standing "Dual reverse proxy — Caddy + Traefik both on docker-deb" backlog item (Casey/Riley, Media section below) — Traefik is almost certainly the thing answering on the default ports. Not resolved today; both services must be accessed with an explicit `:8443` for now.
- ✅ **Both vaultwarden.lan:8443 and convertx.lan:8443 confirmed fully secure end-to-end 2026-07-24.** Caddy's local CA root cert exported from docker-deb and trusted on amontillado — imported into Windows' LocalMachine\Root store (PowerShell `Import-Certificate`, needed an elevated/admin window — first attempt failed with Access Denied from a non-admin shell) and separately into Firefox's own cert store (Firefox doesn't read the Windows store by default — imported directly via Settings → Privacy & Security → Certificates → View Certificates → Authorities → Import, checked "Trust this CA to identify websites"). No more browser warnings, no cleartext traffic on either site.
- ⚠️ **Router's own `/etc/hosts` (192.168.1.1) confirmed stale — separate finding, not yet actioned.** No entries at all for shardik/maturin/aslan/blaine/babar; still lists swarm01/02/03 (long deleted) and old pi1-deb/pi2-deb/octopi-deb naming. This is the DNS source of truth for any client that isn't part of the managed Ansible fleet (Chris's own workstation/phone) — worth a cleanup pass, and worth remembering that git-ansible's hosts fixes earlier this cycle (truenas-bsd, rocky-rpm, etc.) do **not** reach this file and so won't resolve from Chris's own devices unless mirrored here too.

## Scrutiny Fleet-Wide SMART Monitoring — ✅ DONE 2026-07-24

- **Full build completed same-day as spec'd.** Hub (Scrutiny + InfluxDB) on docker-deb at http://192.168.1.34:8082. Spoke collectors deployed and confirmed publishing on maturin, aslan, blaine, babar (Docker wasn't installed on any PVE host — used native Go binary + cron instead, not the Docker collector originally planned), and freenas-bsd (native FreeBSD binary on the TRYAGAIN pool — not `/opt`, since TrueNAS CORE boot environments can wipe root-filesystem changes on update; cron job added via GUI Tasks → Cron Jobs, not raw crontab, since CORE's config is middleware-managed and won't persist a manually-edited crontab). All collectors run every 30 min (`0,30 * * * *`).
- **First-pass results, all clean after investigation** — several flagged errors on first collector run turned out to be false alarms or already-known conditions, not new problems:
  - Blaine sdc "INQUIRY failed" — confirmed online and actively serving CRU data (READING/TROVE WEBSITE/RPG_ARCHIVE via restic-deb); CRU hot-swap backplane likely doesn't pass SMART commands through even though normal I/O works fine.
  - Blaine sda/sdd flagged "error log" (exit 64) on the collector's first pass — direct `smartctl -a` showed sda completely clean; sdd (blaine's own OS boot SSD) has only old errors from initial burn-in (7 hrs power-on time), SSD_Life_Left 253/253, not current.
  - Aslan sdb "error log" flag — matches the already-documented condition (12TB HDD, 22 uncorrectable errors, deliberately relegated to non-critical/bulk use only in hw_inv.md). Known, not new.
  - Aslan sdc "checksum error" flag — direct check showed completely clean (Orico SATA SSD, aslan's actual OS drive per the hw_inv.md correction). One-off blip on first collector pass.
  - **Net result: no actual drive health problems found anywhere in the fleet.** Good outcome for a first-ever fleet-wide SMART sweep.
- ⚠️ **Real gap found along the way, unrelated to Scrutiny itself:** TrueNAS's `/etc/resolv.conf` had no working DNS path at first (`fetch` couldn't resolve github.com) — traced to the Global Configuration nameserver; confirmed working once verified against `192.168.1.1`. Worth remembering if any future external-fetch task on TrueNAS mysteriously fails.
- Deployment method note for future fleet-wide reuse: Ansible ad-hoc (`ansible <hosts> -i ~/ansible_dev/inventory_auto -m shell -a "<command>" --become --ask-vault-pass` from git-ansible) is far faster than hopping SSH sessions host-by-host for read-only fleet checks — used successfully to pull `smartctl --scan` from maturin/aslan/blaine in one shot.

## Top 10 Big Projects (curated 2026-07-24)

1. ~~Finish backup rotation~~ — ✅ done, see Decisions above.
2. Move the half rack into place — Rack Build Phase 1 (Riley).
3. Physically set up the SG200-50 switch — Rack Build Phase 1 (Riley).
4. VLAN/pfSense buildout — SG-1100 offline config, segment the 4 approved VLANs. Natural next phase once the switch is in.
5. STL/media collection frontend — Manyfold, or a custom page like vinyl_collection.html if Manyfold doesn't fit.
6. DC salvage — finish surveying and decommissioning the remaining DCs (DC1 done, more to go).
7. Drive database + hardware inventory web frontend — replaces manual doc-editing workflow.
8. Dual reverse proxy cleanup — Caddy and Traefik both running on docker-deb; pick one, retire the other.
9. Comics stack — Komga/Mylar, libraries not yet populated.
10. Monitoring stack overhaul — Prometheus retention decision plus the still-undocumented Proxmox cluster diagram/monitoring architecture.

## Quick Wins — Under 30 Minutes Each (curated 2026-07-24)

1. ~~Add babar to the Ansible inventory~~ — ✅ done 2026-07-26.
2. ~~Confirm Open WebUI loads clean at 192.168.1.34:3000~~ — ✅ confirmed 2026-07-26, loads clean, llama3.2:3b ready, no errors.
3. ~~Set git identity on restic-deb~~ — ✅ confirmed already set 2026-07-26 (coshaughnessy@gmail.com / cos), no action needed.
4. ~~Check the 1 HIGH Zabbix alert sitting on the dashboard~~ — ✅ checked 2026-07-26: pihole-pi1-deb mmcblk0 disk latency spike, no mmc errors in dmesg, host idle at check time. Transient blip on an old 3.79GB SD card, not a failing-card signal. No action needed.
5. ~~Add babar to the hosts.md hostname table~~ — ✅ done automatically 2026-07-26 as a side effect of the onboard2.yml run (row exists, MAC/OS/status fields placeholder "—" for now).
6. ~~Confirm batocera-deb and pi3-deb are actually in `[linux_skip]`, not `[linux]`~~ — **premise was wrong 2026-07-26: no `[linux_skip]` group exists in inventory_auto** (actual groups: linux, windows, bsd, network, android, media, mac, debian, redhat, pi, proxmox, control). Mid-fix mistake: assumed the group name instead of checking, briefly deleted both hosts from the file entirely (sed insert silently no-opped against a nonexistent group), caught immediately and restored to `[linux]` exactly as before — confirmed via `grep -n -A 5 '\[linux\]'`. **Open decision for Chris/Jordan, not resolved tonight:** should batocera-deb/pi3-deb move to `[pi]` instead of `[linux]`, given they're both Pi hardware and may not be good candidates for standard Debian package/patch playbooks? Left in `[linux]` (original state) pending that call.
7. ~~Drop the stale "Kuma ping-only" line in Taylor's backlog~~ — ✅ done 2026-07-26.
8. ~~Remove the stale "cru_stats.sh path fix" line under Sam's list~~ — ✅ already struck as done in Sam's section, confirmed 2026-07-26.
9. ~~Confirm whether the Zabbix web frontend is actually deployed/reachable~~ — ✅ confirmed 2026-07-26, live dashboard screenshot from Chris (192.168.1.29:8080, 38 hosts, real data).
10. **Wire SMART alerts into smartd.conf — scope corrected 2026-07-26, no longer a quick win.** Fleet search (`ansible linux -m shell -a "test -f /opt/scripts/smartd_telegram_alert.sh"`) confirmed the script only exists on git-ansible (a VM, no real physical disk to monitor) — every host with actual drives (babar, docker-deb, restic-deb, monitor-deb, etc.) is missing it. Real scope: confirm smartd runs as a daemon on physical-drive hosts, push the script out, wire each smartd.conf individually. **Chris confirmed 2026-07-26: still wants this — Telegram is active/push, Scrutiny's dashboard is passive/pull, not redundant.** Promoted to a real backlog item, not started tonight (time + scope). Needs proper specing next session: which hosts (likely same set as Scrutiny spokes: maturin/aslan/blaine/babar — freenas-bsd has its own native alerting, probably out of scope here), smartd daemon-mode confirmation first.

## Scrutiny → Telegram Alerting (found 2026-07-26, not yet built)

- **Scrutiny's Hub has native Telegram notification support** (via Shoutrrr, same library pattern as Discord/Slack/ntfy/etc.) — no separate script or Zabbix wiring needed. Config: `telegram://<bot-token>@telegram?chats=@channel-or-chat-id`, placed in `scrutiny.yaml` at `/opt/scrutiny/config/` on docker-deb (already mounted by the Hub container). Confirmed via `example.scrutiny.yaml` from the official repo.
- **Chris confirmed he wants this** — reuse OerthBot's existing token + OerthChannel rather than a second bot, same pattern as Kuma's Telegram wiring.
- **Not started 2026-07-26 — real scope, not a quick win:** needs OerthBot's token pulled from `/etc/oerthbot/config.json` on git-ansible and written into docker-deb's `scrutiny.yaml` without the secret getting echoed into any terminal/chat history along the way, then a Scrutiny container restart and a live notification test (`curl -X POST http://localhost:8082/api/health/notify`).
- This also separately confirms: Zabbix's *default* Linux template only covers disk I/O performance/latency, not SMART attribute data — Zabbix does have an official "Smartctl by Zabbix agent 2" template that could pull real SMART data (zabbix-agent2 is already fleet-wide), but it hasn't been imported/linked. Not needed now that Scrutiny→Telegram covers this more directly.

## Docker & LXC — Not Currently Running (curated 2026-07-25)

Docker candidates:

1. Immich — photo/video library with mobile auto-backup and AI search.
2. Nextcloud — personal cloud storage, file sync, office suite.
3. n8n — workflow automation; could glue Telegram bot, Kuma, and Zabbix alerts into one pipeline.
4. Watchtower — auto-updates container images on a schedule.
5. Dockge or Komodo — visual compose-stack manager.
6. ~~Scrutiny~~ — ✅ done, see Scrutiny section above (built 2026-07-24).
7. Speedtest Tracker — scheduled speed tests with history graphs.
8. Changedetection.io — monitors web pages for changes (restocks, price drops, etc.).
9. Firefly III — personal finance/budget tracker.
10. BookStack — wiki with a real editing UI, complements raw MkDocs markdown.

LXC candidates:

1. NetBox — IP address management and network documentation; would have caught the rocky-rpm/idee-deb/stale-hosts drift chased down by hand this cycle.
2. Semaphore UI — web UI for running Ansible playbooks instead of SSH + CLI every time.
3. Frigate — NVR with AI object detection, for whenever cameras get added.
4. Paperless-ngx — document scanning/OCR/archive.
5. Beszel — lightweight real-time resource monitoring across the fleet.
6. Wiki.js — more interactive wiki/knowledge base than raw MkDocs.
7. ntfy — simple push-notification server.
8. Vikunja — task/kanban project management; could complement or partially replace the todo.md workflow.
9. Actual Budget — lightweight personal budgeting.
10. ~~Snipe-IT~~ → Stirling-PDF — self-hosted PDF toolkit (merge, split, OCR, watermark, compress), complements ConvertX. (Snipe-IT already deployed — plow-rpm, 192.168.1.53 — see Hardware Inventory Completion below for its stale-since-05-25 refresh item.)

**Starter batch recommendation (not "install all 20 at once"):** NetBox (addresses IP/DNS drift directly), Scrutiny (✅ already done), Immich (pure upside, no dependency). Rest stays backlog, one at a time — deploy, verify, move on.

## Action Items — 2026-07-21 (live session with Chris)

- [ ] Source an AM4 CPU for shardik. No spare in hw_reserve.md. Two cannibalize candidates in the fleet, both Ryzen 5 1600X: urnst-deb (tagged "CPU swap test bench") or temerant-win (earmarked for the TrueNAS rebuild — pulling its CPU would need to be sequenced against that project). Buying new is the other option. **Deprioritized 2026-07-23 per Chris — not urgent, babar covers the primary use case. Revisit only when Chris raises it.**
- [ ] Confirm whether urnst-deb being administratively offline today is prep for the shardik CPU pull — asked, no answer yet.
- [ ] **Prometheus retention/disk decision for monitor-deb.** Currently 30d retention producing 9G on a ~32G disk; disk hit 100% full today (real outage-causing, not cosmetic — an ansible task failed with "No space left on device"). Freed ~6G today (docker prune + apt clean) as a stopgap, but this refills over time. Options: lower retention (loses history), expand the VM's disk (Kai/Proxmox-side), or accept periodic manual cleanup. **Decision pending Chris.**
- [x] Add babar to `~/ansible_dev/inventory_auto` — **done 2026-07-26.** Ran `onboard2.yml` (`proxmox` and `linux` groups, both confirmed via `grep -in babar inventory_auto`). Full config pass also landed: packages, SSH keys/hardening, Zabbix agent2. Closes the gap open since babar joined the cluster 2026-07-08.
- [ ] Clean up `inventory_auto` group membership — the `all`/default groups include many non-Ansible-manageable devices (router, network gear, printer, phones, TVs, Roomba, Windows boxes needing WinRM not SSH). Every ad-hoc/playbook run against `all` throws ~15 "UNREACHABLE" errors that are just noise, not real problems. Worth scoping a proper `[linux]`/`[proxmox]` group and keeping non-Linux devices out entirely.
- [ ] Two hosts (pihole-pi1-deb, blank-dietpi-deb) missed their apt-update step in today's baseline run due to a dpkg/apt lock collision (leftover from an earlier accidental duplicate ansible-playbook run colliding with itself) — safe to pick up on the next scheduled run, low priority.
- [ ] Verify Homepage "Pis" section icons render correctly after a refresh (`home-assistant.png`, `octoprint.png`, `pi-hole.png`, `batocera.png`, `raspberry-pi.png` — best-guess icon names against gethomepage's standard set, batocera.png especially unconfirmed).
- [ ] hw_inv.md/CLAUDE.md network table: shardik's line still says "back online 2026-06-28, 1-month uptime target" — stale now that it's confirmed CPU-dead, not touched yet since Chris didn't ask for that specific edit this session.

## Decisions Made This Session (2026-07-21)

- **Canonical TrueNAS hostname: truenas-bsd** (matches fleet naming convention — shardik-pve1-deb, maturin-pve2-deb, etc., confirmed via router DHCP table). Fixed on git-ansible (source of truth for fleet-wide DNS via homelab_baseline.yml's hosts-push task) and propagated. Router's own DHCP reservation tag was a red herring — that field (`tag`) doesn't generate DNS records in dnsmasq, only `name` does.
- **rocky-rpm moved to 192.168.1.51**, its correct range per Chris's documented IP scheme (50-69 = RPM servers). Was squatting at .20 (Debian/VM range) due to a static IP set outside DHCP.
- **octopi-deb/octopi-pi4-deb duplicate naming consolidated to octopi-pi4-deb only** (one of the four known Pi dual-naming pairs flagged in the Jordan backlog below — the other three, pi1-deb/pihole-pi1-deb, pi2-deb/blank-dietpi-deb, pi4-deb/backup-dietpi-deb, are being kept as intentional aliases per Chris, not touched).
- **swarm01/02/03 (VMs 102/104/105) confirmed fully decommissioned**, not just stopped — hw_inv.md and project memory both had them listed as "stopped/pending" for weeks; they're actually long gone. DHCP reservations and hosts entries removed to match.

## Action Items — 2026-07-16 (babar onboarding gaps, live-verified)

- [x] **Add babar to `~/ansible_dev/inventory_auto` on git-ansible** — **done 2026-07-26**, see Action Items 2026-07-21 above for detail.
- [ ] **Add babar to hosts.md hostname table** — table stops before babar joined the cluster (2026-07-08). Morgan/Jordan.
- [ ] **Add babar to backup Homepage dashboard** (backup-dietpi-deb:3002, next-server process) — likely same root cause as the Kuma manual-entry gap: no scripted onboarding step covers Homepage. Confirm with Drew/Jordan whether Homepage has a config file that can be scripted or if it's manual-UI only like Kuma.

## Action Items — Weekly Team Meeting 2026-07-12 (new this session)

- [ ] ⚠️ **Pull the shardik LXC 150 stress-ng soak test result** — test window (7 hrs, started 2026-07-08/09) closed days ago and nobody has captured the tmux pane yet. Jordan flagged this as the top open item blocking any further MCE diagnosis. `tmux capture-pane -pt <session>` on shardik, then compare timestamps against the bank 0 (2026-07-06) and bank 5 (2026-07-08/09) MCE events in `journalctl -k`.
- [ ] **Sam proposal 1 (pending Chris approval): storage.cfg node-scoping linter.** Small script to audit every dir-storage entry in cluster storage.cfg and flag any missing a `nodes` restriction — directly targets the confirmed-live SDA_store/hdd12tb/hdd3tb/nvme_store aliasing bug found on babar. Sam's pitch: catches the next one of these before it silently returns wrong data instead of erroring.
- [ ] **Sam proposal 2 (pending Chris approval): pre-push diff-check for MkDocs SCP workflow.** Wraps the todo.md/completed.md SCP step with a `git diff` against git-ansible's current state before committing, to catch working-directory/Gitea divergence before it breaks the checkbox-persist webhook — aimed at not repeating the 2026-06-28 completed.md overwrite incident.
- [ ] Taylor confirmed backup-dietpi-deb's Kuma → Telegram wiring is in fact live (per 2026-07-05 resolution) — the older "ping-only" backlog line under Taylor's Next Week list is stale and can be dropped once Chris confirms.
- [ ] Jordan reported weekly_patch.yml's 3am Sunday cron ran clean again this morning with no failure pings — fleet patch automation continues to hold.

## Action Items — Weekly Team Meeting 2026-07-19 (new this session)

- [ ] ⚠️ **Stress-ng soak test result STILL not pulled — now 10+ days stale.** Test window closed 2026-07-08/09, first flagged as top blocker at the 2026-07-12 meeting, still sitting unpulled a week later. Jordan/Kai: `tmux capture-pane -pt <session>` on shardik, compare against the bank 0 (2026-07-06) and bank 5 (2026-07-08/09) MCE timestamps in `journalctl -k`. Nothing further happens on shardik's MCE diagnosis until this is read.
- [ ] **Sam proposal 3 (pending Chris approval): hw_inv.md auto-diff-audit.** Ansible fact-gathering (RAM/storage) diffed against hw_inv.md on a schedule — targets the recurring "docs said 32GB, box has 64GB" pattern that's hit aslan and maturin twice now.
- [ ] **Sam proposal 4 (pending Chris approval): shardik MCE watcher.** Lightweight journalctl/rasdaemon poll that pings Telegram the moment a new MCE bank event lands, so the next occurrence doesn't sit undiscovered in a boot log for days.
- [x] Movies and TV backups — **confirmed done 2026-07-24.** backup_drives.md shows all active Movie/TV drives with Jun 2026 backup dates, real populated Used/Free stats, clean SMART. Matches Chris's report.
- [x] STL_ACCESSORIES_TERRAIN and STL_SOURCE_MATERIAL rsyncs — **confirmed done by Chris 2026-07-24.**
- [ ] Morgan's undocumented-changes tally: babar's three 2026-07-16 onboarding gaps (Ansible inventory, hosts.md, Homepage dashboard) are still open — carried forward again, no movement this week.
- [ ] Riley: rack Phase 1 (place rack, install SG200-50/PDU) still waiting on Chris's physical time — transport unblocked since 2026-07-12. **Chris flagged renewed interest 2026-07-24 — this is now his stated next priority.**

## Decisions Still Needed from Chris

- [ ] **Hyper-V VLAN approach for amontillado** — still open. Reasoning for why the VMs were proposed for Servers (VLAN 10) instead of Trusted (VLAN 20): Trusted is meant for physical end-user devices (amontillado itself, phones, etc.), Servers is meant for anything acting as backend infrastructure. If amontillado's Hyper-V VMs are running actual services other systems depend on, keeping them in Trusted either forces opening Trusted↔Servers broadly (defeats the segmentation) or leaves them unreachable from the rest of the infra. If they're just personal/test VMs with no service role, Trusted is fine — worth Riley confirming what those VMs actually do before deciding.

---

## Resolved This Session (2026-07-21)

- ⚠️ **Shardik's CPU confirmed dead — closes the MCE investigation thread.** Chris confirmed the CPU (Ryzen 7 2700X) is dead, not the PSU. This is the real answer to the weeks-long diagnostic chain: bank 0 MCE (2026-07-06), bank 5 MCE hitting 2 CPUs simultaneously (2026-07-08/09), the stress-ng soak test that was never pulled, RAM ruled out via clean dmidecode audits — all of it was pointing at the CPU, and now it's confirmed. The 2026-06-28 "PSU replaced, resolved" closure and the 1-month uptime target were both invalidated by this — hw_inv.md and project memory corrected. No spare AM4 CPU on hand; sourcing decision open (see Action Items above).
- **Fleet RAM capacity fully audited live** (not doc-trusted) via `dmidecode -t memory` (Linux/BSD) and PowerShell `Win32_PhysicalMemoryArray` (Windows): maturin, babar, blaine, amontillado, and truenas are all genuinely maxed at their board's real ceiling. **Only aslan has headroom** — 64GB installed, 128GB max, but all 4 DIMM slots are full so it requires swapping sticks, not adding: 2×32GB (keep 2×16GB) gets to 96GB, or 4×32GB for the full 128GB.
- **Large DNS/hosts/IP hygiene pass**, triggered by chasing the truenas-bsd naming question and expanding into a full compare of git-ansible's /etc/hosts against the router's DHCP table and active leases:
  - truenas-bsd confirmed canonical and now live fleet-wide (see Decisions above)
  - rocky-rpm migrated 192.168.1.20 → .51, verified end-to-end (router reservation, VM's own static IP, hosts file, and both inventory_auto entries all updated and confirmed)
  - aslan's duplicate DHCP reservation (stale leftover from the idee-deb→aslan rename) removed from router, hosts, and inventory_auto
  - swarm01/02/03 confirmed fully decommissioned (not stopped) — DHCP reservations and hosts entries removed, hw_inv.md and project memory corrected
  - Three devices with active DHCP leases but missing from /etc/hosts added: DIGIDIOT-DC1 (.219), ollama (.169, the babar Ollama LXC), firetv-media (.145)
  - mediastack2-deb → mediastack-deb typo (stray "2") fixed on the router
  - octopi-deb/octopi-pi4-deb duplicate consolidated (see Decisions above)
  - Full `homelab_baseline.yml` run completed fleet-wide to propagate all of the above — `failed=0` across every reachable host; remaining "unreachable" results are all expected (non-Linux devices, known-offline hosts, Windows boxes needing WinRM)
- **kasm-2404-deb (VM 111) located — running on babar, not deleted.** hw_inv.md had it listed as "stopped on aslan," which was stale on both counts: it's not on aslan at all (migrated to babar at some point after babar joined the cluster 2026-07-08), and it's actually running, not stopped. Confirmed via `qm list` on babar and a direct SSH login.
- **octopi-pi4-deb had a real (if brief) outage today** — unreachable with no DHCP lease at all, pointed to a cable/boot issue rather than an IP conflict. Resolved after a physical check; bonus finding, it's also reachable via Tailscale (100.75.54.17), which wasn't documented anywhere.
- **Duplicate ansible-playbook processes found and killed** — two extra copies of the same baseline run were stacked on top of the original, almost certainly the cause of an earlier 40-minute hang (dpkg/apt lock contention matches this exactly, see the pihole-pi1-deb/blank-dietpi-deb item above).
- **Homepage dashboard: added a "Pis" section.** The entire Raspberry Pi fleet was missing from the dashboard — not a bug, just never built out. Home Assistant, OctoPrint, Pi-hole, and Batocera got real clickable links; the DietPi/RetroPie/offline boxes got ping-only status tiles since they have no web UI to link to.
- ⚠️ **monitor-deb hit 100% disk full mid-session — real, not cosmetic.** Root filesystem had 0 bytes free, confirmed by an actual ansible task failure ("No space left on device"), not just a warning. Root cause: Prometheus data (9G under a 30-day retention window — not misconfigured, just genuinely that much data on a small ~32G disk) plus 2.17G of safely-reclaimable unused Docker images. Freed the Docker images + apt cache, now at 88%/3.6G free — stable for now, but not a permanent fix since Prometheus will keep growing back toward the retention ceiling (see Action Items above).

---

## Resolved This Session (2026-07-08 → 2026-07-09)

- **Babar joined the Proxmox cluster as the 5th physical node.** Found as an undocumented fresh Proxmox VE install at 192.168.1.12 (default hostname "pve"), renamed to babar (elephant, Jean de Brunhoff — see Naming Reference), enterprise repos disabled/no-subscription repo added, updated to pve-manager 9.2.4 / kernel 7.0.14-4-pve, joined via `pvecm add`. Full hardware catalogued: Dell Pro Tower Plus QBT1250, Core Ultra 7 265 (20 cores, up to 6.5GHz), 128GB DDR5-4800, RTX 5060 (8GB) + Intel Arrow Lake-S iGPU, 4x M.2 slots (1 populated at purchase, 2 more filled this session with a 128GB WD PC SN520 and a 512GB SK hynix PC300 — mounted as `nvme128`/`nvme512` Proxmox dir storage). **Most capable node in the cluster.** hw_inv.md updated with a full babar section — still missing the final nvme128/nvme512 storage table entries (see Hardware Inventory Completion below).
- **Corosync qdevice permanently removed — not just fixed.** Was co-located on git-ansible (itself a VM running on maturin), making it a single point of failure that could double-fail quorum — Chris caught this. Separately, babar joining brought the cluster to 5 nodes (odd), and Proxmox's own `pvecm qdevice setup` now refuses to attach a qdevice to an odd-node cluster ("Clusters with an odd node count are not officially supported!") — confirming a qdevice is actively unsupported here now, not just unnecessary. **Do not re-add unless node count goes even again**, and if it ever does, use genuinely independent hardware, not a VM riding on one of the cluster's own nodes.
- **kasm-2404-deb (VM 111) migrated off shardik to babar's local-lvm**, live. hw_inv.md had this VM's location wrong (documented as aslan) — actually found running on shardik via `qm list`, corrected before the migrate command was run against the wrong node.
- **Isolated shardik stress test set up** — once VM 111 was off, created a dedicated LXC (150) on shardik and ran stress-ng (`--matrix --fma --cpu --cpu-method all`) for 7 hours in tmux, specifically to try to reproduce the CPU MCE fault in isolation from any production workload. **Result not yet checked — pending.**
- **Shardik's CPU MCE fault further decoded** (from `journalctl -k -b -1`): bank 5, decoded as the CPU's execution unit (not the memory controller) on this chip's SMCA bank mapping, with UC+PCC set (uncorrected, processor-context-corrupted — fatal-class, hit 2 CPUs simultaneously). RAM increasingly ruled out as the cause — this fault is distinct from the earlier bank 0 MCE and from the DIMM issue already fixed. Points more toward CPU or motherboard VRM than memory. **Still unresolved — awaiting the stress-ng soak test result before further action.**
- **aslan and maturin RAM corrected in hw_inv.md** — both were stale at 32GB, actually confirmed at 64GB (4x16GB DDR4) via `dmidecode -t memory` on each host. Recurring pattern this session: don't trust hw_inv.md's hardware figures without a live `dmidecode`/`lscpu` check first.
- ⚠️ **Near-miss: generic `apt install nvidia-driver` on babar attempted to remove `proxmox-ve` and the PVE kernel entirely.** Blocked automatically by Proxmox's own `pve-apt-hook` safety mechanism — no actual damage. Root cause: the generic Debian nvidia-driver metapackage drags in a full X11 desktop stack + conflicts with PVE's kernel packages, wrong tool for a headless hypervisor host. **Do not run `apt install nvidia-driver` (or any variant) on a Proxmox host — use NVIDIA's official `.run` installer instead.**
- **NVIDIA driver installed on babar via the official `.run` installer** (610.43.03, `-m=kernel-open` — mandatory for RTX 5060/Blackwell GPUs, `--dkms` for kernel-update persistence), Secure Boot Machine-Owner-Key (MOK) signed and enrolled at the physical console. **Gotcha for next time:** the MOK enrollment screen appears *before* GRUB, not after — easy to miss if watching for the boot menu; a missed/dropped enrollment shows as `mokutil --list-new` returning empty after a reboot that should have prompted. Also, the actual signing cert isn't DKMS's own key — the NVIDIA installer generates and uses its own cert at `/usr/share/nvidia/nvidia-modsign-crt-<random>.der`; check `modinfo nvidia | grep -i sig` for the real signer rather than assuming.
- **Ollama deployed on babar with full RTX 5060 GPU passthrough**, confirmed working with live model inference (llama3.2:3b, 53% GPU utilization, 2GB VRAM). Architecture: privileged LXC (102, 8 cores/16GB RAM, rootfs on the new `nvme512` storage), GPU passed through via `lxc.cgroup2.devices.allow`/`lxc.mount.entry` cgroup2 rules rather than full PCIe passthrough — far simpler than fighting unprivileged UID/GID idmap for a homelab use case. Matching userspace-only driver (`--no-kernel-module`) installed inside the container. Full architecture and gotchas saved to memory for reuse if GPU passthrough is needed elsewhere.
- ⚠️ **CORRECTION 2026-07-16: "Babar fully onboarded into fleet management" (below, originally logged 2026-07-08/09) was wrong on the Ansible piece.** Verified live via `grep -i babar ~/ansible_dev/inventory_auto` on git-ansible — babar is NOT in `[proxmox]` or `[linux]` groups. It is confirmed in `/etc/hosts` (192.168.1.12) but missing from `inventory_auto`, missing from hosts.md's hostname table, and missing from the backup Homepage dashboard (backup-dietpi-deb:3002). Original (inaccurate) claim preserved below for record: Zabbix agent2, Prometheus node_exporter, and Uptime Kuma manual entry are still believed accurate — only the Ansible inventory and doc/dashboard entries are confirmed missing. Original text: "Babar fully onboarded into fleet management — Ansible inventory (`[proxmox]` and `[linux]` groups in `inventory_auto`, via the actual `onboard2.yml` playbook, not hand-edited), Zabbix agent2, Prometheus node_exporter (native systemd install, not Docker — babar has no Docker), Uptime Kuma (manual UI entry, no scripted path exists for Kuma registration in this repo)."
- **Cluster storage.cfg node-scoping risk confirmed live, not just theoretical.** `pvesm status` on babar shows SDA_store, hdd12tb, hdd3tb, and nvme_store all reporting identical Total/Used/Available numbers, matching `local` exactly — these storage definitions aren't scoped with a `nodes` restriction, so on a node where the "real" underlying path doesn't exist, they silently alias local root-disk stats instead of erroring. `tank-storage` (zfspool) fails outright on babar (`cannot open 'tank': no such pool`) for the same underlying reason. **Needs a `nodes` restriction added to each of these storage.cfg entries — real data-misdirection risk for anyone trusting these names cluster-wide, directly relevant to CRU/STL backup rotation.** Not yet fixed.

## Resolved This Session (2026-07-06)

- **Red case hostname decided: Garm.** (dog, Norse mythology, Hel's hellhound). Confirmed — no longer ambiguous with the freenas naming question below.
- **TrueNAS (freenas-bsd) rebuild hostname decided: Gan.** New name, not drawn from the original reserve pool — Dark Tower reference (the prime creative force behind the Beams), fits the existing shardik/maturin/aslan/blaine theme. Morgan/Jordan to apply once the TrueNAS hardware rebuild actually happens (still blocked on the M1115 HBA).
- **Shardik RAM issue addressed** — bad DIMM handled. Gate before resuming the uptime clock: sustained stress test/benchmark, not just another memtest pass (Jordan/Kai).
- **Priority call for 2026-07-07: switch bench test over SMART monitoring wiring.** Chris judged this more impactful than Taylor's smartd_telegram_alert.sh wiring (not urgent right now). Clarified: this is testing the SG200-50/SG-1100 **in place on top of freenas-bsd**, not a rack install — matches Riley's existing "offline config, laptop direct to LAN, not live network" plan. Rack is still offsite and not a blocker for this.
- **Internal DNS raised as a want** — Chris flagged that DNS (resolving hostnames like garm/gan/garuda instead of raw IPs) would help, but noted it likely depends on the switch/VLAN work landing first. Logged against the existing Unbound backlog item below; not actioned — Riley to scope sequencing against the rack/VLAN rollout.
- **Proxmox "wheel" cluster lost quorum 2026-07-06 (~06:10am)** — maturin dropped to seeing only itself (`Nodes: 1`, `Quorate: No`), blocking `qm start` on VM 101 (monitor-deb) and VM 106 (git-ansible) with "cluster not ready - no quorum?". Root cause: corosync (knet) links between maturin and the rest of the cluster were flapping under real network instability — shardik/aslan/blaine all still pingable, but with high jittery latency (shardik especially: 64-199ms swings), consistent with the network health concerns already flagged from earlier tonight (aging GS116 switch). Not a dead-node event.
  - **Key finding: VM 101 and VM 106 were never actually down.** `qm start` reported "already running" for both once management access was restored — the entire incident was Proxmox's cluster-management layer (pmxcfs going read-only without quorum) blocking status/commands, not an actual service outage. Confirmed both hosts pingable with clean sub-ms latency throughout.
  - **Architecture gap found:** the corosync qdevice (tie-breaker vote) depends on qnetd, which lives on git-ansible — VM 106, itself a VM inside this same cluster. When quorum is lost, the VM hosting the tie-breaker can't start without quorum, and quorum can't easily recover without the tie-breaker — a circular dependency. **Recommend qdevice/qnetd be moved to infrastructure outside the Proxmox cluster it arbitrates for** (e.g., a bare host or a VM in a different cluster/no cluster at all) — Kai/Riley to evaluate.
  - **Recovery path used:** `pvecm expected 1` and direct `corosync-cmapctl` writes were both refused (corosync enforces a hard floor of 2 expected votes, won't allow literal single-node quorum via those interfaces). Actual fix was the documented "break glass" procedure: `systemctl stop pve-cluster` + `pmxcfs -l` (forces `/etc/pve` writable locally, bypassing quorum). Once VMs were confirmed already running, the override was reverted cleanly (`systemctl start pve-cluster`, after killing the manual `pmxcfs -l` process first to avoid a service-start conflict). Maturin is back to normal cluster-aware mode (still correctly showing `Quorate: No` since the underlying network partition itself is unresolved).
  - **Still open:** why corosync/knet is flapping between maturin and the other three nodes despite basic ICMP connectivity working. Likely same root cause as the GS116 switch concerns — worth prioritizing alongside tomorrow's SG200-50 bench test rather than treating as unrelated.
- **Same quorum issue recurred ~06:30-06:50am, same morning, ~20 min after the first fix.** Maturin dropped out again (Nodes: 1, Quorate: No) while the rest of the cluster (shardik/aslan/blaine + qdevice) stayed quorate throughout — confirms this is an isolated, repeating maturin↔network problem, not a one-off. Diagnostic findings this round: `journalctl -u corosync` on maturin showed the knet link to aslan (node 3) repeatedly dropping and reconnecting every 6-20 seconds; NIC-level checks on both ends came back clean (maturin `enp0s31f6` and aslan `nic0` both 1000Mb/s, full duplex, link up — rules out bad negotiation on either host's own port); a 100-packet sustained ping from maturin to aslan showed 0% loss but abnormally jittery latency for same-subnet gigabit (12-41ms, mdev 4.6ms, should be sub-1ms) — real evidence pointing at switch-side congestion or a marginal port rather than a dead cable or bad NIC. Matches the standing GS116 suspicion.
  - **Resolution:** same break-glass (`systemctl stop pve-cluster` + `pmxcfs -l`) restored maturin's config access immediately. Before reverting, corosync self-recovered on its own (`pvecm status` showed `Nodes: 4, Quorate: Yes` while still in local mode) — reverted cleanly (`kill` on the manual `pmxcfs -l` process + `systemctl start pve-cluster`), maturin rejoined normally, confirmed `Nodes: 4, Quorate: Yes` with no stray processes.
  - **Root cause still unresolved and now confirmed recurring within the same morning** — this is no longer a one-off, it's an active intermittent fault. Elevates the SG200-50/switch bench test priority for 2026-07-07 from "worth doing" to "should happen before this happens a third time, possibly during working hours with more at stake."
- **Network jitter confirmed NOT isolated to maturin↔aslan — broader, same morning (~08:00am).** SABnzbd (mediastack-deb, 192.168.1.36) threw a "Lost connection" banner in the WebUI; container itself was confirmed healthy/running (Docker, up 4 days, port 8090→8080 mapped correctly) — not a crash. A 20-packet sustained ping from mediastack-deb to the gateway (192.168.1.1) showed 0% loss but severe jitter: 43-214ms, mdev 53.5ms — markedly worse than the maturin-aslan numbers, and this time to the router itself, not between two cluster nodes. Confirms this is shared upstream hardware degrading (almost certainly the GS116), not a single bad link/port/cable. Ties the Proxmox flapping and the SABnzbd UI drop to the same root cause.
  - **Decision: switch swap deferred a few hours, not to tomorrow** — Chris opted to wait rather than do it immediately when this was found (~08:00am 2026-07-06). Bench-test the SG200-50/SG-1100 (in place, on top of freenas-bsd, offline/laptop-direct config per Riley's plan) later today once Chris is back on it — no longer just "tomorrow's priority," this is the same morning, elevated given confirmed multi-host impact.
- **ROOT CAUSE FOUND AND FIXED (~08:20am): loose GS116 power adapter, not the switch itself.** Chris found the switch's 12V 2A adapter was loose/not seated properly and replaced it with a proper snug Netgear 12V 1A adapter. This **supersedes** the "GS116 hardware degrading" theory above — a loose power connection causing intermittent brownouts/resets explains the jitter far better than switch-side congestion, and explains why it hit multiple unrelated hosts (mediastack-deb, maturin↔aslan) simultaneously. **Verified, not just assumed:** mediastack-deb→gateway ping went from 43-214ms/mdev 53.5ms (pre-fix) to 0.44-0.62ms/mdev 0.037ms (post-fix) — genuinely healthy LAN latency. Maturin rejoined the cluster cleanly (`Nodes: 3, Quorate: Yes`, no drops) shortly after. **Switch bench test (SG200-50) downgraded back to non-urgent** — this was a power connector fault, not a failing switch; the managed-switch/VLAN project can proceed on its original timeline rather than emergency-elevated.
- **Shardik RAM re-verified 2026-07-06 ~1:12pm — stress test passed, BIOS-level confirmation done before reboot.** Full stress test (not just another memtest pass) completed and passed, satisfying the gate set earlier today. BIOS checked while open: system clock accurate (07/06/2026 13:12, confirms CMOS battery replacement is holding), all 4 DIMMs present and matching (DDR4_A1/A2/B1/B2, 8GB DDR4-2400 each, 32GB total — DIMM fix confirmed clean), H/W Monitor rails all healthy (12V/5V/3.3V all within tolerance, no sag; CPU 41°C/M-B 39°C idle-normal). **Gate satisfied at the time — uptime clock resumed, but see below: real post-flash instability occurred ~09:49-10:26am. Chris has not yet confirmed whether this resets the clock — open question, not decided.**
- **[DONE] Shardik BIOS update 10.43 (Beta) → 10.50 (stable), completed ~1:20pm 2026-07-06.** Flash succeeded during a thunderstorm (not on UPS, real risk, held anyway) — confirmed via BIOS Main screen showing `P10.50`, all 4 DIMMs still present/matching post-flash. fTPM was disabled pre-flash per ASRock's own advisory (fTPM re-provisioning risk during this AGESA bump) and re-enabled successfully after. Boot order restored to `proxmox (NVMe)`. **Caveat for the record:** 10.50's actual changelog is just a Secure Boot Key update (2023 KEK/DB/PK) — not a stability/perf fix. The real stability fixes this week remain the PSU replacement, CMOS battery, and DIMM swap (all hardware). Don't credit this BIOS update if shardik hiccups again — hardware gets the scrutiny first.
- **Post-flash boot surfaced a stale storage entry, not a real problem.** First boot after the flash threw `Timed out waiting for device .../b02f39e7-...` and `Dependency failed for mnt-pve-DIR_SDA.mount` — looked alarming but confirmed harmless: `blkid`/`zpool status` show the "tank" ZFS pool (raidz1, 4x disk, 21.8TB) is fully healthy with no errors, and none of the 4 physical disks (sda-sdd, all ZFS tank members) hold that UUID. The "DIR_SDA" Proxmox storage definition is orphaned — points at a UUID that doesn't exist on any currently-installed disk. **Confirmed by Chris: this is a known legacy entry from the earlier ZFS failures caused by the bad RAM** (the same DIMM issue fixed this week) — not a new/mystery disk, just leftover config debris from that incident that was never cleaned up. Not blocking anything (shardik booted clean, VM 111 running, tank pool untouched/healthy). **Low-priority cleanup for Alex:** remove the stale "DIR_SDA" storage entry from Datacenter → Storage — config cleanup only, no ZFS pool/data changes needed.
- **Shardik: real instability found post-BIOS-flash (~09:49-10:26am), root-caused and resolved.** Chris reported shardik "crashed 2x" after the BIOS update. `ssh shardik` initially failed with "No route to host" — not a DNS/hostname issue (SSH by IP worked fine). Real findings: (1) `journalctl --list-boots` showed the current boot's timestamps wildly wrong (dated April 13 instead of July 6) — evidence the RTC came up stale immediately after the BIOS flash reset defaults; (2) corosync threw `quorum_initialize failed: CS_ERR_LIBRARY` right at boot (09:49:19), consistent with a wrong clock breaking corosync until NTP corrected it; (3) `pve-replication-state.json` was left completely empty (0 bytes), causing `pvescheduler` to log "invalid json data" every minute continuously from 09:49 through at least 10:26. **Current state:** `timedatectl` confirms clock now correct/NTP-synced (verified 14:32). `replication.cfg` is empty — no real replication jobs configured, so the JSON error was cosmetic, not masking a real failure. Fixed by writing `{}` to the state file; confirmed no recurrence since. **Separately noted, not yet investigated:** repeated failed root SSH login attempts from git-ansible (192.168.1.3) at 10:10:02 — unclear if related, worth a look.
- **CRU scripts now under real version control — new Gitea repo `homelab-scripts`.** Found today that `cru_hotplug.sh`, `cru_vm_detach_check.sh`, `build_drives_db.py`, `drives.db` (blaine) and `cru_stats.sh`, `backup_drives_update.sh`, `update_drives_table.py` (restic-deb) were all loose, unversioned files with zero backup/history. Created `homelab-scripts` on Gitea (git-ansible), cloned onto both hosts with a subfolder each (`blaine/`, `restic-deb/`), committed and pushed both sets.
- **CRU backup workflow fully documented — new runbook + nav section.** `cru_backup_workflow_runbook.md` created covering onboarding (snapshot → detect → identify → preflight → attach → mount), running the backup, the exit script chain, offboarding, and the docs sync — the "10 steps that took hours" from 2026-07-03's hotplug automation work finally written down. Added a "Runbooks" nav section to `mkdocs.yml`.
- **Two real script bugs found, one fixed today:** (1) FIXED — `update_drives_table.py` never parsed the Backup date even though `cru_stats.sh` was already writing a timestamp header; extended it to parse and populate Backup automatically, same as Used/Free/SMART, verified live on the site. (2) NOT YET FIXED — `cru_vm_detach_check.sh` and `cru_hotplug.sh` (cmd_preflight) call `qm unset`, invalid on this Proxmox version; correct syntax is `qm set <vmid> --delete <slot>`. Worked around live, scripts still need the fix — queued for Sam/Kai.
- **`backup_drives.md` reconciled between blaine and the live site** — blaine's local copy had drifted ahead (STL_ACCESSORIES_TERRAIN, STL_SOURCE_MATERIAL rows existed locally but never reached the site). Pushed accurate data up, alphabetized the STL Archive Drives table, added an explicit alphabetization rule to the file.
- **CRU drive swap completed: 3 old drives out, 3 known archive drives back in.** STL_ACCESSORIES_TERRAIN, STL_SOURCE_MATERIAL, and FUTURE_USE pulled. The "new" 3 drives onboarded (cru1/cru2/cru3) turned out to be existing archive drives rotating back in, not new hardware — confirmed by Chris (full archives already on them) after serial numbers closely matched existing Books-section rows. Relabeled NTFS volumes to match canonical doc labels for auto-stats matching going forward: cru1 → **READING**, cru2 → **TROVE NOT BOOKS** (content confirmed as a thetrove.is wget mirror, not audiobooks — sticker "Audiobooks 24-02" was simply wrong), cru3 → **D&D GAMING**. Doc row "AUDIOBOOKS 3TB" renamed to "TROVE NOT BOOKS" (same serial WMAW20629019) and re-alphabetized. All 3 drives came up read-only (NTFS "unclean file system" — not safely ejected from Windows before pulling); fixed per-drive with `ntfsfix -d`, confirmed read-write after. Added this failure mode to the CRU runbook's troubleshooting table. `cru_mount_vm.sh`'s `UUID_MAP` updated and committed to `homelab-scripts`. **Not yet run: the exit script chain** (`cru_stats.sh`/`backup_drives_update.sh`) — deliberately held off since no rsync has actually landed on these 3 drives yet this session; running it now would falsely stamp a Backup date. Run it after the actual backup work happens.
- **Live rsync test onto cru1 (READING) confirmed the switch/power-adapter fix under real load.** ~25-29MB/s sustained, versus ~400kbps pre-fix — good evidence the fix holds under real transfer load, not just idle pings. Synced `Reading 420 RIF` (renamed to `READING_0726` on both plex source and cru1 to match) — 178.3GB / 28,426 new files, in progress via tmux (see below).
- ⚠️ **Shardik rebooted again, unprompted, ~19:37 same day — NEW finding, distinct from the earlier RTC issue.** `journalctl -b -1 -p err` showed a genuine hardware Machine Check Exception: `mce: [Hardware Error]: CPU 6: Machine Check: 0 Bank 0: baa0000000060135`. This is a real CPU/hardware-level fault — RAM already passed two stress tests this week, so this points elsewhere (CPU, motherboard, or power delivery, consistent with the standing PSU-suspect theory). Corosync also failed to init right after this reboot (`quorum_initialize failed: CS_ERR_LIBRARY`), but this time the clock was correct/NTP-synced — a different cause than the earlier RTC-driven failure, and it cleared on its own; cluster confirmed fully quorate (`sudo pvecm status`: Nodes 4, Quorate Yes) once checked with sudo (unprivileged `pvecm status` throws `ipcc_send_rec` errors — a permissions artifact, not a real problem). Also recurring: failed root SSH auth attempts from git-ansible (192.168.1.3), now seen twice today (10:10:02 and 19:10:01) — still not investigated. **Not resolved. MCE needs Jordan's review before anything further gets tried on shardik.**

---

## Resolved This Session (2026-07-05)

- **Patch reboots vs. shardik uptime clock** — Chris's ruling: scheduled patch reboots do **not** reset the clock; only unplanned freezes/outages do. Note this doesn't help this week anyway — see below.
- **Shardik uptime clock reset again 2026-07-05** — accidental unplug (not a repeat PSU failure, confirmed by Chris), caught via the new backup-dietpi-deb Kuma monitor and recovered before Chris even checked. Per the ruling above, this **does** count (real outage, not a patch reboot) — new target ~2026-08-05, pending final confirmation. No alert fired because backup-dietpi-deb's Kuma has no notification channel wired yet — folded into Taylor's queue below.
- **garuda = pve3**, confirmed. This matches the original naming-list reservation ("garuda reserved for next new physical node") — the red case needs a different name, see Decisions above.
- **Sam's two proposals approved**: general alert relay bot (Kuma/Zabbix/SMART → one Telegram channel) and the CRU label linter script. Both now active, queued below.
- **STL rsync throughput crisis confirmed top priority** — Alex/Riley/Taylor target root cause by 2026-07-12.
- **cru_stats.sh path fix — Alex signed off 2026-07-05.** Sam cleared to ship.
- **VPN rationalization decided: Tailscale.** WireGuard (mediastack) and ZeroTier (amontillado) — decommission both.
- **blank-dietpi-deb renamed docs-dietpi-deb** — role: documentation-adjacent host (extends the "Gitea mirror secondary" option toward actually serving docs, not just mirroring the repo).
- **STL rsync throughput — major improvement: ~400kB/s → 25MB/s (~60x).** No longer a viability crisis (2.7TB is now ~30 hours, not 44 days). Root-cause work continues but the backups aren't blocked anymore — downgraded from top priority.
- **Rack is currently offsite** — needs Chris's car to transport home before Phase 1 (placement) can even start.
- **Telegram bot fully deployed and verified 2026-07-05.** OerthBot live on git-ansible (`/opt/scripts/notify_telegram.py`, config at `/etc/oerthbot/config.json`, mode 600), admin of OerthChannel, test message confirmed delivered.
- **weekly_patch.yml Telegram integration — done and tested 2026-07-05.** Rewrote against the actual live version (the local draft was stale — apt-only, no RedHat/Suse, gather_facts off). Added per-host reboot/failure notifications (delegate_to localhost, ignore_errors) plus a run-complete ping from a second play targeting `git-ansible-deb` (inventory hostname, not "git-ansible"). Backed up as `weekly_patch.yml.bak-2026-07-05`. Live-tested with `--limit git-ansible-deb --ask-vault-pass` (real run, not `--check` — command tasks always skip under `--check`) — completion ping confirmed delivered to OerthChannel. Ready for the real Sunday 3am fleet-wide run.
- **Kuma → Telegram: done 2026-07-05.** Both instances (monitor-deb and backup-dietpi-deb) configured with OerthBot, "apply to all monitors" checked — closes the exact gap that missed today's shardik unplug.
- Remaining: (1) SMART alerts via smartd — script (`smartd_telegram_alert.sh`) is deployed to `/opt/scripts/` but not wired into smartd.conf, and it's unconfirmed whether smartd runs as a continuous daemon anywhere vs. one-off manual `smartctl` checks; (2) Zabbix's native Telegram media type — unconfirmed whether the Zabbix web frontend is actually deployed/reachable yet.

---

## Next Week — Assigned (2026-07-06 → 2026-07-12)
_Every specialist gets ≥5 pulled tasks. Goal: clear backlog before scope creep adds more. Full context for each item is in the system-based backlog further down._

### Jordan
1. Amontillado C: drive audit — 7% free, find what's consuming it
2. fail2ban rollout via Ansible across all SSH-exposed hosts
3. Git identity (user.email/user.name) on restic-deb
4. DC salvage: scavenge remaining 2 DC machines for 32GB DDR4 UDIMM sticks (need 6 more for shardik+aslan grail RAM)
5. Onboard pbs-deb via onboard2.yml (passwordless sudo + SSH key auth)
6. Add Zabbix repo task to homelab_baseline.yml (before agent install)
7. ⚠️ **Shardik MCE (Machine Check Exception) found 2026-07-06 ~19:37** — `CPU 6: Machine Check: 0 Bank 0: baa0000000060135`. Real hardware-level fault, not the RAM (already stress-tested twice) or the earlier RTC issue. Needs proper diagnosis (mcelog/rasdaemon if available) before anything else gets tried on shardik.

### Kai
1. Manyfold/blaine LXC (CT 103) — one more week, then confirm as permanent home or move
2. Spec pve3 (garuda) Tailscale clustering — corosync over WAN, cold/warm failover runbook
3. Add pve3/garuda to the Proxmox cluster (now that the name's confirmed)
4. Right-size VM RAM allocations audit across all nodes
5. Investigate maturin VM 112's orphaned 164GB disk on shardik NVMe
6. GPU transcoding prep for aslan passthrough (joint with Casey, once RAM allows)

### Sam
1. ~~Ship the cru_stats.sh / backup_drives_update.sh path fix~~ — **CONFIRMED ALREADY DONE 2026-07-06.** Checked `backup_drives_update.sh` directly: it already reads from `/opt/cru_stats` correctly and pushes via Gitea API, not a local git clone. This item was stale.
2. Build the general alert relay bot (Kuma/Zabbix/SMART → Telegram) — approved
3. Build the CRU label linter (scans scripts/configs for stale cru3-style labels) — approved
4. auto network_inventory.md script — arp-scan + masscan + ansible facts combined
5. Validate backup_drives_update.sh Gitea-API refactor — one week of clean runs before calling it trusted
6. ~~automate the `backup_drives.md` Backup date column~~ — **DONE 2026-07-06.** `update_drives_table.py` extended to parse the existing `=== label - $(date) ===` header line from each `/opt/cru_stats/<label>.txt` file and populate Backup the same way it already does Used/Free/SMART. Deployed via heredoc directly on restic-deb, ran clean end-to-end (`cru_stats.sh` → `backup_drives_update.sh` → Gitea API push succeeded), confirmed live on the site (STL_ACCESSORIES_TERRAIN, STL_SOURCE_MATERIAL both showing "Jul 2026", sourced from real data not hand-entry). **Still open, not yet fixed:** the two `qm unset` bugs in `cru_vm_detach_check.sh` and `cru_hotplug.sh` (cmd_preflight) on blaine — needs `qm set <vmid> --delete <slot>` instead. Queued for Sam/Kai.
6. merge-aware todo_sync.sh — cron on git-ansible preserving Gitea `[x]` state on pull

### Riley
1. Flint 2 AP-mode cutover pre-work (dumb AP, trunk GE1, tagged VLANs 10/20/30/99)
2. pfSense SG-1100 offline config (WAN, DHCP, VLAN interfaces, firewall rules) — laptop direct to LAN, not live network
3. Prepare both Hyper-V VLAN options (trunk+vSwitch vs. second NIC) as a documented decision for Chris
4. DHCP reservation for octopi-pi4-deb (lock 192.168.1.122)
5. pve3/garuda Tailscale setup on the ThinkStation
6. Decommission WireGuard (mediastack) and ZeroTier (amontillado) — Tailscale confirmed as the sole VPN 2026-07-05

### Morgan
1. This reorg — todo.md sorted into system-based sections (done this session, keep maintaining it this way going forward)
2. Clean up the undocumented-changes tally, keep it current
3. Session runbooks: shardik recovery, red case inventory page, PBS migration decision log, pve3 DR node page
4. Set holy_grail.md as the MkDocs front page (docs/index.md or nav reorder)
5. Cluster capacity page — mobo/CPU/RAM/VM placement per node, upgrade path (Kai + Jordan feed data)
6. MkDocs Network section overhaul with Riley — network_inventory.md, network_diagram.md, hosts.md, vlan_design.md

### Alex
1. ⚠️ **Verify CRU onboard/offboard scripts before tomorrow morning's swap (2026-07-06)** — this is time-sensitive
2. Scope a web frontend for the drive database + hardware inventory + wishlist
3. Research LAGG + CIFS multisync + TrueNAS community edition as a future path
4. Investigate Plex mount options optimized for high small-file IOPS (STL/RomM libraries)
5. STL rsync throughput root-cause, joint with Riley/Taylor — de-escalated 2026-07-05 (400kB/s→25MB/s improvement), continue at lower urgency
6. STL_FIGURES label audit — confirm no scripts still reference old cru3 names

### Taylor
1. ~~Wire an actual notification channel into backup-dietpi-deb's Kuma instance~~ — **stale, removed 2026-07-26.** Telegram wiring confirmed live 2026-07-05.
2. Configure Zabbix → Telegram alerting
3. Set Uptime Kuma's TrueNAS poll interval to 30 seconds
4. Document the full Zabbix topology — server on monitor-deb, 11 agents, confirm whether Grafana pulls from it
5. Coordinate with Sam on the new alert-relay bot — Taylor owns which alerts route through it
6. Wire smartd_telegram_alert.sh into smartd.conf (-M exec directive); confirm smartd runs as a persistent daemon vs. one-off manual smartctl checks

### Casey
1. Evaluate Overseerr or Wizarr for Plex request management
2. Investigate Plex audio normalization options (new ask from Chris)
3. Add Tautulli for Plex analytics
4. Add Bazarr for subtitle automation
5. Resolve the Plex Music library mobile bug (Plex Pass confirmed active)
6. GPU transcoding — coordinate with Kai once aslan RAM allows

### Drew
1. Finish the Ender 3 V2 temp tower calibration, confirm a dialed-in profile
2. Bring argos-pi4-deb online, confirm wall-mount location with Chris
3. Onboard argos via Ansible (onboard2.yml)
4. Spec PoE switch + PoE HATs for single-cable Pi rack wiring
5. Logitech Z-680 2.1→5.1 diagnosis — rear/center channels still not resolved (separate from today's fixed static issue)

### Chris (Owner)
_Things only you can do — accounts, purchases, physical presence, final calls._
1. Pick red case hostname from the remaining 8: babar, navius, rocinante, garm, chuchundra, jasconius, camazotz, owsla
2. Confirm argos-pi4-deb wall-mount location — Chris has no strong preference, Drew/Jordan can pick a practical spot and proceed unless a hard constraint comes up
3. ⚠️ Check temerant-win's 2x 3TB HDDs for important data before it gets gutted for the TrueNAS rebuild
4. Order 2x SFF-8087 to SATA breakout cables (~$5-10 ea, eBay) — needed before Jordan finishes the HBA install
5. Decide Hyper-V VLAN approach for amontillado — trunk+vSwitch vs. second NIC (Riley's prepping both options, final call is yours)
6. Physical: desk wire tidy — full shutdown and rewire
7. DC salvage: schedule DC2 walkthrough, confirm DC3/DC4 status, retrieve the 12U half rack — needs your physical presence
8. Photograph the 5 waiting systems, pve3, printers, GPUs, and laptops for hw inventory / Snipe-IT import
9. Rack build Phase 1: place the rack in its final location, install SG200-50/patch panel/PDU — physical prep before Riley's config goes live

---

## Backlog by System
_Full context for every item above, plus everything else not yet scheduled. Organized by domain, not by "when."_

### Shardik & Cluster Stability
- ✅ **CPU confirmed dead 2026-07-21 — closes this entire diagnostic thread.** The stress-ng soak test result below was never actually pulled, but it's moot now: Chris confirmed the CPU itself (Ryzen 7 2700X) is dead. This is the real answer to both MCE findings below (bank 0 2026-07-06, bank 5 2026-07-08/09) and the "CPU or motherboard VRM" suspicion — it was the CPU. See Action Items — 2026-07-21 for the sourcing decision (no spare AM4 CPU on hand).
- [ ] ~~Check result of the 7-hour stress-ng soak test in isolated LXC 150~~ — superseded, CPU confirmed dead by other means 2026-07-21, this result no longer matters for diagnosis. Leave the tmux session be or clean it up next time shardik's touched.
- ⚠️ **Second, distinct MCE bank decoded 2026-07-08/09: bank 5 (execution unit), UC+PCC set, hit 2 CPUs simultaneously** — `journalctl -k -b -1`. Different bank than the 2026-07-06 bank 0 finding below. RAM continues to look ruled out (aslan/maturin DIMM audits both came back clean and were actually a documentation error, not a hardware fault). **Resolved 2026-07-21 — this was the dead CPU.**
- ⚠️ **Machine Check Exception found 2026-07-06 ~19:37.** `CPU 6: Machine Check: 0 Bank 0: baa0000000060135` (VAL/UC/EN/PCC all set — Processor Context Corrupted, which is why it forced a reboot) in the previous boot's error log. **Correction to the standing "PSU suspected" theory: shardik's PSU is already new (replaced this week) — a fresh PSU covers wall→12V stability but is a different component from the motherboard's own VRM (steps 12V down to CPU core voltage).** **Resolved 2026-07-21 — this was the dead CPU, not the PSU or VRM.**
- [ ] Repeated failed root SSH login attempts from git-ansible (192.168.1.3) against shardik — seen twice today (10:10:02 and 19:10:01), still not investigated. Could be a misconfigured Ansible/cron job on git-ansible or something worth a closer look.
- ⚠️ **Shardik hung/froze 2026-07-05 evening — separate incident from this morning's accidental unplug.** Symptoms: frozen display, keyboard LEDs unresponsive to toggle, unreachable via ping/SSH from multiple hosts (amontillado, aslan), not present in `pvecm status` membership at all. Cluster itself stayed quorate throughout (maturin/aslan/blaine fine) — no impact to other nodes. Hard power-cycled to recover; came up in Memtest86+ (intentional, Chris wanted to run it).
- ✅ **Shardik RAM issue addressed 2026-07-06** — bad DIMM (moving-inversions failure, 30-31GB range, found 2026-07-05) identified and handled. Known-good spares in reserve if still needed: 2x G.Skill Trident Z RGB 8GB DDR4-3200 (memtest-clean 2026-06-29). **Next step: sustained benchmark/stress test (not just memtest) to confirm stability before trusting it and resuming the uptime clock** — Jordan/Kai.
- ⚠️ **Hardware documentation mismatch discovered 2026-07-05 — needs reconciling once shardik is stable.** Memtest86+ shows shardik's actual live hardware as: **AMD Ryzen 5 1600 (6c/12t)**, not the documented Ryzen 7 2700X (8c/16t); **32GB RAM (4×8GB: 1x Team Group DDR4-2400 + 3x Micron DDR4-2666 2019-W43)**, not the documented 64GB maxed. hw_inv.md and project_lab_state memory both need correcting to match reality — confirm via `lscpu` + RAM check from inside the OS once it boots normally, don't just take the memtest screen's word for it without a second confirmation.
- **Shardik uptime clock** — reset 2026-07-05 (accidental unplug that morning, not a repeat PSU failure) — superseded by that evening's separate RAM-caused hang. Clock resets again once the RAM stress test/benchmark below confirms stability. Policy: scheduled patch reboots don't count against it, only unplanned freezes/outages do (Chris, 2026-07-05).
- [ ] Shardik: sustained RAM stress test / benchmark (e.g. stress-ng --vm, or a full repeat memtest pass) before resuming the uptime clock — Jordan/Kai
- ✅ **Shardik back up 2026-07-05 late evening, ZFS tank pool confirmed healthy** — `zpool status tank`: ONLINE, all 4 raidz1 members ONLINE, no known data errors. Hard power cycle didn't hurt anything.
- ⚠️ **Odd discovery in dmesg 2026-07-05 — AppArmor profiles for Discord, Brave, 1Password, balena-etcher, buildah, ch-run/ch-checkns loading on boot**, plus an HD-Audio codec with mic/headphone/line-in jacks detected. This is desktop/personal-computer software, not what a dedicated headless Proxmox hypervisor should have. Chris confirmed `hostname && hostname -I` on the actual session — this genuinely is shardik (192.168.1.2), not a mixup with a different host. Chris recalls using those apps on eld (restic-deb's prior identity) rather than shardik, and eld's drives have since been wiped — so the profiles likely came from an OS image/clone/template carried over during shardik's May 2026 ZFS rebuild, not anything currently concerning. **Not urgent — investigate OS install provenance when there's time, not tonight.**
- [ ] Connect a real notification channel to backup-dietpi-deb's Kuma so a drop like today's actually pages someone (Taylor, see Next Week)
- [ ] No production workloads on shardik until the uptime target holds — KASM (111) is there as a stress test only, that's fine
- [ ] Shardik: SMART test on 4x 6TB drives (sda/sdb/sdc/sdd) — results pending
- [ ] Shardik: PBS decision — migrate PBS back to shardik or keep on aslan (Alex + Kai)
- [ ] Proxmox HA sequencing — **decided 2026-07-05:** hold off until (1) shared storage/ZFS replication exists between nodes, and (2) shardik's uptime lock expires. Revisit after both clear.

### Proxmox / Virtualization & VM Placement (Kai)
- [ ] hw_inv.md: add babar's nvme128/nvme512 storage table entries (drives are mounted and working, just not documented yet)
- [ ] Scope cluster storage.cfg dir-storage entries (SDA_store, hdd12tb, hdd3tb, nvme_store) with a `nodes` restriction — confirmed live-misbehaving on babar (aliasing local disk instead of the intended remote path). Alex + Kai.
- [ ] Add pve3 (garuda) to the Proxmox cluster — **stale, no pve3 hardware built yet; garuda is name-reserved only** (shardik + maturin + aslan + blaine + babar, 5 nodes as of 2026-07-08)
- [ ] Configure Tailscale on pve3/garuda; full hardware inventory (dmidecode, photos) — same caveat, no hardware yet
- [ ] Add pve3/garuda to inventory_auto and MkDocs — same caveat, no hardware yet
- [ ] Migrate mediastack-deb → shardik after uptime target holds (currently on aslan)
- [ ] Right-size VM RAM allocations across all nodes
- [ ] Shrink maturin pve-data pool — only cloudinit template remains on local-lvm
- [ ] Investigate maturin VM 112 leftover disk on shardik NVMe (164GB orphan)
- [ ] P2V GOODWIM CentOS drive (Seagate 500GB) before disposing
- [ ] Manyfold — blaine LXC (CT 103) outperforming docker-deb; one more week before calling it permanent. Do NOT delete CT 103.
- [ ] GPU transcoding — revisit mediastack on aslan with GTX 1080 Ti passthrough once RAM allows (Casey + Kai)
- [ ] Rebuild swarm01/02/03 when actually needed (currently destroyed, clean rebuild, no Ceph)
- [ ] Deploy Traefik / Uptime Kuma / Homepage / Zabbix frontend in Swarm mode (longer-horizon)
- [ ] Local AI Assistant next steps: Open WebUI front-end, sysadmin/homelab/casual personalities, Whisper/Piper, MkDocs as RAG knowledge base — Ollama backend itself is done, this is the remaining build-out
- [ ] Local AI Assistant (aslan): GTX 1080 Ti passthrough — still open as a *separate* potential second Ollama/transcoding instance if capacity is ever needed, not required now that babar covers the primary use case

### Storage, Backup & CRU Rotation (Alex)
- [ ] STL_FIGURES — audit all scripts for hardcoded old label references (cru3 was: STL_Non-Fantasy → STL_#CRUNCH → STL_FIGURES)
- [x] STL_ACCESSORIES_TERRAIN (2.7TB) — done, confirmed by Chris 2026-07-24.
- [x] STL_SOURCE_MATERIAL (2.7TB) — done, confirmed by Chris 2026-07-24.
- [ ] FUTURE_USE spare (5.5TB, ST6000VN0001) — partition, format NTFS, label. No content assignment yet.
- [ ] SOURCE_MATERIAL (1.4T) — no drive assigned, on hold
- [ ] STL_T-Z status — backup_drives.md and cru_plexfolder_stats.sh live cache disagree on completion date. Confirm actual state before trusting either.
- [ ] sdc (20TB) — confirmed dedicated TrueNAS emergency spare, shelved, not returning to rotation
- [ ] ⚠️ **Blaine: install 2x 1TB SATA SSDs next time blaine is shut down.** Confirmed free via dmesg (2026-07-05): `ata3` is clean/never-linked — safe bet. `ata2.01` repeatedly shows "failed to resume link" (SStatus 4) — test before trusting it for anything permanent. Confirm physical SATA power + cable are actually run to both before counting on them.
- [ ] Establish offsite drive rotation schedule (Tier 3)
- [ ] Evaluate PBS tape backup to CRU bays (blaine-pve, post-install)
- [ ] Scope a web frontend for the drive database + hardware inventory + wishlist (new, Alex)
- [ ] Research LAGG + CIFS multisync + TrueNAS community edition as a future path (new, Alex)
- [ ] Investigate Plex mount options optimized for high small-file IOPS (new, Alex)

### TrueNAS Hardware & NIC (freenas-bsd 192.168.1.5)
- [ ] **cos SSH key auth — decided 2026-07-03: staying on password.** Root cause diagnosed (StrictModes rejects pubkey because /mnt/TRYAGAIN pool root is group-writable). Exact fix identified (remove group Write on pool root ACE only, recursive OFF) but Chris declined as too risky for a production pool root. cos's home is now at /mnt/TRYAGAIN/admin/cos. Revisit only if Chris wants to reconsider.
- [ ] **X540-T2 — evidence strongly points to genuinely dead card.** Both ports refuse link across cable/port cross-tests; enumerates cleanly on PCIe bus so not a bus/detection issue. Bench test on a separate machine is the final formality. Source/RMA a replacement if confirmed dead.
- [ ] alc0 (onboard NIC) — revived and currently primary, watch for stability over the next 1-2 days before fully trusting it (alc driver has a rougher FreeBSD track record)
- [ ] Jumbo frames on alc0 — backlog, wait for stability proof first
- [ ] Alex + Riley: LAGG on freenas-bsd — on hold pending a confirmed working second NIC
- [ ] **TrueNAS Hardware Rebuild** (temerant donor: Ryzen 5 1600X, 32GB DDR4, GTX 1080 Ti, 500GB SSD) — blocked on HBA cross-flash:
  - [ ] Check temerant-win's 2x 3TB HDDs for important data first ⚠️
  - [ ] Flash IBM M1115 (found) to LSI IT mode — Jordan, do NOT attach TrueNAS drives before flashing
  - [ ] Order 2x SFF-8087 to SATA breakout cables
  - [ ] Install hardware into existing FreeNAS beige tower, install TrueNAS on 500GB SSD, import TRYAGAIN pool
  - [ ] Update mediastack-deb fstab if IP changes
  - [ ] Dedupe TRYAGAIN (fdupes/rdfind, post-rebuild); delete Weltgeist/Alea Iacta Est iocage jails (91GB)

### Network / VLAN / Rack Build (Riley)
- [ ] **Theoretical rack contents updated 2026-07-05:** SG200-50 (1U), MD1200 (2U, fixed spec), Dell R750 + HBA for TrueNAS (2U, fixed spec, replaces the vague "TrueNAS rack-mount chassis" placeholder), pfSense/SG-1100 on a 1U shelf, PDU (0-1U). Roughly ~12U or under without the patch panel — workable for the 12U half rack. UPS placement (rackmount vs. floor-standing) still undetermined. Pi rack + maturin shelf may need to live outside the enclosure if space stays tight.
- [ ] docker-deb static IP or confirmed DHCP reservation ⚠️ (hosts Vaultwarden, Traefik, Portainer)
- [ ] **VPN rationalization — DECIDED 2026-07-05: Tailscale.** Decommission WireGuard (mediastack) and ZeroTier (amontillado).
- [ ] Netgate (192.168.1.6) — confirm model and role, unresponsive to nmap/arp-scan
- [ ] Identify 192.168.1.218 (locally administered MAC, high ephemeral ports only)
- [ ] Clarify Flint2 + Netgate topology — document which handles what
- [ ] Scan guest WiFi subnet — third LG TV likely there
- [ ] Unbound (local DNS resolver) for internal hostname resolution (garm, gan, garuda, etc. instead of raw IPs — Chris flagged 2026-07-06), Authelia (auth layer) — longer-horizon; likely depends on the pfSense/switch VLAN rollout landing first, Riley to scope sequencing
- [ ] **Rack Build + pfSense + VLANs** — hardware in hand (APC half rack, SG-1100, SG200-50 configured, GS116 to retire). Priority raised: GS116 has a confirmed dead port after 7 years and no port visibility to diagnose others.
  - Phase 0: **transport rack home** — ✅ unblocked 2026-07-12, Chris has his car back. Ready whenever Chris can make the trip.
  - Phase 1 (no downtime): place rack, install SG200-50/PDU (no patch panel — dropped 2026-07-05, only real structured run is Flint2→Beryl and it's nowhere near the rack), Flint 2 to AP mode, SG-1100 offline config
  - Phase 2 (cutover, ~1hr outage): WAN → SG-1100, SG-1100 → SG200-50 trunk, migrate cables off GS116, verify + rollback plan
  - Phase 3 (IP migration, full weekend): DHCP reservations by MAC first, then inventory_auto/MkDocs/corosync/fstab/Kuma/Homepage/Zabbix updates
  - Phase 4 (physical, ongoing): shelf for maturin, Pi rack into rack, TrueNAS rack-mount chassis
  - VLAN scheme: 10 Servers / 20 Trusted / 30 IoT / 99 Mgmt

### Security & Monitoring (Taylor)
- [ ] Alert on: drive errors, disk >85%, service down, high temp, RAM pressure
- [ ] docker-deb watchdog — Sam building, alerts Kuma if container stack hasn't restarted in >1 week
- [ ] Uptime Kuma TrueNAS poll interval → 30 seconds
- [ ] Document full Zabbix topology — server on monitor-deb, 11 agents, confirm Grafana pull
- [ ] monitor-deb :9221 — unknown service, identify
- [ ] Configure Zabbix → Telegram alerting
- [ ] Wire smartd_telegram_alert.sh into smartd.conf (-M exec) — script deployed to /opt/scripts/ but not yet wired in; confirm smartd runs as continuous daemon fleet-wide first
- [ ] Deploy Loki for log aggregation
- [ ] Vaultwarden autofill port-matching bug in browser extension
- [ ] Evaluate HashiCorp Vault for Ansible secrets management

### Automation & Scripts (Sam)
- [ ] General alert relay bot (Kuma/Zabbix/SMART → one channel) — approved 2026-07-05
- [ ] CRU label linter script — approved 2026-07-05
- [ ] auto network_inventory.md — arp-scan + masscan + ansible facts combined
- [ ] auto backup date in cru_stats — update_drives_table.py writes Backup column on SMART pass
- [ ] backup_drives_update.sh Gitea-API refactor — implemented, needs a week of clean runs before trusted
- [ ] merge-aware todo_sync.sh — cron on git-ansible preserving Gitea `[x]` state on pull

### Documentation / MkDocs (Morgan)
- [ ] Session runbooks: shardik recovery, red case inventory page, PBS migration log, pve3 DR node page
- [ ] Cluster capacity page — mobo/CPU/RAM/VM placement/upgrade path per node (Kai + Jordan feed data)
- [ ] holy_grail.md as MkDocs front page
- [ ] Pull-before-push check before every SCP (avoid repeat of the completed.md overwrite incident)
- [ ] MkDocs Network section overhaul with Riley
- [ ] Pi Status page with uploaded Pi photos
- [ ] Create Proxmox cluster diagram; document monitoring stack architecture
- [ ] Create backup_policy.md — 3-2-1 approach, rotation schedule, STL archive policy
- [ ] hw_inv.md — document retired/added drives; update hosts.md with aslan + Beryl AP
- [ ] SCP network_inventory.md, vlan_ip_plan.md, site_assets.md to git-ansible docs root
- [ ] Automate doc updates — push from ED session to git-ansible without manual paste
- [ ] completed.md auto-population via checkbox_persist.js
- [ ] ED: create CLAUDE.md for each specialist (domain, personality, rules, escalation paths)

### Media / Plex / Mediastack (Casey)
- [ ] Add Tautulli (Plex analytics), Bazarr (subtitle automation)
- [ ] Tdarr transcoding — needs GPU node first (aslan)
- [ ] Plex Music library mobile fix (Plex Pass confirmed, unresolved)
- [ ] Add Training and Photos libraries to Plex
- [ ] Plex audio normalization — new ask, needs investigation
- [ ] Evaluate Overseerr or Wizarr for request management
- [ ] Dual reverse proxy — Caddy + Traefik both on docker-deb, resolve with Riley
- [ ] STL collection page — evaluate Manyfold first; custom page (like vinyl_collection.html) if it doesn't meet the need (Drew + Sam)
- [ ] Komga / Mylar — comics stack, populate libraries?
- [ ] RomM: complete tactical RPG collections, dedupe DS ROMs, explore LaunchBox archive migration

### IoT / Maker / Pi Fleet / 3D Printing / Physical AV (Drew)
- [ ] Ender 3 V2 yellow PLA — temp tower to dial in profile before structural prints
- [ ] Logitech Z-680 2.1→5.1 issue — static/dropout fixed 2026-07-05 (PC audio driver, not hardware), but the longstanding "stuck at 2.1" issue is separate and still open — rear/center channels not diagnosed
- [ ] Bring argos-pi4-deb and argos-pi4-wifi-deb online; wall-mount argos as HA field station (confirm location w/ Chris); onboard via Ansible
- [ ] PoE switch + PoE HATs — single cable per Pi
- [ ] Full cable management on rack
- [ ] retropi IP and pihole-pi-deb IP — confirm and document in hw_inv.md/hosts.md
- [ ] Check pihole-pi1-deb SD card (was 91% full)
- [ ] Purchase Hologram.io SIM for argos-deb LTE
- [ ] Home Assistant phases 2-4: Zigbee/MQTT/ESPHome/Frigate, automations/Music Assistant/OctoPrint, argos-deb wall kiosk

### Sysadmin / Ansible / Patching (Jordan)
- [ ] Amontillado C: drive audit (7% free); investigate D: drive (11% free)
- [ ] fail2ban rollout via Ansible
- [ ] Git identity on restic-deb
- [ ] BIOS download links for shardik/maturin/aslan/blaine — links gathered, aslan (F52) and blaine (revision-dependent) need action
- [ ] Add microcode + non-free-firmware to homelab_baseline.yml
- [ ] Onboard pbs-deb via onboard2.yml
- [ ] Add Zabbix repo task to homelab_baseline.yml (before agent install)
- [ ] Fix SSH service name for DietPi hosts (ssh vs. dropbear)
- [ ] Fix ansible_facts deprecation warnings before ansible-core 2.24
- [ ] Document mkdocs_dev_material living on restic-deb intentionally
- [ ] Pin ansible_python_interpreter per host in inventory_auto
- [ ] Add chrony LXC skip to sync_time.yml; update check_services.yml; fix pause timing in fail2ban.yml
- [ ] Audit offline hosts from router — inactive vs. decommissioned
- [ ] Confirm batocera-deb (and pi3-deb — host TBD) are actually in `[linux_skip]`, not `[linux]` — 2026-07-06 fleet run shows both "unreachable" in the linux-group recap, meaning the host pattern didn't exclude them like it should have
- [ ] Dedupe Ansible inventory aliases — pi1-deb/pihole-pi1-deb (.120), pi2-deb/blank-dietpi-deb (.121), pi4-deb/backup-dietpi-deb (.126) each resolve to the same physical host, so the baseline playbook runs twice against each. **octopi-deb/octopi-pi4-deb (.122) — DONE 2026-07-21, consolidated to octopi-pi4-deb only.** Chris's call: the remaining three are being kept as intentional aliases, not touched.
- [ ] ⚠️ **tools-deb (192.168.1.125, seen in 2026-07-06 fleet run) vs. ha-net (192.168.1.125 per Pi Fleet docs, RPi 4/Home Assistant OS)** — same IP, different hostname in two sources. Confirm which is current before trusting either doc.

### DC Decommission Salvage
- [ ] DC1 authorization follow-up — Dell N4032F x2, Lambda GPU workstations, Dell Precision 7920
- [ ] DC1 NEEDS MORE INFO checklist (see dc_salvage.md)
- [ ] Dell R730 pickup — get CPU/RAM specs
- [ ] Dell JBOD (4TB SAS) — confirm chassis/bay count
- [ ] DC2 walkthrough; DC3/DC4 status confirmation
- [ ] 12U half rack — retrieve, rack new DC hardware
- [ ] KEEP: Dell PowerVault MD1200 (12-bay SAS shelf), DLI IP Power Switches x2
- [ ] EVALUATE: Dell PowerEdge R750 (CPU/RAM/drives/PCIe), Dell M630 blades (pull specs), Hitachi AMS2100 drives (Alex to decide before disposal), Polycom conference gear (resale)
- [ ] PASS: Synology RS810RP+, Dell M1000e chassis

**Scavenge checklist (every visit):** Priority 1 — 32GB/16GB DDR4 UDIMM, LSI 9211-8i/9207-8i/M1015/PERC H200, Intel PCIe NICs. Priority 2 — R750 contents, NVMe/SSDs, 10GbE NICs. Priority 3 — SAS drives 1TB+, SAS HBAs (flag for Alex).

**RAM Upgrade Targets (as of 2026-07-02):**

| Node | Current | Grail Target | Needed |
|---|---|---|---|
| shardik | 64GB (confirmed maxed, board ceiling is 64GB) | — | ⚠️ **CPU dead as of 2026-07-21 — RAM upgrade path moot until a CPU is sourced.** Table entry below (32GB/128GB target) is stale, corrected 2026-07-21 per live hw_inv.md figures. |
| aslan | ✅ **96GB installed 2026-07-22** (2×32GB + 2×16GB mixed) — Chris had 2×32GB sticks on hand already, no purchase needed | 128GB (4×32GB UDIMM) | 2×32GB more (swap the remaining 2×16GB) for full 128GB — not urgent, 96GB is solid headroom for now |
| maturin | ✅ 64GB (4×16GB) — **live dmidecode-confirmed 2026-07-21: board ceiling is 64GB, already maxed** | 64GB (maxed) | None — this row was stale (previously said 32GB current/needs 4×16GB), corrected. |
| blaine | 32GB DDR3-1333, live dmidecode-confirmed max is 32GB | 32GB | ✅ sufficient, confirmed maxed, no upgrade path exists |

⚠️ DC server RAM is DDR4/DDR5 RDIMM ECC — not compatible with AM4 consumer boards. Only desktop DDR4 UDIMM non-ECC works.

### Hardware Inventory Completion
- [ ] hw_inv.md: add babar's nvme128 (128GB WD PC SN520) and nvme512 (512GB SK hynix PC300) storage table entries
- [ ] hw_inv.md: correct aslan's storage prose — currently says "Samsung 970 EVO Plus 500GB NVMe", actually an Orico ~1.9TB SATA drive (found as `sdc`, holding aslan's OS) — Storage Layout table's 1.71TB figure already matches reality, just the prose description is stale
- [ ] Automate hardware inventory audit vs hw_inv.md — this session found aslan/maturin RAM stale (32GB documented, 64GB actual) and aslan's storage description stale; recurring enough now to script (Ansible fact-gathering + diff against hw_inv.md), not keep catching by hand — Jordan/Sam
- [ ] Photo + dmidecode all 5 waiting systems, pve3, printers (Elegoo Mars 3, Ender 3 V1, Flashforge Dreamer), GPUs, laptops
- [ ] SCP new photos to MkDocs docs/images/hw/
- [ ] **Snipe-IT refresh, not initial import** — corrected 2026-07-24: already has 27 assets logged (plow-rpm, 192.168.1.53), but last activity is 2026-05-25, ~2 months stale. Missing babar entirely (joined 2026-07-08), doesn't reflect shardik's CPU death (2026-07-21) or aslan's RAM upgrade (2026-07-22). Needs a catch-up pass, not a from-scratch import.
- [ ] Add 12TB + suspect 20TB HDD to hw_reserve.md (SMART both); document hw_reserve NICs/RAM found
- [ ] Identify alma-rpm, rocky-rpm, 2404HV-deb roles; identify DIGIDIOT.local AD usage

### Physical / Facilities
- [ ] Tidy desk wires — full shutdown and rewire
- [ ] Sort hardware / locate spares
- [ ] Clean off shelves

---

## Parking Lot (Research Needed — Not Yet Scheduled)

- [ ] Swarm architecture — should monitoring stack move to swarm?
- [ ] Ceph — second attempt, needs dedicated hardware evaluation
- [ ] YouTube channel tech scouting — Chris to provide channel list
- [ ] Komga / Mylar comics population
- [ ] Farson VM — dedicated vuln/pentest VM (Taylor to scope, just a whim for now)

---

## Naming Reference

Active Proxmox nodes (5, as of 2026-07-08): shardik (bear), maturin (turtle), aslan (lion), blaine (Blaine the Mono), **babar (elephant, Jean de Brunhoff — new, 192.168.1.12, most capable node in the cluster)**. garuda remains name-reserved for "next new node" — no pve3 hardware has actually been built yet, despite earlier todo items referencing it as if it existed. Red case: **Garm confirmed 2026-07-06** (dog, Norse mythology, Hel's hellhound). TrueNAS (freenas-bsd) rebuild: **Gan confirmed 2026-07-06** (Dark Tower — new name, outside the original reserve pool). Remaining unused reserve: garuda, navius, rocinante, chuchundra, jasconius, camazotz, owsla.
