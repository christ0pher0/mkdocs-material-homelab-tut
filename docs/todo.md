# Homelab Todo & Roadmap
_Last updated: 2026-07-05 (backup-dietpi-deb "watch the watcher" stack fully live — Kuma + Homepage both persistent via systemd, 27 hosts monitored, real ping widgets working on both dashboards; caught a genuine shardik network drop same day — resolved (stale ARP, not hardware), guest was healthy throughout; monitor-deb ↔ backup-dietpi-deb monitoring now mutual in both directions; Proxmox HA sequencing decided — blocked on shared storage + shardik uptime lock; Logitech Z-680 static/dropout symptom being triaged, root cause not yet confirmed; STL rsync throughput crisis escalated to critical, 710kB/s / ~44 days not viable; weekly_patch.yml 3am reboot vs. shardik uptime-clock conflict flagged for Chris; red case tentatively named garuda pending sign-off; Sam proposed two new automation projects; see Decisions Needed section below)_
---

## Decisions Needed from Chris — 2026-07-05 Meeting

- [ ] **Weekly patch reboots vs. shardik uptime clock** — weekly_patch.yml runs Sundays 3am and can reboot nodes for kernel/microcode updates. Shardik's 1-month target (2026-08-01) was framed as "stability," but a patch-triggered reboot resets a literal uptime counter. Jordan needs a call: (a) exclude shardik from automated patch reboots until Aug 1, or (b) treat the target as "no unplanned crashes" and let scheduled reboots continue. Decide before next Sunday's 3am run.
- [ ] **Red case hostname** — team proposed **garuda** (next name off the approved 12-name master list) for the ASRock B450M Steel Legend red case. Needs Chris sign-off before Jordan/Kai provision it.
- [ ] **Sam's two new project proposals** — (1) extend the in-progress Telegram bot from patch-only notifications into a general alert relay (Kuma/Zabbix/SMART all through one bot), (2) a "drive label linter" that scans all scripts/configs for stale CRU label references (cru3 has changed labels 3x and bitten the team before). Approve, prioritize, or park.
- [ ] **STL rsync throughput crisis timeline** — at 710.56 kB/s a 2.7TB copy is ~44 days, not viable. Alex/Riley/Taylor want to prioritize root-causing this by next Sunday (2026-07-12) — confirm this takes precedence over other assigned network/storage work this week.

---

## Critical / Security

- [ ] **cos SSH key auth on freenas-bsd (192.168.1.5) — DECIDED 2026-07-03: staying on password, not fixing.** Root cause fully diagnosed: OpenSSH `StrictModes` rejects pubkey auth because `/mnt/TRYAGAIN` (pool root, owner `cifs1:plex_access`, mode `drwxrwx---+`) is group-writable and `cos` is a `plex_access` member — StrictModes checks every ancestor directory in the path, not just the immediate home dir. Mid-session fix attempt: created new sibling dataset `TRYAGAIN/admin` (root:wheel, no group-write) and relocated cos's home to `/mnt/TRYAGAIN/admin/cos` (rsync'd dotfiles/authorized_keys over, correct 700/600 perms, Home Directory field repointed via WebUI) — this did NOT work, because `/mnt/TRYAGAIN` itself is still an unavoidable ancestor of any dataset under that pool, and its group-write bit was never touched. Real fix identified (Alex): remove Write from the `group@`/`plex_access` ACE on the **pool root** dataset only (Storage → Pools → TRYAGAIN → Edit Permissions → uncheck group Write, leave Read+Execute) — safe because Samba only writes inside subdirectories like `plex/`, never at the root, **provided "Apply permissions recursively" is left OFF** (checking it would strip plex_access write from every share subdirectory, breaking CIFS fleet-wide). Chris declined to make this change — too risky-feeling for a production pool root; password auth on this one host is an acceptable asymmetry vs. the rest of the Ansible-keyed fleet. **If revisited:** the fix above is exact and ready to execute, just needs sign-off. cos's home directory is now permanently at `/mnt/TRYAGAIN/admin/cos` (moved from `/mnt/TRYAGAIN/home/cos`, old copy left untouched, not deleted) regardless of the key-auth decision.
- [ ] docker-deb static IP or confirmed DHCP reservation — hosts Vaultwarden, Traefik, Portainer ⚠️
- [ ] Disk space alerts — amontillado C: (7% free ⚠️), pi1 SD (91%) ⚠️
- [ ] **amontillado C: drive** — 65.9GB free of 930GB (7%). Jordan to audit what's consuming it
- [ ] **Telegram bot** — Sam building patch notification bot (weekly_patch.yml results → Telegram after 3am run). Needs token + channel ID from Chris.
- [ ] **docker-deb watchdog** — Sam building script to alert Uptime Kuma if container stack hasn't restarted in >1 week
- [ ] Alert on: drive errors, disk >85%, service down, high temp, RAM pressure
- [ ] **monitor-deb (VM 101, maturin) hung 2026-07-03 — no alert fired.** Chris caught it manually and restarted it; fixed. Root gap: monitor-deb hosts Uptime Kuma + Zabbix themselves, so when the VM hangs, the thing that would alert on downtime is the thing that's down — no external/independent watchdog exists for the monitoring host itself. **Decided 2026-07-03: install Homepage + Uptime Kuma on `backup-dietpi-deb` (S3, RPi 2B, 192.168.1.126)** as an independent secondary monitoring point, alongside its existing Gitea mirror + Vaultwarden backup duties — both new services are low-footprint enough that the Pi has room. Rationale for weight choice: Homepage is lightest (static dashboard, on-demand API pulls, no polling loop, no DB) and Uptime Kuma is next-lightest with active alerting (small Node.js app, SQLite, its own polling loop); Grafana and Zabbix were ruled out as too heavy for this Pi. Note: `blank-dietpi-deb` (S2, .121) remains fully unassigned/role TBD if Chris later wants to split this out separately instead of consolidating onto backup-dietpi-deb. Taylor/Sam to implement.
- [ ] Investigate amontillado D: (2.79TB, 11% free) — audit VMs and junk, clear or expand
- [ ] **VPN rationalization** — 3 VPN solutions running (Tailscale, WireGuard on mediastack, ZeroTier on amontillado). Riley to pick one and decommission the others
- [ ] **X540-T2 in freenas-bsd — evidence now strongly points to genuinely dead card, not board/slot/cable.** 2026-07-04: reseated and retested with a different known-good patch cable AND a different switch port (in addition to the original session's cable/port cross-test) — both ix0 and ix1 still show "no link ... giving up" via `dhclient`. Card still enumerates cleanly on the PCIe bus (pciconf/dmesg, device 0x1528), so this isn't a bus/detection issue — both PHYs simply refuse to link regardless of what's plugged in, which is classic hardware failure, not a driver or cabling problem (a driver bug would typically prevent the interface from working at all or behave inconsistently, not just refuse link negotiation cleanly on both ports every time). Bench test on a separate machine is still the final formal confirmation but is now more a formality than an open question. **Also tried 2026-07-04: reinstalling the Dell 0THGMP (Intel I350-T4 quad-port) instead** — this card beeped continuously and auto-shut-down the system on boot, a different failure mode entirely (looks like a board-level BIOS/Option ROM/CSM issue on this old Gigabyte Z77-DS3H board, not the card — Chris recalls this exact card working fine in another machine, possibly shardik, which would confirm it's this board's BIOS, not the card). Net state: `alc0` (onboard, slow but working) remains the only functional NIC on this box for now. LAGG plan below is on hold until a working second/replacement NIC is actually confirmed.
- [ ] **Alex + Riley: LAGG on freenas-bsd** — originally planned around X540-T2 ix0+ix1, now on hold pending resolution above. Link-aggregate for NIC redundancy — needs LACP/failover config on both TrueNAS (Network → Link Aggregations) and SG200-50 switch port config. Backlog, not urgent.

### Backup Strategy

- [ ] STL_FIGURES — audit all scripts for hardcoded old label references (cru3 was: STL_Non-Fantasy → STL_#CRUNCH → STL_FIGURES)
- [ ] **STL_ACCESSORIES_TERRAIN (732G + 446G ≈ 1.18TB combined)** — drive ST3000NM0033-9ZM178, serial Z1Y331AG, 2.7TB. Partitioned, formatted, labeled, mounted, **rsync IN PROGRESS as of 2026-07-03**. Attached to VM 100 scsi1.
- [ ] **STL_SOURCE_MATERIAL (1.4T)** — drive ST33000651NS, serial Z292SYYH, 2.7TB. Partitioned, formatted, labeled, mounted, **rsync IN PROGRESS as of 2026-07-03**. Attached to VM 100 scsi2.
- [ ] ⚠️ **restic-deb VM rsync throughput very slow — 710.56 kB/s average.** At this rate a 2.7TB copy is ~44 days — not viable. Needs diagnosis before either STL drive rsync is trusted to finish this week. Alex to own; Taylor/Riley to check freenas-bsd `alc0` link negotiation as a prime suspect (recently-revived NIC, previously "dead" — possible duplex/speed mismatch, not yet proven stable under sustained load per [[project_lab_state]] risk note). Also check whether rsync is traversing network (TrueNAS source over LAN) vs. local disk-to-disk on VM 100 — very different bottlenecks. **Escalated 2026-07-05 team meeting — target root cause identified by next Sunday (2026-07-12).**
- [ ] **FUTURE_USE spare (2026-07-03):** ST6000VN0001-1SF17Z, serial Z4D2EJ31, 5.5TB. Partition, format NTFS, label "FUTURE_USE" — no content assignment yet. Attached to VM 100 scsi3 2026-07-03.
- [ ] SOURCE_MATERIAL (1.4T) — no drive assigned. Inventory available drives first, then assign. On hold.
- [ ] **STL_T-Z status unresolved** — backup_drives.md (local) shows Jun 2026/✅ per todo.md's completion claim, but cru_plexfolder_stats.sh --view live cache still shows Feb 2025/— as of 2026-07-03. Two sources disagree — confirm actual state before trusting either.
- [ ] sdc (20TB) — pulled from CRU rotation 2026-07-02. Relabel as spare. Shelf it — quick pivot if TRYAGAIN needs emergency replacement. History: prior anxious behavior in TrueNAS, passed SMART 2026-07-02. **Confirmed 2026-07-03: dedicated emergency TrueNAS spare, not returning to CRU rotation.**
- [ ] **Logitech sub recap** — caps blown on subwoofer (Z-680). Onset 2026-07-05: fine this morning, degraded same day to intermittent speaker count (1, now fluctuating to 2) plus heavy static/hum on both working speakers — rapid same-day onset is typical of caps crossing end-of-life (gradual wear, abrupt failure), not a new/separate cause. Static points to PSU-section caps (ripple bleeding into audio), not just whatever's causing the channel dropout — Drew should scope the recap kit to cover PSU caps, not just the minimum for the dropout symptom. Revisit Sunday.
- [ ] Establish offsite drive rotation schedule (Tier 3)
- [ ] Evaluate PBS tape backup to CRU bays (blaine-pve post-install)
- [ ] cru_stats.sh saves to /root/scripts/cru_stats/ (sudo) but backup_drives_update.sh reads ~/scripts/cru_stats/ — fix path mismatch

---

## This Week — Assigned

- [ ] **Jordan: amontillado C: drive audit** — 7% free, find what's consuming it. `WinDirStat` or `du` via WSL
- [ ] **Jordan: pihole-pi1-deb SD card** — 91% full, swap with replacement SD in reserve before it fails silently
- [ ] **Jordan: fail2ban rollout** — run fail2ban.yml across all SSH-exposed hosts via Ansible
- [ ] **Sam: cru_stats path fix** — align cru_stats.sh and backup_drives_update.sh to same path. Alex to sign off first.
- [ ] **Sam: Telegram bot** — weekly_patch.yml results → Telegram channel after 3am Sunday run. Needs token + channel ID from Chris
- [ ] **Sam: auto network_inventory.md** — script combining arp-scan + masscan + ansible facts → outputs fresh network_inventory.md. Replaces manual scans.
- [ ] **Sam: refactor backup_drives_update.sh** — use Gitea API instead of local mkdocs clone on restic-deb. Eliminate git conflicts between restic-deb and git-ansible. **Implemented 2026-07-03 (per Chris) — needs testing/validation before it's trusted. Not yet marked complete.**
- [ ] **Sam: auto backup date in cru_stats** — write `Backup: <date>` to stats file when SMART passes. update_drives_table.py to read and update Backup column automatically.
- [ ] **Kai: pve3 Tailscale clustering** — spec corosync over Tailscale, WAN timeout tuning, cold/warm failover runbook. Sunday meeting deliverable.
- [ ] **Jordan: git identity on restic-deb** — set user.email and user.name globally so commits don't fail.
- [ ] **Jordan: BIOS download links** — Jordan to find and provide direct download links for Chris to apply. Current status per dmidecode 2026-07-02:
  - shardik (ASRock AB350M Pro4): P10.43 Jun 2025 — https://www.asrock.com/mb/AMD/AB350M%20Pro4/index.asp#BIOS
  - maturin (Dell OptiPlex 7050): 1.27.0 Sep 2023 — https://www.dell.com/support/product-details/en-us/product/optiplex-7050-desktop/drivers — appears current, confirm ✅
  - aslan (Gigabyte AB350-Gaming 3-CF): F50a Nov 2019 — https://www.gigabyte.com/Motherboard/GA-AB350-Gaming-3-rev-1x/support#support-dl-bios — F52 available ⚠️
  - blaine (Gigabyte GA-Z77-DS3H): F8 Aug 2012 — Rev 1.0: https://www.gigabyte.com/Motherboard/GA-Z77-DS3H-rev-10/support | Rev 1.1: https://www.gigabyte.com/Motherboard/GA-Z77-DS3H-rev-11/support — physical inspection required to confirm revision before flashing
- [ ] **Jordan: add microcode + non-free-firmware to homelab_baseline.yml** — ensure amd64-microcode/intel-microcode installed on all Debian nodes based on CPU vendor, and non-free-firmware repo present. Prevents future drift.
- [ ] **Jordan: onboard pbs-deb** — run onboard2.yml, confirm passwordless sudo and SSH key auth working.
- [ ] **Jordan: octopi-pi4-deb SSH key auth** — confirm key auth works after baseline run; if not, run onboard2.yml individually.
- [ ] **Jordan: blaine sdc SMART long test** — started ~2026-06-29. Expected completion ~Wed Jul 1 5am. Check results, relabel, attach to VM 100 for STL rsync.
- [ ] **Jordan: add Zabbix repo task to homelab_baseline.yml** — restic-deb had no Zabbix repo, agent2 install failed. Add repo setup task before agent install. Sam to implement.
- [ ] **Jordan: fix SSH service name for DietPi hosts** — baseline uses 'ssh' service name but DietPi uses dropbear. Add conditional or ignore for DietPi hosts.
- [ ] **Jordan: fix ansible_facts deprecation warnings** — update homelab_baseline.yml to use ansible_facts["fact_name"] syntax before ansible-core 2.24 drops support. Sam to implement.
- [ ] **Riley: DHCP reservation for octopi-pi4-deb** — lock to 192.168.1.122 on router to prevent drift.
- [ ] **Riley: Flint 2 cutover pre-work** — configure OpenWrt in dumb AP mode; set trunk port to switch GE1 with tagged VLANs 10/20/30/99; map main SSID → VLAN 20, guest/IoT SSID → VLAN 30. Deliver as paste-ready config block.
- [ ] **Riley: pfSense SG-1100 offline config** — initial setup via laptop direct to LAN port (not live network). WAN interface, VLAN interfaces 10/20/30/99, DHCP pools per vlan_ip_plan.md, firewall rules per plan. Deliver step-by-step runbook. Pre-work for cutover weekend.
- [ ] **Riley: Hyper-V VLAN decision for amontillado** — amontillado on VLAN 20 (GE25) but Hyper-V VMs need VLAN 10 access. Decision: (a) trunk port on GE25 + separate vSwitch per VLAN in Hyper-V, or (b) second NIC on amontillado for VLAN 10. Must decide before cutover day.
- [ ] **Jordan: document mkdocs_dev_material on restic-deb** — note it lives there intentionally (required by backup_drives_update.sh until Sam refactors).
- [ ] **Riley: pve3 Tailscale setup** — configure Tailscale on ThinkStation offsite node.
- [ ] **Morgan: session documentation** — shardik recovery runbook, red case inventory page, PBS migration decision log, pve3 DR node page. First active assignment.
- [ ] **Morgan: cluster capacity page** — MkDocs page showing each node: mobo, CPU, current RAM, max RAM, slot config, current VM/CT placement and allocation, upgrade path. Reference before every hardware decision. Kai provides VM data, Jordan provides dmidecode, Morgan builds the page.
- [ ] **Morgan: set holy_grail.md as MkDocs front page** — Chris wants the mission statement as the site's landing page (docs/index.md or mkdocs.yml nav reorder), not buried in the doc tree.
- [ ] **Morgan: pull-before-push check** — before SCPing holy_grail.md / hardware_target_state.md to git-ansible, confirm neither already exists there under a different name/content (avoid repeat of the completed.md overwrite incident 2026-06-28).
- [ ] **Morgan + Riley: MkDocs Network section overhaul** — create dedicated Network section in nav. Move network_inventory.md, network_diagram.md, hosts.md here. Add vlan_design.md. Riley owns content accuracy, Morgan owns structure and nav.

---

## Immediate Maintenance (Sysadmin)

- [ ] **Patch all hosts** — weekly_patch.yml runs Sundays 3am (automated). Manual run if urgent.
- [ ] Fix pi1-deb SD card — 91% full, will fail silently (replacement SD in reserve)
- [ ] Clean stale entries from GL-MT6000 /etc/hosts: snipeit-deb, grafana-docker-deb, ubuntu-ansible-deb, apache-deb, weltgeist-media, alea_iacta_est-media
- [ ] Investigate orphaned Docker network br-ca523ef71531 on docker-deb — prune if safe
- [ ] Remove snipeit-deb from all docs (LXC destroyed 2026-05-10)
- [ ] Remove grafana-docker-deb, ubuntu-ansible-deb, apache-deb from all docs
- [ ] MkDocs update on git-ansible — post every session

---

## In Progress

- [ ] Inventory 5 remaining waiting systems — match hardware to roles
- [ ] Inventory pve3 (ThinkStation offsite) — specs, storage, role
- [ ] Purchase Hologram.io SIM for argos-deb LTE
- [ ] Pi rack — 3D print or buy, house all 8 Pis cleanly
- [ ] PoE switch + PoE HATs — single cable per Pi for power + network
- [ ] Shrink maturin pve-data pool — only cloudinit template remains on local-lvm
- [ ] Investigate maturin VM 112 leftover disk on shardik NVMe (164GB orphan)
- [ ] P2V GOODWIM CENTOS drive (Seagate 500GB) — convert CentOS install to Proxmox VM before disposing
- [ ] Audit offline hosts from router — confirm which are inactive vs decommissioned (eld-win, work-win, tahoe-mac, etc.)
- [ ] onboard pbs-deb via Ansible (onboard_host.yml not yet run — passwordless sudo added manually)
- [ ] **Manyfold** — remove from docker-deb :3214 (poor performance). blaine LXC (CT 103) is the candidate — promising results. Kai to complete evaluation and confirm as permanent home before go-live.
- [ ] **Set Uptime Kuma TrueNAS poll to 30 seconds** — Taylor (USB NIC fragility mitigation)
- [ ] **Check pihole-pi1-deb SD card** — was 91% full 2026-06-21, run `df -h` on pihole-pi1-deb (192.168.1.120)
- [ ] **Ender 3 V2 yellow PLA** — run temp tower first to dial in profile before printing anything structural (Drew)
- [ ] **Pi Status page** — build in MkDocs with uploaded Pi photos (Morgan)
- [ ] **retropi IP** — confirm IP for slot 4 (retropi). Add to hw_inv.md and hosts.md
- [ ] **pihole-pi-deb IP** — confirm IP for slot 6. Add to hw_inv.md and hosts.md
- [ ] **blank-dietpi-deb role** — assign permanent role (slot 2, 192.168.1.121, RPi 2B). Options: Gitea mirror secondary, MQTT broker, rsync relay
- [ ] **Netgate clarification** — confirm model and role in topology (Riley). Did not respond to nmap/arp-scan — offline?
- [ ] **Document monitoring topology** — Zabbix server on monitor-deb :10051, agents on 11 hosts. Is Grafana pulling from Zabbix? Taylor to map.
- [ ] **Identify 192.168.1.218** — locally administered MAC, high ephemeral ports only. Riley to investigate
- [ ] **Identify alma-rpm role** — Apache :80 running, role undocumented
- [ ] **Identify rocky-rpm role** — SSH only, role undocumented
- [ ] **Identify 2404HV-deb role** — Ubuntu 24.04 Hyper-V VM, SSH + node-exporter only
- [ ] **Identify DIGIDIOT.local AD usage** — Server 2016 DC running as Hyper-V VM. What's joined? Still needed?
- [ ] **monitor-deb :9221** — unknown service, identify

### DC Decommission Salvage

- [ ] **DC1 authorization follow-up** — Dell N4032F x2, Lambda GPU workstations, Dell Precision 7920
- [ ] **DC1 NEEDS MORE INFO checklist** — work through on next visit (see dc_salvage.md)
- [ ] **Dell R730 pickup** — get CPU model + RAM when collecting
- [ ] **Dell JBOD (4TB SAS)** — confirm chassis/bay count, pair with Dell SAS 12G HBA for TrueNAS
- [ ] **DC2 walkthrough** — schedule and inventory
- [ ] **DC3/DC4 status** — confirm if going down, schedule walkthrough
- [ ] **12U half rack** — retrieve, rack all new DC hardware
- [ ] **Logitech Z-680 sub recap** — Drew to spec capacitor kit (known failure mode)
- [ ] **Dell PowerVault MD1200** — KEEP. 12-bay SAS shelf. Pairs with SAS HBA for TrueNAS expansion. Retrieve when collecting other DC hardware.
- [ ] **Dell PowerEdge R750** — check CPU/RAM/drives/PCIe cards. Potentially TrueNAS rebuild target or new Proxmox node.
- [ ] **DLI IP Power Switches (x2)** — KEEP. Get model numbers. Useful for remote power cycling.
- [ ] **Dell M630 blades** — pull model + service tag. DDR4 ECC RDIMM + E5-2600 v3/v4 CPUs have resale value. Check 2.5" drives in each blade.
- [ ] **Synology RS810RP+** — pass. Too old (Atom D510, DSM EOL). Donate/scrap.
- [ ] **Hitachi AMS2100** — pass on controllers. Alex to decide on Cheetah drives before disposal.
- [ ] **Dell M1000e chassis** — pass. Too power-hungry for homelab. Scrap/sell.
- [ ] **Polycom conference gear** — resale. Get model numbers, list on eBay/Marketplace.

**DC Salvage Scavenge Checklist — what to grab on every visit:**

Priority 1 — Pull every one found:
- Any **32GB DDR4 UDIMM** (Crucial, Kingston, Corsair, G.Skill — non-ECC, unbuffered)
- Any **16GB DDR4 UDIMM** (already have 10, more is fine)
- **LSI 9211-8i, 9207-8i, IBM M1015, Dell PERC H200** — TrueNAS HBA (IT mode or flashable)
- **Intel PCIe NICs** (avoid Realtek)

Priority 2 — Note specs, photograph:
- **R750 contents** — CPU, RAM type/amount, drives, PCIe cards
- Any **NVMe drives** (U.2 or M.2)
- Any **2.5" or 3.5" SSDs**
- **10GbE NICs** (Intel X540, X550, Mellanox ConnectX-3/4)

Priority 3 — Photograph, flag for Alex:
- Any **SAS drives 1TB+** (MD1200 candidates)
- Any **SAS HBAs** (even IR mode — some flashable)

### RAM Upgrade Targets — Scavenge / Shop

State as of 2026-07-02:

| Node | Current | Grail Target | Needed |
|---|---|---|---|
| shardik | 32GB (4×8GB DDR4-2400) | 128GB (4×32GB DDR4 UDIMM) | 4×32GB — 2 Crucial CT32G4DFD832A in hand, 2 more machines to check |
| aslan | ✅ 64GB (4×16GB) — COMPLETE 2026-07-02 | 128GB (4×32GB DDR4 UDIMM) | 4×32GB — scavenging DC2/DC3 |
| maturin | 32GB (4×8GB) | 64GB (maxed) | 4×16GB UDIMM — 10×16GB DDR4-2400 UDIMM found at DC 2026-07-02 |
| blaine | 32GB (4×8GB DDR3-1333) — confirmed 2026-07-02 | 32GB | ✅ sufficient (DDR3, Sandy Bridge — no upgrade path worth pursuing) |

⚠️ **DC server RAM = DDR4/DDR5 RDIMM ECC — NOT compatible with AM4 consumer boards.** Only workstation/desktop DDR4 UDIMM non-ECC works.

**Found 2026-07-02 at DC:**
- 10×16GB DDR4-2400 UDIMM (part: 16GF2X16QFHH36-135-K) — assign 4→maturin (maxes it), 4→shardik (interim upgrade), 2 spare
- 2×32GB DDR4-3200 UDIMM Crucial CT32G4DFD832A — holy grail sticks. 2 more DC machines to check.
- 8×32GB DDR5 ECC RDIMM SK Hynix (Supermicro) — incompatible with all current nodes. **Sell.**
- 2×32GB DDR4-2933 RDIMM OWC Mac Pro (already in pve3) — RDIMM, not usable in AM4 nodes.

- [ ] **Scavenge 2 remaining DC machines** — pull all 32GB DDR4 UDIMM sticks found. Need 6 more for grail (4 shardik + 4 aslan − 2 in hand).
- [ ] **Install 16GB sticks** — Jordan: 4×16GB→maturin (64GB, maxed), 4×16GB→shardik (64GB interim). Verify compatibility on OptiPlex 7050 first.
- [ ] **Shop (if not found):** 32GB DDR4-3200 UDIMM non-ECC — ~$40-60/stick on eBay. Buy only what DC salvage doesn't cover.

### Hardware Inventory Completion

- [ ] Photo and dmidecode all 5 waiting systems
- [ ] Photo pve3 (ThinkStation offsite)
- [ ] Photo Elegoo Mars 3, Ender 3 V1, Flashforge Dreamer
- [ ] Photo GTX 1080 and GTX 1080 Ti cards
- [ ] Photo all laptops and portable devices
- [ ] SCP all new photos to MkDocs docs/images/hw/
- [ ] Import all hardware into Snipe-IT (192.168.1.53 — plow-rpm)
- [ ] Add 12TB HDD and suspect 20TB HDD to hw_reserve.md (run SMART on both)
- [ ] Document hw_reserve — NICs found, additional RAM found

---

## Sunday Projects
_Large multi-step tasks requiring a 4-hour focused block_

### 1. Pi 2B — Assign Role
**Goal:** Pi 2B (blank-dietpi1-deb, 192.168.1.121) is online — needs a permanent role

- [ ] Check what's currently running (`systemctl list-units --type=service --state=running`)
- [ ] Decide on role (options: Gitea mirror secondary, rsync log relay, MQTT broker)
- [ ] Assign hostname reflecting role, update Ansible inventory
- [ ] Add to MkDocs hosts.md

### 2. TrueNAS Hardware Rebuild ⭐
**Goal:** Replace aging Z77/i5-3570K with temerant hardware (Ryzen 5 1600X, 32GB DDR4, GTX 1080 Ti)
**Blocker:** LSI HBA not yet found — order now if not located

- [ ] Check temerant-win 2x 3TB HDDs (Seagate ST3000DM001) for important data ⚠️
- [ ] Pull mobo, Ryzen 5 1600X, 32GB DDR4, GTX 1080 Ti, 500GB SSD from temerant
- [ ] **Flash M1115 to LSI IT mode** — Jordan to execute. Chris has done this before. Do NOT attach TrueNAS drives before flashing.
- [ ] Order 2x SFF-8087 to SATA breakout cables (~$5-10 each eBay)
- [ ] Install hardware into existing FreeNAS beige full tower
- [ ] Install TrueNAS on 500GB SSD — replace USB boot drives
- [ ] Boot TrueNAS, import TRYAGAIN pool
- [ ] Update mediastack-deb fstab if IP changes
- [ ] Dedupe/find duplicate filenames on TRYAGAIN — fdupes or rdfind (post-rebuild)
- [ ] Delete iocage datasets — Weltgeist and Alea Iacta Est jails (91GB)

### 3. Physical Tidy

- [ ] Tidy desk wires — full shutdown and rewire
- [ ] Sort hardware / find HBA
- [ ] Clean off shelves

### 4. Pi Day — Phase 2
**Goal:** Phase 1 complete (rack installed, 6 Pis running). Phase 2: remaining Pis + cable management.

- [ ] Bring argos-pi4-deb (.127) and argos-pi4-wifi-deb (.128) online
- [ ] Wall-mount argos as HA field station — confirm location with Chris, wire sensors (temp/humidity/PIR)
- [ ] Onboard argos via Ansible (onboard2.yml)
- [ ] PoE switch + PoE HATs — single cable per Pi for power + network
- [ ] Full cable management on rack

### 5. TrueNAS NIC Swap + Boot Test — ✅ RESOLVED 2026-07-03 (unexpected path)
**Goal:** Replace fragile USB NIC with reliable PCIe NIC; confirm Kingston boot mirror

- [ ] **Watch `alc0` for stability over next 1-2 days before fully trusting it** — `alc` driver has a rougher FreeBSD track record than Intel NICs; possible this is why it was originally marked dead (intermittent, not fully broken)
- [ ] hw_inv.md / network_inventory.md — update NIC status for freenas-bsd (done same session, see below)
- [ ] Source/RMA replacement X540-T2 (or equivalent Intel-chipset 10GbE/GbE card) if bench test confirms it's dead — add to shopping list
- [ ] **Jumbo frames on alc0** — backlog, not now. Wait for stability proof first; requires matching MTU on Flint port too. Revisit as separate perf task once alc0 is trusted.

### 6. Shardik PSU Replacement
**Goal:** Replace confirmed-dead PSU — 1-month uptime target starts when she's back online

- [ ] **Shardik down 2026-07-05** — Chris confirmed likely accidental unplug (not a repeat PSU failure). Caught via new backup-dietpi-deb Kuma monitor, recovered before Chris checked (brief). Uptime clock resets again — new target ~2026-08-05 pending confirmation. **No alert fired** — backup Kuma instance has no notification channel wired up yet, ping-only dashboard so far. Follow-up: connect Telegram bot (or equivalent) to backup-dietpi-deb Kuma so this kind of drop actually pages someone next time.

### 7. Network Inventory & Documentation
**Goal:** Full enumeration of all hosts, services, and ports on the homelab network

- [ ] SCP network_inventory.md to git-ansible MkDocs docs
- [ ] Resolve open questions (see network_inventory.md)

### 8. Rack Build + pfSense + VLANs ⭐
**Goal:** APC half rack, Cisco SG200-50 managed switch, pfSense on SG-1100, full VLAN segmentation
**Hardware in hand:** APC 4-post enclosed half rack, Netgate SG-1100, Cisco SG200-50 (confirmed 2026-07-03 — the only layer 2 managed switch we have, no separate Dell unit), Netgear GS116 (currently live, retire on cutover)
**Owner:** Riley (network), Jordan (power/rack), Alex (TrueNAS chassis future)
**Priority note (2026-07-04):** GS116 has had at least one confirmed dead port for ~7 years and is still in daily use (14/16 ports active). Tonight's NIC throughput debugging found a client-specific bottleneck (git-ansible → freenas-bsd capped at ~340-514kB/s raw TCP while restic-deb's path to the same host sustains 24-25MB/s) that couldn't be fully diagnosed because the GS116 is unmanaged — no port stats, no way to inspect further short of physically swapping cables. A switch with one known-dead port after 7 years of continuous use is a reasonable candidate for other ports quietly degrading too. This is a concrete argument to treat the SG200-50 cutover as sooner-than-"someday" — it would also finally give visibility (per-port error/utilization stats) into problems like tonight's that are currently undiagnosable.

**Phase 1 — Pre-flight (no downtime)**
- [ ] Place rack in final location
- [ ] Install SG200-50, patch panel, PDU in rack
- [ ] Set Flint 2 to AP mode while still live on existing network
- [ ] Configure SG-1100 offline (laptop direct to LAN port): WAN, DHCP, DNS relay, VLAN interfaces

**Phase 2 — Cutover (planned outage ~1 hour)**
- [ ] ⚠️ Announce maintenance window — everything goes down briefly
- [ ] Pull WAN ethernet from Flint 2 → plug into SG-1100 WAN port
- [ ] SG-1100 LAN → SG200-50 trunk port
- [ ] Move all cables from GS116 → SG200-50 (correct VLAN per port)
- [ ] Verify internet, verify all VLANs routing, verify firewall rules
- [ ] Rollback: if anything breaks, replug Flint 2 WAN and return to GS116

**Phase 3 — IP migration (full weekend)**
- [ ] ⚠️ All hosts get new IPs — update DHCP reservations by MAC first
- [ ] Update Ansible inventory_auto with new IPs
- [ ] Update MkDocs hosts.md, network_inventory.md
- [ ] Update Proxmox cluster configs (corosync ring addresses)
- [ ] Update all fstab NFS/CIFS mounts with new IPs
- [ ] Update Uptime Kuma monitors
- [ ] Update Homepage dashboard
- [ ] Update Zabbix agent configs

**VLAN scheme:**
- VLAN 10 Servers: 192.168.10.0/24 — Proxmox, TrueNAS, VMs, Docker, Pis
- VLAN 20 Trusted: 192.168.20.0/24 — amontillado, work devices
- VLAN 30 IoT: 192.168.30.0/24 — TVs, Echo, Fire TV, WiFi clients
- VLAN 99 Mgmt: 192.168.99.0/24 — switch UI, pfSense UI (amontillado only)

**Phase 4 — Physical rack (no downtime, ongoing)**
- [ ] Shelf for maturin (OptiPlex SFF) in rack
- [ ] Pi rack into rack
- [ ] TrueNAS rack-mount chassis (tied to TrueNAS rebuild Sunday project)

### 9. VM & Container Placement Audit ⭐
**Goal:** Ensure every VM and LXC is on the optimal hypervisor with right-sized resources
**Owner:** Kai
**Blocker:** Wait for shardik uptime target (2026-08-01) before migrating any prod workloads. No production touching shardik until Aug 1. KASM (111) moved there as stress test only — acceptable. Target will likely be amended again.

- [ ] **Migrate mediastack-deb → shardik** after Jul 28 — currently on aslan (migrated from maturin 2026-07-02 for RAM swap). Shardik is the ultimate destination (Ryzen 7 2700X, tank pool). Wait for 1-month uptime target 2026-07-28.
- [ ] **Right-size VM RAM allocations** across all nodes — audit over/under provisioned VMs
- [ ] **Swarm VMs (102/104/105)** — decide rebuild or decommission. All stopped on aslan.
- [ ] **GPU transcoding** — revisit mediastack on aslan with GTX 1080 Ti passthrough once RAM allows. Casey + Kai.
- [ ] **Manyfold permanent home** — blaine LXC test (CT 103) outperforming docker-deb. Kai to report on LXC results, then decide: keep on blaine or move to dedicated LXC on better node. DO NOT delete CT 103.

### Completed Sunday Projects

---

## Planned Projects

### PVE Cluster — blaine-pve + pve3

- [ ] Add blaine-pve to cluster after Proxmox install (Sunday)
- [ ] **Wednesday Jul 1** — Check SMART results on blaine drives (sda 16TB ~1am, sdb 2TB ~7am Tue, sdc 20TB ~5am Wed). Re-attach to VM 100, relabel, begin STL ACCESSORIES rsync.
- [ ] **Shardik: SMART test** — run short SMART on 4x 6TB drives (sda/sdb/sdc/sdd), results pending.
- [ ] **Shardik: PBS decision** — migrate PBS back to shardik or keep on aslan. Alex + Kai. Sunday.
- [ ] **Red case (ASRock B450M Steel Legend)** — team proposed hostname **garuda** (2026-07-05 meeting, next off the approved 12-name list) — pending Chris sign-off. Role still TBD. Specs: Ryzen 5 1600X, 32GB DDR4-2133, 1TB SSD.
- [ ] **hw_reserve.md** — SCP to git-ansible + git commit + push (updated this session).
- [ ] Configure Tailscale on pve3
- [ ] Full hardware inventory pve3 (dmidecode, photos)
- [ ] Add pve3 to Proxmox cluster (shardik + maturin + aslan + blaine + pve3)
- [ ] Add pve3 to inventory_auto and MkDocs
- [ ] Configure Proxmox HA for automatic VM failover — **sequencing decided 2026-07-05:** hold off until (1) shared storage or ZFS replication exists between nodes (HA can't properly fail over VMs whose disks live on local-only storage), and (2) shardik's "no production workloads until 2026-08-01" uptime lock expires (HA could auto-migrate/restart VMs onto it, violating that lock). Revisit after both are clear.
- [ ] Set up shared storage — NFS from TrueNAS

### Docker Swarm

- [ ] Rebuild swarm01/02/03 (currently stopped)
- [ ] Deploy Traefik in Swarm mode — cluster-wide reverse proxy
- [ ] Deploy Uptime Kuma in Swarm
- [ ] Deploy Homepage dashboard in Swarm
- [ ] Deploy Zabbix frontend in Swarm — monitoring survives node failure
- [ ] Evaluate MkDocs in Swarm

### Monitoring Stack (monitor-deb 192.168.1.29)

- [ ] Add Uptime Kuma to Homepage widget (fix slug)
- [ ] Configure Zabbix → Telegram alerting
- [ ] Deploy Loki for log aggregation
- [ ] Uptime Kuma monitoring of mediastack-deb containers
- [ ] Document full Zabbix topology — server on monitor-deb, 11 agents deployed

### Local AI Assistant (aslan)

- [ ] Deploy Ollama with GTX 1080 Ti GPU passthrough (GPU already bound to vfio-pci on aslan)
- [ ] Deploy Open WebUI
- [ ] Create sysadmin / homelab / casual assistant personalities
- [ ] Add Whisper (STT) and Piper (TTS)
- [ ] Feed MkDocs docs as RAG knowledge base

### PBS — Next Steps

- [ ] Evaluate PBS tape backup to CRU bays on blaine-pve (post-install)

### Mediastack / Plex

- [ ] Add Tautulli — Plex analytics
- [ ] Bazarr — subtitle automation
- [ ] Tdarr — transcoding (needs GPU node first — aslan)
- [ ] Add Plex Music library fix for mobile (Plex Pass confirmed, unresolved)
- [ ] Add Training and Photos libraries to Plex
- [ ] Dual reverse proxy — Caddy + Traefik both on docker-deb. Riley + Casey to resolve.

### RomM / Gaming

- [ ] Complete tactical RPG collections across all supported platforms
- [ ] Deduplicate DS ROMs (Fire Emblem Shadow Dragon appears 3x)
- [ ] Explore LaunchBox ROM archive on NAS — migrate to RomM

### Vaultwarden / Secrets

- [ ] Fix Vaultwarden autofill port matching issue in browser extension
- [ ] Store all service credentials with full URL including port
- [ ] Evaluate HashiCorp Vault for Ansible secrets management

### Home Assistant

- [ ] Phase 1 — backup to TrueNAS, Tailscale
- [ ] Phase 2 — Zigbee, MQTT, ESPHome, Frigate
- [ ] Phase 3 — automations, Music Assistant, OctoPrint
- [ ] Phase 4 — argos-deb wall kiosk

### Network

- [ ] Clarify Flint2 + Netgate topology — document which handles what
- [ ] Evaluate VLANs for IoT/media/server segmentation
- [ ] Unbound — local DNS resolver
- [ ] Authelia — auth layer for exposed services
- [ ] VPN rationalization — Tailscale + WireGuard + ZeroTier all running. Pick one, retire the others.
- [ ] Scan guest WiFi subnet — third LG TV likely there, range unknown

### Documentation

- [ ] Create Proxmox cluster diagram
- [ ] Document monitoring stack architecture
- [ ] Create backup_policy.md — 3-2-1 approach, rotation schedule, STL archive policy
- [ ] hw_inv.md — document ST6000VN0001 Z4D2EJ31 retired, ST6000DX000 Z4D07FQ5 added
- [ ] Update hosts.md with aslan and Beryl AP (192.168.1.10)
- [ ] SCP network_inventory.md to git-ansible MkDocs docs root
- [ ] SCP vlan_ip_plan.md to git-ansible MkDocs docs root
- [ ] SCP site_assets.md to git-ansible MkDocs docs root

### Ansible

- [ ] Pin ansible_python_interpreter per host in inventory_auto
- [ ] Add fail2ban to homelab_baseline.yml
- [ ] Add chrony LXC skip to sync_time.yml
- [ ] Update check_services.yml to reflect current services
- [ ] Update fail2ban.yml — add pause before verify task

### Team Documentation

- [ ] **ED: Create CLAUDE.md for each specialist** — Jordan, Kai, Sam, Riley, Morgan, Alex, Taylor, Casey, Drew — document domain, personality, rules, ownership, escalation paths

### MkDocs / Automation

- [ ] Automate doc updates — push from ED session to git-ansible without manual paste
- [ ] completed.md auto-population — move checked items from todo.md via checkbox_persist.js
- [ ] **Sam: merge-aware todo_sync.sh** — deploy cron on git-ansible that pulls todo.md from amontillado but preserves `[x]` state from Gitea (prevent SCP from wiping web-checked boxes)

---

## Parking Lot (Research Needed — Not Yet Scheduled)

- [ ] **Swarm architecture** — should monitoring stack move to swarm? Evaluate what makes sense
- [ ] **Ceph** — second attempt, needs planning and dedicated hardware evaluation
- [ ] **YouTube channel tech scouting** — Chris to provide channel list
- [ ] **ZeroTier** — currently unconfigured on amontillado. Evaluate vs Tailscale/WireGuard
- [ ] **STL collection page** — evaluate Manyfold (:3214 on docker-deb) first; if it doesn't meet the need, build a custom page similar to vinyl_collection.html. Drew + Sam.
- [ ] **Komga / Mylar** — comics stack running on mediastack. Populate libraries?
- [ ] **Farson VM** — dedicated vuln/pentest VM (Kali or OpenVAS/Greenbone). Taylor to scope: host node, targets, reporting. Just a whim for now.
- [ ] **Sam: general alert relay bot** — extend the patch-notification Telegram bot into a unified relay for Kuma/Zabbix/SMART alerts. Proposed 2026-07-05, pending Chris approval.
- [ ] **Sam: CRU label linter script** — scan all scripts/configs for hardcoded/stale CRU drive labels (cru3 alone has changed 3x). Proposed 2026-07-05, pending Chris approval.
- [ ] **Casey: evaluate request-management app (Overseerr or Wizarr)** for mediastack. Proposed 2026-07-05, pending Chris interest.
