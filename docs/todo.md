# Homelab Todo & Roadmap
_Last updated: 2026-08-07 live session with Chris (morning continuation of 08-06). **Restic-deb CRU-drives-zero emergency resolved first thing:** READING, TOSHIBA, and the 6TB ST6000VN0001 all attached/mounted clean. **6TB drive exonerated** — tested in a different bay, linked immediately at full speed; last night's failure was the bay/cable, not the drive (matches the isolation-test conclusion from last night, now confirmed). **Extensive backup_drives.md data-integrity pass, both blaine's local copy and the live git-ansible doc:** confirmed TROVE 24-08 = TheTrove (serial typo Z401Z7A5→Z4D1Z7AS fixed) and TROVE BOOKS = Trove-Books (exact match, no typo) — both are the same physical drives already in CRU rotation under old doc names, not missing backups as previously thought. Renamed the physical NTFS labels on those two drives to match the doc convention ("TROVE BOOKS", "TROVE 24-08") per Chris's explicit call to make physical labels match docs, not the other way around. **Created a new "Archive-Only Drives" section** in both files for drives with no live plex share/source (TROVE 24-08, TROVE BOOKS, TROVE WEBSITE - NOT BOOKS) — hit and fixed a real MkDocs rendering bug along the way (missing blank lines before table/separator lines broke the live page's table rendering, same root cause as the old checkbox-persistence issue). **AUDIOBOOKS 3TB confirmed a mistaken entry** — was incorrectly serial-linked to TROVE WEBSITE - NOT BOOKS (a duplicate, not a real second drive); serial cleared to "TBD" on both files, real physical Audiobooks drive still not found. **Deleted a genuine stale duplicate** ("3T HIT EVERTHING", Z4F95VN8) that was distinct from the real new drive "3T_HIT Everything Else 24-01" (Z4F05VN6, confirmed backed up from plex source `/mnt/plex/24-01 Personal (Everything_Else)/`, ~550GB/147,668 files, live rsync completed clean). **Real Sam-track script bug found and fixed live:** a `vim -c` insert with pipe characters in the text silently dropped the leading `|` on a new table row, corrupting Markdown table parsing and undercounting drives.db from 36→24 — caught via the count mismatch, fixed with `sed`. Per Chris's explicit correction: today's script gaps (UUID_MAP requiring manual updates, NTFS dirty-volume flag not auto-handled, `update_drives_table.py` never adding new rows, the `qm unset` bug) are not "scope creep" — this was always the intended job, just never fully built to spec. **Confirmed no duplicate labels/serials** on either backup_drives.md copy (only benign "TBD" placeholder repeats). **Swapped in 3 more drives for the remaining backup gap list** (MUSIC 10-21-2018, MUSIC+ MUSIC NOT PLEX, PLEX ETC) — two matched by exact serial (MUSIC 10-21-2018, MUSIC+ MUSIC NOT PLEX), but the third's identity is **unresolved**: serial nearly matched "PLEX ETC" (typo fixed: Y5GM755GS→Y5GM7S5GS) but its actual NTFS label is "24-02 AudioBooks" — thematically nothing to do with PLEX ETC, and given today's AUDIOBOOKS 3TB mixup, this may actually be the real missing Audiobooks drive instead. **Not confirmed before session end** — Chris was going to browse via SMB to check contents. Real live NTFS labels for all three: cru1="3TB_HIT_Music", cru2="24-02 AudioBooks", cru3="24-02 Music" — dirty-flag fixed on all three (`ntfsfix`), mounted read-write, but **no backup run yet and no plex source identified for any of the three.** ⚠️ **Also re-confirmed operationally: physically pulling a CRU drive without first running `qm set 100 --delete scsiN` doesn't corrupt data (already unmounted = safe) but does leave a stale VM-config slot reference that breaks the next attach/preflight** — this bit us again this session after Chris pulled 3 drives without detaching first._

_Prior update — 2026-08-06 live session with Chris. **backup_drives.md/drives.db data-integrity pass:** found and fixed three serial-number transcription typos on blaine's `backup_drives.md` that were causing `cru_hotplug.sh identify` to report all three currently-mounted CRU drives as UNKNOWN — READING (Z1Y32KTB→Z1Y32KT8), and two legacy-labeled rows Chris confirmed are the same physical drives as what's actually mounted: "AUDIOBOOKS 3TB" = TROVE WEBSITE - NOT BOOKS (WMAW20629019→WD-WMAWZ0029010) and "D&D GAMING" = RPG_ARCHIVE (Z5011ZMP→Z50113MP). `drives.db` rebuilt, all three now resolve correctly via `identify`. **Real script bug found and fixed in `update_drives_table.py`** (restic-deb): the Backup-date parser split header lines on the first " - ", which breaks for any label containing its own hyphen (e.g. "TROVE WEBSITE - NOT BOOKS" was producing "BOOKS 2026" instead of "Aug 2026") — fixed to `rsplit(' - ', 1)`, confirmed correct on the live doc afterward. Legacy labels ("D&D GAMING", "AUDIOBOOKS 3TB") still not renamed in `backup_drives.md` — open, no decision from Chris yet. **CRU drive swap session, partially completed, ended in a worse state than it needs to be — read carefully before next session:** intended to swap 3 (of a planned 4-drive batch) CRU drives. Confirmed live that `cru_vm_detach_check.sh`'s known `qm unset` bug (already in todo.md, queued for Sam) is still broken — worked around three times with direct `qm set 100 --delete scsiN`. Unmount initially failed "busy" on all three — root cause was active Samba sessions from amontillado (W:/X:/Y: mapped drives) holding cru1/cru2/cru3 open since Aug 3; resolved via `smbcontrol smbd close-share`. TROVE WEBSITE (WD30EZRS) and RPG_ARCHIVE (ST3000DM001) were physically removed and detached from VM 100 — **READING was not actually removed** despite Chris believing all three were swapped (confirmed via by-id serial match, same Z1Y32KT8 throughout the session). Of the intended 3 replacement drives, only 2 ever linked: TOSHIBA DT01ACA300 (Y5GM22NGS) and ST6000VN0001-1SF17Z (Z4D1Z7AS, 6TB) — the third bay never linked at all (`ata2.01`, "failed to resume link", persistent from the start). Reseating attempts then knocked ST6000VN0001 offline too; `dmesg` showed both `ata2` ports degrading (6.0→3.0→1.5Gbps) and failing IDENTIFY, initially pointing to a channel/cable-level fault — but isolation testing (old TROVE WD30EZRS, then a separate ST3000VN0001-1SF176/Z4F05VN6, both linked cleanly in the same bay afterward) narrowed it back to **ST6000VN0001 itself as the likely failed unit**, not the bay/cable. Blaine was rebooted mid-session (picked up a pending kernel update, 7.0.14-2→7.0.14-8-pve) attempting to clear the fault — did not bring the drive back. **Chris wants to test the 6TB drive in a different machine/port tomorrow before writing it off as failed.** ⚠️ **Session ended with restic-deb (VM 100) holding zero CRU drives.** READING and TOSHIBA are both physically present and detected on blaine but neither is attached to VM 100 (scsi1/2/3 all cleared, only scsi0 boot disk remains) or mounted in restic-deb. **First thing next session: re-attach and mount READING + TOSHIBA before anything else.** Also unconfirmed: current physical storage location of the old TROVE WEBSITE and RPG_ARCHIVE drives (removed tonight, not verified stored), and whether the isolation-test ST3000VN0001-1SF176 drive is still sitting in a bay or was removed._

_Prior update — 2026-08-05 live session with Chris. **EMULATION consolidation fully closed out.** `[emu]` console-folder library merged into `ROMs` (source of truth) using a custom game-unit-level matching script, then `[emu]` deleted once drained (Chris relocated `_Translations`/`_1G1R` out first). Two dedup passes on `Translations` (16.5GB reclaimed) plus one full-EMULATION-wide strict scan across `1G1R`/`ROMs`/`Sorted_Roms_0726`/`Translations` (4,411 files, 65.8GB reclaimed) — total EMULATION size now 3.6TB, down from 4.7TB at the start of this effort. Same dedup method run against `READING_0726` (753 files, 22.6GB reclaimed). **Backup findings:** diffed live `RPG_ARCHIVE` (plex) against its cru3 backup — found `DaArchive 0420 A-Z` (436GB) exists only on cru3, with plex showing just a 2.1MB `Da Docs` placeholder in its place; cause unknown (stale pre-consolidation backup vs. real data loss on the live share) — needs Alex to determine before anyone treats either copy as authoritative. Also found `Solo` (9.5GB, plex) was never backed up to cru3, and two misfiled non-RPG files sit on cru3 (SBLII_Ebrochure, super_bowl_2018_bid_faq — harmless clutter, not urgent). **READING backup to cru1 kicked off** (correctly targeted after an initial mis-run to cru3 was caught and left in place per the no-delete-from-CRU rule — cru3 now also holds a full copy of READING_0726, which is redundant but harmless) — dry run was still working through ~160k small Kindle-collection files at session end, live sync not yet confirmed complete. **Hardware:** Chris located existing DDR3L SO-DIMM stock in hw_reserve.md photos — confirmed a Samsung 8GB PC3L-12800 + one 4GB PC3L stick (12GB combo) covers the OptiPlex 3040 Micro's RAM upgrade from its current 4GB with no purchase needed._

_Prior update — 2026-08-02 Sunday weekly team meeting (scheduled, autonomous run — Chris not present live). Full 10-person status round held, two-hour format. Two wins highlighted: weekly_patch.yml's Sunday 3am cron has now run clean two weeks straight (first real confirmation the 07-26 vault-password fix holds); Scrutiny's fleet-wide SMART sweep came back with no real drive-health problems anywhere. New/escalated items: Jordan flagged the 07-27 Homepage `cat` incident (live Proxmox/Grafana/API credentials printed to terminal scrollback, still unrotated) as needing a real credential-rotation pass, not just awareness — Taylor picked this up as workstream one for the still-unscoped full security sweep. Riley restated that Rack Build Phase 1 has now had zero physical movement across three consecutive weekly meetings (07-12, 07-19, 07-26, and now this one) — flagged as the most stalled "ready to ship" item in the backlog. Sam's proposal count is unchanged at six, all still awaiting Chris's triage; the shardik MCE watcher proposal specifically needs a kill/keep call now that shardik is deprioritized. Morgan re-flagged the CLAUDE.md priorities rewrite (shardik + TRYAGAIN lines both confirmed stale) as ready pending only Chris's sign-off. No completions marked [x] on Chris's behalf since he wasn't present to confirm; new action items below need his review at the next live session._

_Prior update — 2026-07-31 live session with Chris. **Backup drive audit:** identified 9 drives with no 2026 backup at all — D&D GAMING, READING, TROVE 24-08, TROVE BOOKS, TROVE NOT BOOKS, MUSIC 10-21-2018, MUSIC+ MUSIC NOT PLEX, PLEX ETC, 3T HIT EVERTHING (all Books/Music/Other category drives, last touched Feb 2024–Feb 2025 per backup_drives.md). **CRU bay troubleshooting (restic-deb/blaine):** cru1 wouldn't detect a physically-reseated drive even after a host-level SCSI bus rescan on blaine; root-caused via `dmesg` to a stale QEMU passthrough handle (drive re-enumerated sdc→sde on the host after reseat, VM 100's `scsi1` held a reference to the old node) — fixed live with `qm set 100 --delete scsi1` then re-attach to the same by-id path, confirmed working via `lsblk`/`partprobe`. **cru1 = READING** (audiobook archive, last backup Feb 2025 — stale). **cru2 = "TROVE WEBSITE - NOT BOOKS"** — Chris confirmed this is NOT part of the main plex share and NOT the same drive as backup_drives.md's existing "TROVE NOT BOOKS" entry; not currently logged in backup_drives.md, needs Alex to formally add with correct source/backup method. **cru3 = RPG_ARCHIVE** — diffed against live `/mnt/plex/RPG`, confirmed current (archive has one extra folder, "DaArchive 0420 A-Z", no longer on the live share; otherwise identical). **Renamed for consistency:** live plex share folder `/mnt/plex/RPG` → `/mnt/plex/RPG_ARCHIVE` (on TrueNAS via CIFS mount), and cru3's `RPG` subfolder → `RPG_ARCHIVE` to match; two stray root-level files on cru3 (SBLII_Ebrochure_9_5_17.pdf, super_bowl_2018_bid_faq pdf) moved into RPG_ARCHIVE by Chris. ⚠️ **Chris deleted `System Volume Information` from cru3's root directly** — against the project's absolute no-delete-from-CRU rule; flagged once before it happened, no actual data loss (NTFS system metadata only, not archive content). **Manyfold's actual library path confirmed as `/mnt/plex/_STL/manyfold`** (not the sibling `STL` folder) — resolves the ambiguity between the two STL-named directories. **Shardik CPU upgrade path researched and logged to hw_inv.md:** board (ASRock AB350M Pro4) officially supports up to Ryzen 9 5950X (16c/32t) after a BIOS update, but the update needs a working supported CPU installed first (no CPU-less flashback) — either 1600X candidate (urnst-deb/temerant-win) works for that step. Chris found a used 5950X at $293 on eBay (fair market price) but it's listed "for parts only" — not guaranteed functional, not yet purchased._

_Prior update — 2026-07-31 Friday one-on-one (scheduled, autonomous run — Chris not present live). Hour 1 Claude School: "using the project folder and CLAUDE.md for persistent context" taught, using this project's own CLAUDE.md as the live example. Follow-up on 2026-07-24's assignment (classify one recurring manual check as scheduled-task/Sam-automation/keep-live): **no submission logged — carrying forward, not chasing.** New assignment: next time an instruction would otherwise be repeated to the ED live, add it to CLAUDE.md as a standing rule instead — one example, due 2026-08-07. Real finding surfaced this session: CLAUDE.md's own stated priorities ("shardik stability, PSU suspected, 1-month uptime target" and "TRYAGAIN pool resilience, ada4 replacement needed") are both stale — shardik's CPU is confirmed dead and deprioritized by Chris (2026-07-21/23), and ada4 was already replaced with resilver complete per project memory (2026-06). Flagged for Chris to confirm and for CLAUDE.md's priorities section to be rewritten. Hour 2: Sunday meeting prep brief generated — see session output, top items are Rack Build Phase 1 (zero movement across three weekly meetings), Sam's 6 stacked pending proposals, and the Prometheus retention decision. No infra changes made, no completions confirmed by Chris (not present)._

_Prior update — 2026-07-30 live session with Chris, continuation of the overnight 2026-07-27 session (same thread, spanned several days of intermittent activity). Closed out: "apache-deb" mystery host (dead end, not a real host, closed as non-issue); Homepage "Pis" section icons (confirmed all rendering correctly). Fixed: Ollama's Homepage widget ("Missing Widget Type: ollama" — gethomepage has no native Ollama widget, switched to the documented `customapi` workaround pointed at Ollama's `/api/tags`); Ollama LXC's IP was mis-ranged (`.169`, peripherals/IoT range) and got moved to `.20` (20-49, correct VM/container range) via a proper DHCP reservation, same pattern as the 2026-07-21 rocky-rpm fix. **Homepage instances brought to genuine full parity per Chris's explicit ask** — see the dedicated note below on why this took three attempts and what the real architectural difference between the two instances is._

_Prior update — 2026-07-27 live session with Chris (overnight into early morning). Headline: **plow-rpm fully migrated off RHEL/Rocky-hybrid to a clean Rocky Linux 9 VM, end to end** — Snipe-IT DB+config+storage backed up, new VM (173, babar) provisioned, restored, verified matching the old instance exactly (27 assets/83 components/2 people), cut over to the same IP (192.168.1.53), old VM destroyed, onboarded into hosts.md/inventory_auto/Zabbix/both Homepage instances. Real bugs found along the way: new VM wouldn't boot at all until `--cpu host` was set explicitly (Proxmox's default `kvm64` CPU model panics Rocky 9's init — will hit any future EL9 VM build); `onboard2.yml` assumes a `sudo` group that doesn't exist on RHEL-family hosts (needs `wheel` instead) and doesn't handle Zabbix's RHEL9 repo (package isn't in default dnf repos) — both need Sam/Jordan to fix properly. A hostname mix-up during onboarding briefly created a real collision between this host and the pre-existing, unrelated `rocky-rpm` (192.168.1.51) in `/etc/hosts` and `hosts.md` — caught and fixed same session, no lasting damage. Also: `cat`-ing monitor-deb's Homepage config to check for a missing entry incidentally printed several live credentials (Proxmox root password, Grafana admin password, and API keys for Portainer/Sonarr/Radarr/Prowlarr/Lidarr/Mylar/Plex/Jellyfin/Komga/Audiobookshelf/RomM, qBittorrent password) into this session — Chris hasn't decided yet whether any need rotating._

_Prior update — 2026-07-26 live session with Chris (morning, ended here — heading up on the roof). Session covered: 9 of 10 quick wins closed; babar's Ansible-inventory gap root-caused and permanently fixed (was being silently wiped every hour by `generate_inventory.py`, not a one-off miss); SMART-to-Telegram alerting built and live on all 5 physical hosts; weekly patch/reboot automation found completely broken (missing vault password, likely for months) and fixed, real run completed clean; monitor-deb disk-full crisis resolved (Prometheus retention 30d→15d per Chris's actual need, oldest 6 blocks manually cleared, 90%/2.9G free now); `check_disk_space.yml` wired to Telegram for real CRITICAL alerts (was silently report-only); new offboard/decommission script ("debark") fully spec'd, not built, queued for Sam. Three follow-up issues surfaced and logged, not yet actioned: plow-rpm package conflict, truenas-bsd SSH host key change, "apache-deb" unrecognized host in a recap. Sync to git-ansible still needed as of this note._

_Prior update — 2026-07-26 Sunday weekly team meeting (scheduled, autonomous run — Chris not present live). Full 10-person status round held, two-hour format. Headline: backup rotation's completeness (confirmed 2026-07-24) and the weekly_patch.yml vault fix (found and fixed earlier today) were the two wins of the week — Jordan flagged the patch fix as the first real fix in what was likely months of silent failures. Top open item: nobody has yet confirmed whether last night's/this morning's 3am Sunday cron actually ran clean under the new fix — first real test of the repair, unconfirmed as of the 9am meeting. Sam proposed two new projects (todo.md archiver, Scrutiny→Telegram config script) on top of the four still-pending proposals from prior weeks — one of those four (shardik MCE watcher) flagged as likely moot now that shardik is deprioritized, needs Chris's call on whether to formally kill it. No completions marked [x] on Chris's behalf since he wasn't present to confirm; new action items below need his review at the next live session._

_Prior update — 2026-07-26 live session with Chris. Scrutiny host-id labeling added across all 5 spoke collectors (maturin/aslan/blaine/babar/freenas-bsd) — dashboard now groups drives by hostname instead of bare device paths, closing out the 2026-07-24 Scrutiny build. Docker & LXC recommendation lists (10 each, not currently running) curated and logged — see new section below. Snipe-IT correctly identified as already deployed, swapped for Stirling-PDF in the LXC list. Starter-batch pick for next deploys: **NetBox and Immich** (Scrutiny already done). **Scrutiny extended to a 6th spoke: amontillado** (native Windows collector, smartmontools via winget, `commands.metrics_smartctl_bin` override needed since the installer doesn't add smartctl to PATH, Task Scheduler every 30 min via `Register-ScheduledTask` — note `[TimeSpan]::MaxValue` breaks the task XML schema, use a long finite duration like 3650 days instead). One SMART flag investigated on amontillado's /dev/sdb (Seagate 3TB, 35,508 power-on hours) — overall health PASSED, all real failure indicators (reallocated sectors, pending sectors, UDMA CRC errors) at 0; the bit-5 trigger was a one-time historical temperature-attribute dip, not a current issue. False alarm, same pattern as the fleet build's earlier flags._

_Prior update — 2026-07-24 Friday one-on-one (scheduled, autonomous run — Chris not present live). Hour 1 Claude School: "scheduled tasks vs. asking Claude directly" taught, using this session itself as the live example. Follow-up on 2026-07-17's assignment (demand a proof-command before marking a specialist's "done" as [x]): partially applied — today's earlier live session corroborated Movies/TV backups against real backup_drives.md data, but STL closure was taken on Chris's word alone, no command cited. New assignment: pick one recurring manual check and classify it (scheduled task vs. Sam automation vs. keep live) — due next Friday. Hour 2: Sunday prep brief generated — see session output, top items are Rack Build Phase 1, Sam's 4 stalled proposals, and the Prometheus retention decision. No infra changes made, no completions confirmed by Chris (not present)._

_Prior update — 2026-07-24 live session with Chris. **Shardik explicitly deprioritized by Chris** — "not an issue till I say it is," babar is the better node and covers the primary use case; stop surfacing shardik as a top item. **Backup rotation confirmed done**: Chris confirmed movies, TV, and both outstanding STL rsyncs (STL_ACCESSORIES_TERRAIN, STL_SOURCE_MATERIAL) are complete — backup_drives.md corroborates Movies/TV with real populated stats and clean SMART; STL closure taken on Chris's word. Chris flagged renewed interest in physically setting up the rack + switch (Rack Build Phase 1) as the next priority. Two new curated lists added this session: Top 10 Big Projects and Top 10 Quick Wins (under 30 min each) — see new sections below._

_Prior update — 2026-07-21 live session with Chris. Major finding: shardik's CPU is confirmed dead — this closes out the weeks-long MCE investigation thread (bank 0 2026-07-06, bank 5 2026-07-08/09, stress-ng soak test that was never pulled) with a real answer. No spare AM4 CPU in reserve; sourcing decision (buy vs. cannibalize urnst-deb or temerant-win, both Ryzen 5 1600X) still pending Chris. Large network/DNS/IP hygiene pass also done this session — see Resolved below. monitor-deb hit 100% disk full mid-session (real, not cosmetic — caused an ansible task to fail with "No space left on device"); freed ~6G (docker image prune + apt clean), now at 88%/3.6G free, but this is not a permanent fix — Prometheus (9G, 30d retention) will keep growing back toward the ceiling, retention/disk-size decision still open._

_Prior update — 2026-07-19 Sunday weekly team meeting (scheduled, autonomous run — Chris not present live. Full 10-person status round held, two-hour format. Top blocker restated and escalated: the shardik LXC 150 stress-ng soak test result (7-hr run finished 2026-07-08/09) still hasn't been pulled — now 10+ days stale with no tmux capture logged, top item blocking further MCE diagnosis. Sam proposed two new projects this session (hw_inv.md auto-diff-audit, shardik MCE watcher) — pending Chris approval alongside the two proposals still open from 2026-07-12. No completions marked [x] on Chris's behalf since he wasn't present to confirm; new action items below need his review/prioritization at the next live session.)_

_Prior update — 2026-07-17 Friday one-on-one (scheduled, autonomous run — Chris not present live. Hour 1 Claude School: "reading Claude's output critically" lesson delivered, tied to the 2026-07-16 babar Ansible-onboarding correction and the aslan/maturin stale-RAM-doc pattern. Assignment: next time a specialist reports a task "done," ask for the one command that proves it before marking [x]. Note: no submission logged for the 2026-07-10 "loaded prompt" assignment — carrying forward, not chasing. Hour 2: Sunday meeting prep brief generated — see session output. No infra changes made this session, no new completions confirmed by Chris.)_

_Prior update — 2026-07-12 Sunday weekly team meeting (scheduled, autonomous run — Chris not present live. Full 10-person status round held. No completions marked [x] on Chris's behalf since he wasn't present to confirm; new action items below need his review/prioritization at the next live session. See action items under each specialist's section and the new items logged this pass.)_

_Prior update — 2026-07-10 Friday one-on-one (Hour 1 Claude School: better-prompts lesson delivered, assignment given — write a "loaded" prompt for the storage.cfg node-scoping risk, due next Friday. Hour 2: Sunday meeting prep brief generated from current backlog — see weekly_meeting notes / session output. No infra changes made this session, no new completions confirmed by Chris.)_

_Prior update — 2026-07-09 end of session (Babar joined the Proxmox cluster as 5th node (192.168.1.12, Dell Pro Tower Plus, Core Ultra 7 265, 128GB DDR5, RTX 5060) — full onboarding to Ansible/Zabbix/node_exporter/Uptime Kuma complete. Qdevice permanently removed — 5 physical nodes is odd-count and self-resolving, Proxmox itself refuses a qdevice now. kasm-2404-deb (VM 111) live-migrated off shardik to babar (hw_inv.md had its location wrong — was on shardik, not aslan as documented). NVIDIA driver installed on babar (610.43.03, open-kernel-module, DKMS, Secure Boot MOK-signed) after a near-miss where the generic Debian nvidia-driver package nearly removed proxmox-ve entirely (blocked by Proxmox's own pve-apt-hook safety mechanism). Ollama deployed in a privileged LXC (102) on babar with full RTX 5060 GPU passthrough, confirmed working with live model inference. Shardik's CPU MCE fault further decoded (bank 5/execution unit, uncorrected/context-corrupting) — RAM ruled out via successful aslan/maturin DIMM audits (both corrected to 64GB in hw_inv.md, were stale at 32GB); a 7-hour isolated stress-ng soak test was kicked off in a fresh LXC on shardik to try to reproduce the fault, result not yet checked. New known gaps: hw_inv.md still needs babar's final NVMe storage config and a correction to aslan's stale storage description; cluster storage.cfg has several dir-storage entries (SDA_store/hdd12tb/hdd3tb/nvme_store) that are unscoped to specific nodes and confirmed live-misbehaving on babar (aliasing local root disk instead of erroring) — needs a "nodes" restriction added before anyone trusts those names fleet-wide.)_

---

## Action Items — Live Session 2026-08-07 (new this session)

- [x] **"24-02 AudioBooks" (cru2, Toshiba DT01ACA300, serial Y5GM7S5GS) confirmed as the real, long-missing Audiobooks drive** — Chris checked contents via SMB and confirmed. AUDIOBOOKS 3TB's doc row corrected: model fixed (was wrongly "WD Caviar Green WD30EZRS", now "Toshiba DT01ACA300"), serial set to Y5GM7S5GS, on both blaine's local file and the live git-ansible doc.
- [x] **"PLEX ETC" deleted entirely from both files — confirmed it was never a real distinct drive**, just confusion with the Audiobooks drive above (same serial-typo coincidence that started this whole thread). Both files now at 36 drives, consistent.
- [ ] Find plex source paths (if any) for the 3 newly mounted drives — cru1="3TB_HIT_Music", cru2="24-02 AudioBooks" (now correctly = AUDIOBOOKS 3TB), cru3="24-02 Music" — none identified yet, no backup run.
- [ ] **Queued: Audiobooks dedup pass** (same hash-verified methodology as the EMULATION consolidation). Fast filename-only scan tonight found 9,570 filename collisions out of 154,108 total files (~6%) across the three live plex folders (`24-01 AudioBooks` 2.3T, `AudioBooks-Music` 25G, `AudioBooksPlex` 188G) — real signal, but filename matches alone don't confirm true duplicates. Needs a proper hash pass to confirm before any files are touched.
- [x] 6TB drive (ST6000VN0001) exonerated — confirmed working in a different bay, last night's failure was the bay/cable not the drive.
- [x] Restic-deb zero-CRU-drives emergency resolved — READING, TOSHIBA, 6TB all attached/mounted first thing this session.
- [x] TROVE 24-08 (=TheTrove) and TROVE BOOKS (=Trove-Books) confirmed as already-in-rotation drives with stale/typo'd doc entries, not missing backups. Serial typo fixed (TROVE 24-08), physical NTFS labels renamed to match doc convention.
- [x] New "Archive-Only Drives" section created in both backup_drives.md copies (blaine local + live git-ansible doc) for TROVE 24-08, TROVE BOOKS, TROVE WEBSITE - NOT BOOKS — drives confirmed to have no live plex share/source.
- [x] MkDocs table-rendering bug found and fixed on the new section (missing blank lines before table/separator broke rendering — same root cause pattern as the historical checkbox-persistence issue).
- [x] AUDIOBOOKS 3TB confirmed a mistaken duplicate entry (wrongly serial-linked to TROVE WEBSITE - NOT BOOKS) — serial cleared to "TBD" on both files. Real Audiobooks drive still not found (see above, may be "24-02 AudioBooks").
- [x] Stale duplicate "3T HIT EVERTHING" (Z4F95VN8) deleted from both files — distinct from the real new drive "3T_HIT Everything Else 24-01" (Z4F05VN6), which is now correctly onboarded with a real backup completed (~550GB from `/mnt/plex/24-01 Personal (Everything_Else)/`).
- [x] Real script bug found/fixed: `vim -c` insert with pipe characters in the text corrupted a Markdown table row (dropped leading `|`), undercounted drives.db 36→24 — fixed with `sed`, verified back to correct count.
- [x] MUSIC 10-21-2018 and MUSIC+ MUSIC NOT PLEX drives inserted and identified by exact serial match — not yet backed up, no plex source confirmed yet (bundled with the AudioBooks identity question above).
- [ ] Sam: proper spec needed for the recurring script gaps hit again this session — UUID_MAP manual updates on every new drive, NTFS dirty-volume flag requiring manual `ntfsfix` every time, `update_drives_table.py` never auto-adding new rows (only updates existing ones by exact label match), and the still-unfixed `qm unset` bug in `cru_vm_detach_check.sh`/`cru_hotplug.sh`. Per Chris: this was always the intended scope, not scope creep — build it to the real job.
- [ ] Operational note for future CRU sessions: always run `qm set 100 --delete scsiN` before physically removing a drive, even though data is already safe post-unmount — skipping it leaves a stale VM-config slot that breaks the next preflight/attach.

## Action Items — Live Session 2026-08-06 (new this session)

- [ ] ⚠️ **Urgent — attach + mount READING and TOSHIBA on restic-deb.** Session ended with zero CRU drives active on VM 100 (scsi1/2/3 all cleared, nothing attached). Do this first next session: `cru_hotplug.sh preflight`/`attach 100 <by-id path> scsiN --apply` for both drives on blaine, then `cru_mount_vm.sh mount` on restic-deb. May need `UUID_MAP` updated in `cru_mount_vm.sh` since these are new bay assignments.
- [ ] ⚠️ **Test ST6000VN0001-1SF17Z (Z4D1Z7AS, 6TB) in a different machine/port** to confirm it's actually failed before writing it off. Isolation testing tonight (two other known-good drives both linked cleanly in the same bay after reseating) points to the drive itself, not the bay/cable.
- [ ] Confirm current physical storage location of the old TROVE WEBSITE (WDC WD30EZRS, WD-WMAWZ0029010) and RPG_ARCHIVE (ST3000DM001, Z50113MP) drives — both removed from blaine tonight, not yet confirmed put away.
- [ ] Confirm whether ST3000VN0001-1SF176 (Z4F05VN6) — used tonight for isolation testing — is still physically inserted in a bay or was removed.
- [x] `backup_drives.md` serial typos fixed (READING, TROVE WEBSITE/"AUDIOBOOKS 3TB", RPG_ARCHIVE/"D&D GAMING") — `drives.db` rebuilt, `cru_hotplug.sh identify` now resolves all three correctly.
- [x] `update_drives_table.py` Backup-date parsing bug fixed (`split`→`rsplit` on the header line) — was producing garbled dates ("BOOKS 2026") for any label containing an internal hyphen. Confirmed correct on the live doc for TROVE WEBSITE (now shows "Aug 2026").
- [ ] Open: rename legacy labels in `backup_drives.md` ("D&D GAMING"→RPG_ARCHIVE, "AUDIOBOOKS 3TB"→TROVE WEBSITE - NOT BOOKS) to match current use — Chris hasn't confirmed yet, not acted on.
- [ ] Sam: `qm unset` bug in `cru_vm_detach_check.sh`/`cru_hotplug.sh` confirmed still broken tonight (worked around manually three times with `qm set <vmid> --delete <slot>`). Carried forward from 08-02 meeting — still needs the real fix, not urgent since the manual workaround is known-good.

## Action Items — Live Session 2026-08-05 (new this session)

- [ ] ⚠️ **Alex: investigate the `DaArchive 0420 A-Z` discrepancy.** 436GB exists only on cru3's RPG_ARCHIVE backup; the live plex copy has just a 2.1MB `Da Docs` folder where it should be. Determine whether this is a stale pre-rename backup (fine) or real data loss on the live share (not fine) before treating either copy as authoritative.
- [x] `Solo` (plex RPG_ARCHIVE) backed up to cru3 — confirmed 2026-08-05, rsync completed clean, 9.8G landed on cru3 matching plex.
- [ ] Alex: two misfiled non-RPG files on cru3 (SBLII_Ebrochure_9_5_17.pdf, super_bowl_2018_bid_faq.pdf) — harmless but worth relocating off the RPG_ARCHIVE backup at some point.
- [x] READING → cru1 backup sync confirmed complete — `to-chk=0/295462`, full 1.7TB tree landed. Note: an earlier mis-run partially copied READING_0726 to **cru3** by mistake before being redirected to cru1 — left in place per the no-delete-from-CRU rule, harmless redundant copy, no cleanup needed.
- [x] EMULATION library consolidated: `[emu]` merged into `ROMs` (source of truth) and deleted; `_Translations`/`_1G1R` relocated to top-level siblings first. Total EMULATION size 4.7TB → 3.6TB.
- [x] Translations/READING duplicate sweeps: two Translations passes (16.5GB), one full-EMULATION-wide pass (65.8GB/4,411 files), one READING pass (22.6GB/753 files). All hash-verified byte-identical only — no variant/patch-revision files touched.
- [x] OptiPlex 3040 Micro RAM upgrade sourced from existing reserve — no purchase needed. Combo: Samsung 8GB PC3L-12800 + one 4GB PC3L-12800 stick = 12GB (up from current 4GB). Physical install still pending Chris.

## Action Items — Weekly Team Meeting 2026-08-02 (new this session)

- [ ] ⚠️ **Credential rotation needed — new urgency.** The 07-27 Homepage `cat` incident printed live Proxmox root, Grafana admin, and API keys (Portainer/Sonarr/Radarr/Prowlarr/Lidarr/Mylar/Plex/Jellyfin/Komga/Audiobookshelf/RomM/qBittorrent) into terminal scrollback — none have been rotated since. Jordan flagged this as workstream one for the still-unscoped full security sweep (queued 07-27). Taylor to draft the sweep scope this week: credential rotation, SSH key hygiene, sudoers/wheel audit, exposed-services review.
- [ ] ⚠️ **Rack Build Phase 1 — zero physical movement across three consecutive weekly meetings (07-12, 07-19, 07-26, 08-02).** Switch config and VLAN plan are fully ready (SG-1100 + Dell switch, 4 VLANs approved 06-28); entirely blocked on Chris physically placing the rack. Flagged as the most stalled "ready to ship" item in the backlog.
- [ ] **Sam's 6 pending proposals still awaiting Chris's triage, no movement:** storage.cfg node-scoping linter, MkDocs pre-push diff-check, hw_inv.md auto-diff-audit, shardik MCE watcher, todo.md auto-archiver, Scrutiny→Telegram config script. Shardik MCE watcher specifically needs a kill/keep call now that shardik is deprioritized.
- [ ] Sam to fix the two known `qm unset` bugs in `cru_vm_detach_check.sh` and `cru_hotplug.sh` (should be `qm set <vmid> --delete <slot>`) — small, doesn't need a proposal cycle.
- [ ] Jordan: fix `onboard2.yml`'s `sudo`/`wheel` group assumption and missing Zabbix RHEL9 repo task — will hit the next RPM-family host onboarding.
- [ ] Morgan: CLAUDE.md priorities rewrite (shardik + TRYAGAIN lines both confirmed stale) and hw_inv.md's stale shardik line — both ready, only need Chris's sign-off to apply.
- [x] Alex: cru2 ("TROVE WEBSITE - NOT BOOKS" / "AUDIOBOOKS 3TB") and cru3 (RPG_ARCHIVE / "D&D GAMING") confirmed logged in backup_drives.md as of 2026-08-06 — serials were just typo'd (now fixed, see 08-06 session above), not actually missing. Remaining open piece: legacy labels not yet renamed to current names (Chris hasn't confirmed). Note: both physical drives were removed from blaine during the 08-06 swap session — no longer in cru2/cru3 bays as of session end.
- [ ] Taylor: Prometheus retention/disk decision for monitor-deb still pending Chris — no longer just a stopgap concern, already caused one real Ansible failure.
- [ ] Riley: Hyper-V VLAN placement for amontillado still needs Chris to confirm what those VMs actually do before finalizing Trusted vs. Servers.
- [ ] Casey: pitching Tautulli (Plex analytics) and Overseerr (request management) as the next two Docker deploys — not yet approved.

## Action Items — Live Session 2026-07-31

- [ ] Alex to formally log cru2 ("TROVE WEBSITE - NOT BOOKS") and cru3 (RPG_ARCHIVE) in backup_drives.md with correct source/backup method — neither is currently in the inventory. cru2 is confirmed not part of the main plex share.
- [ ] READING drive (cru1) backup sync in progress as of 2026-08-05 — see new session section above for status, not yet confirmed complete.
- [ ] 8 other drives flagged with zero 2026 backups (D&D GAMING, TROVE 24-08, TROVE BOOKS, TROVE NOT BOOKS, MUSIC 10-21-2018, MUSIC+ MUSIC NOT PLEX, PLEX ETC, 3T HIT EVERTHING) — no action taken yet, just surfaced.
- [ ] Shardik CPU purchase decision pending — $293 5950X on eBay is "for parts only" (not guaranteed working); Chris to decide whether to pursue a tested-working listing instead, and whether the BIOS-flash detour (temp-install a 1600X first) is worth it given shardik's deprioritized status.

## Action Items — Friday One-on-One 2026-07-31 (Claude School, scheduled/autonomous)

- [ ] **Claude School assignment:** next time you'd repeat an instruction to the ED live instead of it already being a standing rule, add it to CLAUDE.md instead — bring one real example next Friday (2026-08-07).
- [ ] Carried forward, not chased: 2026-07-24's assignment (pick one recurring manual check, classify as scheduled task / Sam automation / keep live) — no submission logged.
- [ ] ⚠️ **CLAUDE.md priorities section is stale — needs Chris's sign-off to rewrite.** It still lists "shardik stability (PSU suspected, 1-month uptime target)" and "TRYAGAIN pool resilience (ada4 replacement needed)" as active priorities. Per project memory: shardik's CPU is confirmed dead (2026-07-21) and the node is explicitly deprioritized by Chris ("not an issue till I say it is," 2026-07-23); ada4 was already replaced (WD HC560) with resilver complete as of 2026-06, pool HEALTHY. Both lines should be retired or rewritten next time CLAUDE.md is touched.

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

## Sunday Projects (queued for a future Sunday team meeting, not scheduled yet)

- [ ] **Full security sweep** — added 2026-07-27 per Chris ("some time soon"), no target date set yet. Scope not defined yet; candidates to consider when this gets picked up: credential rotation (Homepage config exposed several live passwords/API keys this session — Proxmox root, Grafana admin, Portainer/Sonarr/Radarr/Prowlarr/Lidarr/Mylar/Plex/Jellyfin/Komga/Audiobookshelf/RomM/qBittorrent), SSH key hygiene across the fleet, sudoers/wheel config audit, exposed services review, Vaultwarden/Caddy TLS review. Taylor's domain — needs proper scoping before it's actionable.

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
10. ~~Wire SMART alerts into smartd.conf~~ — **✅ DONE 2026-07-26 (morning follow-up).** No smartd.conf edits needed in the end — Debian's default smartd.conf already runs `-M exec /usr/share/smartmontools/smartd-runner`, which auto-executes anything dropped in `/etc/smartmontools/run.d/`. Deployed to maturin/aslan/blaine/babar: `smartd_telegram_alert.sh`, its dependency `notify_telegram.py`, and `/etc/oerthbot/config.json` (0600, root-owned, token never echoed to any terminal — pushed via Ansible copy module directly), then symlinked the alert script into `/etc/smartmontools/run.d/99-smartd-telegram-alert` (no dots in the run-parts filename) on all four. **Verified live end-to-end on maturin** using smartd's built-in `-M test` mode — real Telegram message landed in OerthChannel ("⚠️ SMART Alert: EmailTest on /dev/nvme0..."), confirmed via screenshot, then test flag reverted and smartd restarted clean (fresh timestamp confirmed, "Next check of 2 devices" resumed normal operation). Same wiring is live on aslan/blaine/babar (identical mechanism, not individually re-tested since the pipeline itself is now proven).

## plow-rpm — RHEL to Rocky Migration — ✅ DONE 2026-07-27

**Decision:** Chris is done with RHEL on plow-rpm ("sick of rhel tbh") — replacing with **Rocky Linux**, matching the existing rocky-rpm host. Triggered by chasing today's dnf package conflict (`containers-common` vs `redhat-release` GPG key file).

**Real finding that changes the plan:** plow-rpm's `dnf repolist` shows `appstream`/`baseos` already pointed at **Rocky Linux 9** mirrors, not real RHEL — the box identifies as RHEL 9.6 via the base `redhat-release` package, but its actual repos are Rocky's. It's not registered with any entitlement server either. This is a half-finished or accidental conversion, not a clean RHEL install — today's package conflict is a direct symptom (version/epoch mismatch between what a true-RHEL base expects and what Rocky's AppStream actually ships). **Recommendation: clean fresh Rocky install rather than trying to salvage the hybrid state** — Chris hasn't finalized this call yet.

**Full service audit done — what actually needs to survive:**
- **Real, worth migrating:** Snipe-IT (`snipe-it-app-1` + `snipe-it-db-1` MariaDB 11.5.2 — needs a real DB dump + app config/uploads backup, not just a redeploy), Portainer agent (trivial redeploy, no data), Zabbix agent2 (trivial, via onboard2.yml pattern), Tailscale (trivial, re-auth on new box).
- **Dead, safe to drop entirely:** `site2-nginx-1` (host-network-mode container, SSL-terminating proxy pointed at `192.168.1.172:8080` — that host is completely gone from the network, "Destination Host Unreachable," config dated April 2025, abandoned well over a year). `nginx1` (serves a static placeholder page, "THIS IS not A LOVESONG" — a joke/test file, not real content).

**Resolved: confirmed KVM VM, not physical hardware, not LXC** — `systemd-detect-virt` returned `kvm`, BIOS product name is QEMU's default "Standard PC (i440FX + PIIX, 1996)" string. The desktop-oriented services (GDM, ModemManager, etc.) were a red herring — probably just leftover from whatever base template/ISO this VM was originally built from. This simplifies the migration a lot: standard Proxmox VM provisioning, no physical access needed, same pattern as every other VM in the fleet.

**Dead nginx cruft removed 2026-07-26** — `site2-nginx-1` and `nginx1` both stopped and removed (`docker stop`/`docker rm`, confirmed gone via follow-up `docker ps -a`), config directories `/opt/site2/` and `/opt/website/` deleted too (confirmed contents first via `find` — just certs, compose files, the joke index.html, nothing unexpected). Also found `/opt/audiobookshelf/` while checking `/opt/` afterward — no container exists for it (not even stopped) and the directory's only 124K, far too small for a real media library. Dead scaffolding, never actually deployed. Doesn't factor into migration scope.

**Migration executed and confirmed 2026-07-27 — clean fresh install, not a salvage of the hybrid state.**

- **Backup:** `mariadb-dump` (not `mysqldump` — MariaDB 11.5+ renamed the client tool, no compat symlink in the image) of `snipe-it-db-1`, plus `.env`/compose config and the `snipe-it_storage` Docker volume (uploads, encryption keys), all pulled off plow-rpm to git-ansible before touching the OS.
- **New VM:** 173 (`plow-rocky`), provisioned on **babar** (not shardik — shardik's still down), 2 vCPU/4GB/40GB — deliberately right-sized down from the old VM's 12 vCPU/8GB, since it only needs to run 3 Snipe-IT containers. **Wouldn't boot at all on the first two attempts** — kernel panic ("Attempted to kill init!") within under a second of boot, invisible on the console because it happened too fast to catch. Root cause: Proxmox's default CPU model (`kvm64`) doesn't support the instruction set Rocky/RHEL 9 requires (x86-64-v2) — fixed with `qm set 173 --cpu host`. **Flag for any future EL9 VM build: always set `--cpu host` explicitly.**
- **Restore:** DB imported clean (verified real data — 35 assets/2 users at the row level, dashboard-visible 27/83/2 matching the old instance exactly, difference is likely soft-deleted rows not counted on the dashboard). Storage volume restored via a throwaway `alpine` container mounting both the backup and the named volume (works regardless of Docker's storage driver, no need to touch `/var/lib/docker` paths directly).
- **Cutover:** old plow-rpm (VM 172) stopped, plow-rocky's static IP set to 192.168.1.53 via `nmcli` (cloud-init's `ipconfig0` only applies on first boot, not reliably on every boot — direct `nmcli` was more reliable), `.env`'s `APP_URL` flipped back from a temporary `.212` test value to `.53`, confirmed loading correctly in-browser. Old VM 172 destroyed (`qm destroy`) only after the new one was confirmed live at the real address.
- **Onboarding:** `onboard2.yml` run against the new host (hostname `plow-rpm`, group `linux`) — hit two real playbook bugs, both **not host-specific, will recur for any future RPM-family onboarding:**
  - **"Group sudo does not exist"** — the playbook assumes Debian's `sudo` group; RHEL/Rocky uses `wheel`. Worked around live with a benign empty `sudo` group (`groupadd sudo`, no real permission change) to unblock, but the playbook itself needs an OS-conditional fix. **Sam/Jordan.**
  - **Zabbix agent2 install fails** — "No package zabbix-agent2 available" on Rocky 9, because the playbook never adds Zabbix's official repo for RHEL-family hosts (Debian hosts get it some other way, not audited tonight). Installed manually this session (`rpm -Uvh` the Zabbix 7.0 RHEL9 release package, matched to the fleet's existing 7.0.28 agent version — confirm this stays version-pinned to whatever the Zabbix server expects). **Same fix belongs in `onboard2.yml`. Sam/Jordan.**
  - Scrutiny was correctly skipped — plow-rpm's a VM, no direct SMART/disk access to report.
- **Naming collision, caught and fixed same session:** a re-run of `onboard2.yml` used hostname `rocky-rpm` instead of `plow-rpm` by mistake, creating a real duplicate/conflicting entry against the pre-existing, unrelated `rocky-rpm` host (192.168.1.51, see 2026-07-21 above). Both `/etc/hosts` and `hosts.md` briefly had two different IPs claiming the same hostname. Fixed: corrected both files back to `plow-rpm`, deduped the resulting double-entries, regenerated `inventory_auto` manually rather than waiting for the hourly cron. No lasting damage, but worth remembering `onboard2.yml`'s hostname prompt has no collision-checking against existing *different* hostnames (only checks if the exact IP+hostname pair already exists).
- **Homepage:** added to both instances — the primary (monitor-deb) already had a correct `Snipe-IT` entry from before (IP never changed, so it never went stale), only the backup instance (backup-dietpi-deb) needed the new entry added.
- Dead nginx cruft (`site2-nginx-1`, `nginx1`, `/opt/site2/`, `/opt/website/`) removed 2026-07-26 as part of the pre-migration audit — see below, unchanged from the original finding.

## New Project: Host Offboard/Decommission Script ("debark") — spec'd 2026-07-26, not built

Counterpart to `onboard2.yml` — no existing script does this (`playbooks/` only has an unrelated `remove_apache.yml`). Chris's spec, verbatim requirements:

1. **Network scan** — same discovery mechanism as the existing hourly `scan_and_update_v2.sh`/`parse_scan.py` chain.
2. **Diff against source of truth** — compare what's actually found on the network against `/etc/hosts` and `inventory_auto`.
3. **Anomaly-driven prompt** — if a host in hosts/inventory no longer appears on the network (or similar mismatch), interactively ask Chris whether to offboard it. Not fully automatic — needs his confirmation per host.
4. **Manual offboard path too** — a way to trigger offboarding a specific host directly, without waiting for the scan to flag it.
5. **Full removal, everywhere** — when a host is offboarded, strip every reference to it: `/etc/hosts`, `inventory_auto`, Zabbix, **both** Homepage dashboard instances, Scrutiny, Telegram (alert routing/host-id labels), "everything everywhere." Needs a real audit of every system a host can be registered in before this is considered complete — the list above is what's known today, may not be exhaustive.

**Not started.** This needs proper specing/build by Sam (script author) and review before it touches anything, given it's a removal tool touching six+ systems — not something to improvise live. Natural pairing with the still-open Snipe-IT refresh and the `inventory_auto` group-scoping cleanup item, since all three are "keep the fleet's source-of-truth systems honest" work.

## Weekly Patch Automation — Root-Caused and Fixed 2026-07-26

- ⚠️ **Real finding: the entire weekly Sunday 3am patch/update/reboot automation has been silently failing, likely for months.** Chris asked to confirm "the update" ran last night (today is Sunday) — checked the logs and all three jobs (`update_docker_containers.yml` 3:00am, `docker_prune.yml` 3:15am, `update_reboot_linux.yml` 3:30am) were dying immediately with `[ERROR]: Attempting to decrypt but no vault secrets found`. Root cause: none of these three root-cron lines pass a vault password, unlike other jobs in the same crontab that correctly use `--vault-password-file`. The vault password file itself (`/home/cos/.vault_pass`, 0600) exists and is valid — it just was never wired into these three lines. Log also showed an even older failure mode ("Host key verification failed") predating the vault issue, meaning this has likely been broken in one form or another for a long time.
- **Chris confirmed reactivating this is fine**, understanding `update_reboot_linux.yml` reboots hosts unattended if updates require it — this was flagged explicitly before making the change.
- **Fix applied:** backed up root's crontab (`/tmp/root_cron_backup_20260726.txt`), added `--vault-password-file /home/cos/.vault_pass` to all three lines via a reviewed `diff` before installing, confirmed installed via `sudo crontab -l -u root`.
- **Verified via `--check` (dry-run) on all three playbooks — vault error is gone, real logic now executes.** Confirms real pending-update backlog exists: babar, maturin, aslan, and blaine all show `changed` under package updates, meaning real fixes are queued up and will actually apply this coming Sunday now that the automation works again. Also surfaced (not new, not urgent): expected UNREACHABLE noise for non-Linux devices (phones/TVs/printers/router) hit by an overly-broad target group — matches the existing "scope inventory_auto groups tighter" backlog item; a minor cosmetic `when`-clause bug in the two Docker playbooks for unreachable hosts (ignored, non-blocking); and the "Docker not running" report for docker-deb is likely a `--check`-mode false negative (shell/command tasks typically skip under dry-run), not a real problem — should resolve itself on the real Sunday run.
- **Real (non-check) run executed 2026-07-26 morning, confirmed successful** — no vault errors, git-ansible/kasm-2404-deb/restic-deb all confirmed freshly rebooted via direct `uptime` checks (~1h05m at time of verification). Packages actually updated on babar, maturin, aslan, blaine, git-ansible-deb, kasm-2404-deb, docker-deb, restic-deb, rocky-rpm, alma-rpm. Note: an earlier attempt at this same run was manually cancelled (Ctrl+C, "intolerable" silent output with plain `>>` redirect) — checked for damage afterward (dpkg lock/broken packages), confirmed clean, no residual issue from the cancellation.
- ⚠️ **Three real, pre-existing issues surfaced now that the automation can actually reach them (not caused by the vault fix, newly visible because of it):**
  - **monitor-deb out of disk space again** — "No space left on device," blocked Ansible from even creating a temp dir there. Same Prometheus-retention issue flagged 2026-07-21 (never got a permanent fix, only a stopgap cleanup) — now actively blocking automation, not just a background concern. Retention/disk-size decision still pending Chris.
  - ~~**plow-rpm package update failed for real** — dnf transaction conflict...~~ — **moot as of 2026-07-27**: plow-rpm was fully replaced with a clean Rocky Linux 9 VM (see migration writeup above), not patched in place. The hybrid RHEL/Rocky repo state that caused this conflict no longer exists.
  - **truenas-bsd SSH host key changed** — "REMOTE HOST IDENTIFICATION HAS CHANGED" warning, connection refused (`Offending ED25519 key in /root/.ssh/known_hosts:77`). Not yet investigated — could be benign (key rotation after a TrueNAS update) or worth confirming before clearing the old key. **Do not blindly `ssh-keygen -R` this without Chris/Taylor confirming the cause first.**
- ~~Also noticed in passing: "apache-deb" appeared in a PLAY RECAP...~~ — **checked 2026-07-27, closed as non-issue.** Not in `/etc/hosts`, not in `inventory_auto`, no Ansible fact-caching configured (nothing to go stale), no file anywhere on git-ansible references it. No lead to chase — likely a one-off artifact or a misread hostname in the original recap, not a real host that needs cleanup.

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
- [ ] Clean up `inventory_auto` group membership — the `all`/default groups include many non-Ansible-manageable devices (router, network gear, printer, phones, TVs, Roomba, Windows boxes needing WinRM not SSH). Every ad-hoc/playbook run against `all` throws ~15 "UNREACHABLE" errors that are just noise, not real problems. Worth scoping a proper `[linux]`/`[proxmox]` group and keeping non-Linux devices out entirely.
- [ ] Two hosts (pihole-pi1-deb, blank-dietpi-deb) missed their apt-update step in today's baseline run due to a dpkg/apt lock collision (leftover from an earlier accidental duplicate ansible-playbook run colliding with itself) — safe to pick up on the next scheduled run, low priority.

### Homepage: how the two instances actually differ (documented 2026-07-30, per Chris's request)

**Deployment method is fundamentally different, not just content:**
- **monitor-deb (primary, 192.168.1.29:3002):** runs in Docker. Config lives at `/home/cos/monitoring/homepage/config/services.yaml` on that host, edited directly, picked up without a full service-management dance.
- **backup-dietpi-deb (backup, 192.168.1.126:3002):** no Docker at all on this host. Runs as a native Node process via systemd (`homepage.service` → `node .next/standalone/server.js`), a Next.js standalone production build. **The config it actually reads is `/home/cos/homepage/.next/standalone/config/services.yaml`** — a separate copy from `/home/cos/homepage/config/services.yaml` (the source-tree location, which is what shows up first in an obvious `find`). Editing the source-tree copy does nothing until it's also copied into the standalone path and the service is restarted (`sudo systemctl restart homepage.service`).

**Content is now identical** (both instances' live configs verified byte-for-byte matching and visually confirmed rendering the same layout as of 2026-07-30) — same services, same widgets, same live data sources. Both dashboards will keep drifting apart on every future edit unless whoever's editing remembers the backup instance's path gotcha above.

**Not resolved / worth a future decision:** should the backup instance be converted to Docker to match the primary's deployment method (removes this whole gotcha permanently), or is native Node deliberate for this Pi's resource constraints? Not touched this session — Chris didn't ask for that scope, just parity and documentation of the difference.
- [ ] hw_inv.md/CLAUDE.md network table: shardik's line still says "back online 2026-06-28, 1-month uptime target" — stale now that it's confirmed CPU-dead, not touched yet since Chris didn't ask for that specific edit this session.

## Decisions Made This Session (2026-07-21)

- **Canonical TrueNAS hostname: truenas-bsd** (matches fleet naming convention — shardik-pve1-deb, maturin-pve2-deb, etc., confirmed via router DHCP table). Fixed on git-ansible (source of truth for fleet-wide DNS via homelab_baseline.yml's hosts-push task) and propagated. Router's own DHCP reservation tag was a red herring — that field (`tag`) doesn't generate DNS records in dnsmasq, only `name` does.
- **rocky-rpm moved to 192.168.1.51**, its correct range per Chris's documented IP scheme (50-69 = RPM servers). Was squatting at .20 (Debian/VM range) due to a static IP set outside DHCP.
- **octopi-deb/octopi-pi4-deb duplicate naming consolidated to octopi-pi4-deb only** (one of the four known Pi dual-naming pairs flagged in the Jordan backlog below — the other three, pi1-deb/pihole-pi1-deb, pi2-deb/blank-dietpi-deb, pi4-deb/backup-dietpi-deb, are being kept as intentional aliases per Chris, not touched).
- **swarm01/02/03 (VMs 102/104/105) confirmed fully decommissioned**, not just stopped — hw_inv.md and project memory both had them listed as "stopped/pending" for weeks; they're actually long gone. DHCP reservations and hosts entries removed to match.

## Action Items — 2026-07-16 (babar onboarding gaps, live-verified)

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
- [ ] Morgan's undocumented-changes tally: babar's three 2026-07-16 onboarding gaps (Ansible inventory, hosts.md, Homepage dashboard) are still open — carried forward again, no movement this week.
- [ ] Riley: rack Phase 1 (place rack, install SG200-50/PDU) still waiting on Chris's physical time — transport unblocked since 2026-07-12. **Chris flagged renewed interest 2026-07-24 — this is now his stated next priority.**

## Action Items — Weekly Team Meeting 2026-07-26 (new this session)

- [ ] ⚠️ **Confirm whether this morning's 3am Sunday cron (weekly_patch.yml / docker_prune.yml / update_reboot_linux.yml) actually ran clean under the vault-password fix applied earlier today.** This is the first real run since the fix — everything before was a `--check` dry-run. Jordan to pull the logs and confirm babar/maturin/aslan/blaine actually picked up their queued updates (and, per `update_reboot_linux.yml`, rebooted if required).
- [ ] **Sam proposal 5 (pending Chris approval): todo.md auto-archiver.** File is 572+ lines and growing weekly from session-recap stacking. Script would move resolved/superseded sections older than a rolling window into a separate `todo_archive.md`, keeping the live file scannable. Sam's pitch: same "keep source-of-truth honest" spirit as the debark script and the storage.cfg linter, just aimed at the doc itself.
- [ ] **Sam proposal 6 (pending Chris approval): Scrutiny→Telegram config script.** Automates writing the `telegram://` Shoutrrr URL into `scrutiny.yaml` on docker-deb, pulling OerthBot's token from `/etc/oerthbot/config.json` without it touching any terminal/chat history, then restarts the container and fires the health/notify test endpoint. Directly builds the already-scoped-but-not-started Scrutiny→Telegram item from earlier this week.
- [ ] **Sam proposals 1–4 (storage.cfg node-scoping linter, MkDocs pre-push diff-check, hw_inv.md auto-diff-audit, shardik MCE watcher) still awaiting Chris's approval — carried forward again, no movement.** Proposal 4 specifically flagged this meeting: shardik's CPU is confirmed dead and Chris has deprioritized the node, so an MCE watcher may now be moot. Needs Chris's explicit call — keep it queued for a future node, or drop it.
- [ ] Alex confirmed cru3's current label as **STL_FIGURES** (most recent, 2026-07-24) — reminder to the team that this has changed multiple times and scripts/docs should always be checked against Alex's live word, not assumed from memory.
- [ ] Morgan: hw_inv.md's shardik line still reads "back online 2026-06-28, 1-month uptime target" — stale on two counts now (CPU confirmed dead, and Chris deprioritized the node entirely). Carried forward from 2026-07-21, still not edited.
- [ ] Riley: Rack Build Phase 1 (place rack, install SG200-50/PDU) still waiting on Chris's physical time — this remains his stated top priority as of 2026-07-24, no movement this week.
- [ ] Taylor: Prometheus retention/disk decision for monitor-deb still pending Chris (see 2026-07-21 action items) — disk is stable for now (88%/3.6G free) but not a permanent fix.
- [ ] Kai: babar's nvme128/nvme512 storage table entries still missing from hw_inv.md; storage.cfg node-scoping risk (SDA_store/hdd12tb/hdd3tb/nvme_store aliasing local disk on babar) still not fixed — flagged again as a real CRU/STL data-misdirection risk, not just cosmetic.

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
