# Homelab Todo & Roadmap
_Last updated: 2026-07-06 end of session (Garm=red case, Gan=TrueNAS rebuild hostname — naming closed. Shardik RAM addressed, uptime clock stays paused until a sustained stress test/benchmark confirms stability — Jordan/Kai. Cleared stale "Telegram bot" line-items — OerthBot fully deployed; real remaining gaps are SMART/smartd wiring and Zabbix media type, both under Taylor. octopi-pi4-deb SSH connectivity confirmed via fleet run. Same fleet run surfaced: batocera-deb/pi3-deb showing "unreachable" in the linux-group recap instead of being cleanly skipped, duplicate inventory aliases across 4 Pi hosts, and a tools-deb vs. ha-net naming conflict at .125 — all logged for Jordan. Internal DNS raised as a want, logged against the existing Unbound item, sequencing TBD by Riley. Tomorrow's priority: bench-test the SG200-50/SG-1100 switch in place on top of freenas-bsd — not a rack install — over SMART wiring. Prior 2026-07-05 note: patch reboots ruled NOT to count against shardik's uptime clock; garuda confirmed as pve3's hostname; Sam's two proposals approved; every specialist has ≥5 tasks queued for next week)_

---

## Decisions Still Needed from Chris

- [ ] **Hyper-V VLAN approach for amontillado** — still open. Reasoning for why the VMs were proposed for Servers (VLAN 10) instead of Trusted (VLAN 20): Trusted is meant for physical end-user devices (amontillado itself, phones, etc.), Servers is meant for anything acting as backend infrastructure. If amontillado's Hyper-V VMs are running actual services other systems depend on, keeping them in Trusted either forces opening Trusted↔Servers broadly (defeats the segmentation) or leaves them unreachable from the rest of the infra. If they're just personal/test VMs with no service role, Trusted is fine — worth Riley confirming what those VMs actually do before deciding.

---

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
1. Wire an actual notification channel into backup-dietpi-deb's Kuma instance — it's ping-only right now, which is why today's shardik drop didn't page anyone
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
- [ ] Add pve3 (garuda) to the Proxmox cluster (shardik + maturin + aslan + blaine + garuda)
- [ ] Configure Tailscale on pve3/garuda; full hardware inventory (dmidecode, photos)
- [ ] Add pve3/garuda to inventory_auto and MkDocs
- [ ] Migrate mediastack-deb → shardik after uptime target holds (currently on aslan)
- [ ] Right-size VM RAM allocations across all nodes
- [ ] Shrink maturin pve-data pool — only cloudinit template remains on local-lvm
- [ ] Investigate maturin VM 112 leftover disk on shardik NVMe (164GB orphan)
- [ ] P2V GOODWIM CentOS drive (Seagate 500GB) before disposing
- [ ] Manyfold — blaine LXC (CT 103) outperforming docker-deb; one more week before calling it permanent. Do NOT delete CT 103.
- [ ] GPU transcoding — revisit mediastack on aslan with GTX 1080 Ti passthrough once RAM allows (Casey + Kai)
- [ ] Rebuild swarm01/02/03 when actually needed (currently destroyed, clean rebuild, no Ceph)
- [ ] Deploy Traefik / Uptime Kuma / Homepage / Zabbix frontend in Swarm mode (longer-horizon)
- [ ] Local AI Assistant (aslan): Ollama + GTX 1080 Ti passthrough, Open WebUI, sysadmin/homelab/casual personalities, Whisper/Piper, MkDocs as RAG knowledge base

### Storage, Backup & CRU Rotation (Alex)
- [ ] STL_FIGURES — audit all scripts for hardcoded old label references (cru3 was: STL_Non-Fantasy → STL_#CRUNCH → STL_FIGURES)
- [ ] STL_ACCESSORIES_TERRAIN (2.7TB) — rsync in progress since 2026-07-03, blocked on throughput crisis below
- [ ] STL_SOURCE_MATERIAL (2.7TB) — rsync in progress since 2026-07-03, blocked on throughput crisis below
- [x] **rsync throughput — major improvement 2026-07-05: ~400kB/s → 25MB/s (~60x).** No longer a viability crisis — 2.7TB is now ~30 hours, not 44 days. Root-cause work continues at lower urgency (Alex/Riley/Taylor), no longer blocking trust in the backups.
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
- [x] **Patch panel dropped from rack plan — decided 2026-07-05.** Only real structured cable run in the house (Flint 2 → Beryl AP) isn't anywhere near where the rack will go, so there's nothing to terminate at a panel. Cables plug straight into SG200-50 ports instead. Frees ~1U.
- [ ] **Theoretical rack contents updated 2026-07-05:** SG200-50 (1U), MD1200 (2U, fixed spec), Dell R750 + HBA for TrueNAS (2U, fixed spec, replaces the vague "TrueNAS rack-mount chassis" placeholder), pfSense/SG-1100 on a 1U shelf, PDU (0-1U). Roughly ~12U or under without the patch panel — workable for the 12U half rack. UPS placement (rackmount vs. floor-standing) still undetermined. Pi rack + maturin shelf may need to live outside the enclosure if space stays tight.
- [ ] docker-deb static IP or confirmed DHCP reservation ⚠️ (hosts Vaultwarden, Traefik, Portainer)
- [ ] **VPN rationalization — DECIDED 2026-07-05: Tailscale.** Decommission WireGuard (mediastack) and ZeroTier (amontillado).
- [ ] Netgate (192.168.1.6) — confirm model and role, unresponsive to nmap/arp-scan
- [ ] Identify 192.168.1.218 (locally administered MAC, high ephemeral ports only)
- [ ] Clarify Flint2 + Netgate topology — document which handles what
- [ ] Scan guest WiFi subnet — third LG TV likely there
- [ ] Unbound (local DNS resolver) for internal hostname resolution (garm, gan, garuda, etc. instead of raw IPs — Chris flagged 2026-07-06), Authelia (auth layer) — longer-horizon; likely depends on the pfSense/switch VLAN rollout landing first, Riley to scope sequencing
- [ ] **Rack Build + pfSense + VLANs** — hardware in hand (APC half rack, SG-1100, SG200-50 configured, GS116 to retire). Priority raised: GS116 has a confirmed dead port after 7 years and no port visibility to diagnose others.
  - Phase 0: **transport rack home** — currently offsite, needs Chris's car
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
- [x] cru_stats.sh / backup_drives_update.sh path mismatch fix — ✅ Alex signed off 2026-07-05, Sam cleared to ship
- [x] **Telegram bot (patch notifications) — done 2026-07-05.** OerthBot deployed, weekly_patch.yml wired, see Resolved This Session above.
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
- [x] Pi 2B — ✅ renamed **docs-dietpi-deb** 2026-07-05 (192.168.1.121), role: documentation-adjacent host. Jordan to update Ansible inventory + hostname; Morgan to add to hosts.md.
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
- [x] **octopi-pi4-deb connectivity confirmed 2026-07-06** — homelab_baseline.yml run reached `ok` against the host (reaching "ok" requires a working SSH connection). The polkit/fwupd warning in the run is expected and harmless — that task already has `ignore_errors: yes`.
- [ ] Add Zabbix repo task to homelab_baseline.yml (before agent install)
- [ ] Fix SSH service name for DietPi hosts (ssh vs. dropbear)
- [ ] Fix ansible_facts deprecation warnings before ansible-core 2.24
- [ ] Document mkdocs_dev_material living on restic-deb intentionally
- [ ] Pin ansible_python_interpreter per host in inventory_auto
- [ ] Add chrony LXC skip to sync_time.yml; update check_services.yml; fix pause timing in fail2ban.yml
- [ ] Audit offline hosts from router — inactive vs. decommissioned
- [ ] Confirm batocera-deb (and pi3-deb — host TBD) are actually in `[linux_skip]`, not `[linux]` — 2026-07-06 fleet run shows both "unreachable" in the linux-group recap, meaning the host pattern didn't exclude them like it should have
- [ ] Dedupe Ansible inventory aliases — pi1-deb/pihole-pi1-deb (.120), pi2-deb/blank-dietpi-deb (.121), pi4-deb/backup-dietpi-deb (.126), octopi-deb/octopi-pi4-deb (.122) each resolve to the same physical host, so the baseline playbook runs twice against each
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
| shardik | 32GB (4×8GB DDR4-2400) | 128GB (4×32GB UDIMM) | 4×32GB — 2 in hand, 2 more DC machines to check |
| aslan | ✅ 64GB (4×16GB) complete | 128GB (4×32GB UDIMM) | 4×32GB — scavenging DC2/DC3 |
| maturin | 32GB (4×8GB) | 64GB (maxed) | 4×16GB UDIMM — 10 found at DC 2026-07-02 |
| blaine | 32GB DDR3-1333 | 32GB | ✅ sufficient, no upgrade path worth it |

⚠️ DC server RAM is DDR4/DDR5 RDIMM ECC — not compatible with AM4 consumer boards. Only desktop DDR4 UDIMM non-ECC works.

### Hardware Inventory Completion
- [ ] Photo + dmidecode all 5 waiting systems, pve3, printers (Elegoo Mars 3, Ender 3 V1, Flashforge Dreamer), GPUs, laptops
- [ ] SCP new photos to MkDocs docs/images/hw/
- [ ] Import all hardware into Snipe-IT (192.168.1.53 — plow-rpm)
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

Active Proxmox nodes: shardik (bear), maturin (turtle), aslan (lion), blaine (Blaine the Mono), garuda = pve3 (bird, confirmed 2026-07-05). Red case: **Garm confirmed 2026-07-06** (dog, Norse mythology, Hel's hellhound). TrueNAS (freenas-bsd) rebuild: **Gan confirmed 2026-07-06** (Dark Tower — new name, outside the original reserve pool). Remaining unused reserve: babar, navius, rocinante, chuchundra, jasconius, camazotz, owsla.
