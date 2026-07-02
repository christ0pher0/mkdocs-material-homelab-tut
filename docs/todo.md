# Homelab Todo & Roadmap
_Last updated: 2026-07-02 (Shardik ZFS RAIDZ1 tank pool created, aslan RAM upgraded to 64GB, mediastack-deb migrated maturin→aslan, DC salvage checklist added, RAM finds logged)_
---

## Critical / Security

- [x] **Shardik PSU** — ✅ COMPLETE 2026-06-28. PSU replaced, CMOS battery replaced, cluster quorate.
- [x] **Shardik RAM** — ✅ COMPLETE 2026-06-29. Bad PNY XLR8 16GB (2x) replaced with Ballistix 16GB + 3x Micron 8GB DDR4-2666 (40GB total). stress-ng 30min passed. Root cause of all historical instability and ZFS corruption confirmed.
- [ ] docker-deb static IP or confirmed DHCP reservation — hosts Vaultwarden, Traefik, Portainer ⚠️
- [ ] Disk space alerts — amontillado C: (7% free ⚠️), pi1 SD (91%) ⚠️
- [ ] **amontillado C: drive** — 65.9GB free of 930GB (7%). Jordan to audit what's consuming it
- [ ] **Telegram bot** — Sam building patch notification bot (weekly_patch.yml results → Telegram after 3am run). Needs token + channel ID from Chris.
- [ ] **docker-deb watchdog** — Sam building script to alert Uptime Kuma if container stack hasn't restarted in >1 week
- [ ] Alert on: drive errors, disk >85%, service down, high temp, RAM pressure
- [ ] Investigate amontillado D: (2.79TB, 11% free) — audit VMs and junk, clear or expand
- [ ] **VPN rationalization** — 3 VPN solutions running (Tailscale, WireGuard on mediastack, ZeroTier on amontillado). Riley to pick one and decommission the others

### Backup Strategy

- [x] STL Non-Fantasy — ✅ COMPLETE 2026-06-28. cru3 now labeled STL_FIGURES. Sync confirmed complete.
- [ ] STL_FIGURES — audit all scripts for hardcoded old label references (cru3 was: STL_Non-Fantasy → STL_#CRUNCH → STL_FIGURES)
- [x] STL T-Z — ✅ COMPLETE 2026-06-29. Rsync complete, SMART ✅, backup_drives.md updated.
- [ ] STL ACCESSORIES (732G) — assign to sda (16TB). SMART ✅ 2026-07-02. Re-attach to blaine, relabel, start rsync.
- [ ] TERRAIN (446G) — assign to sdb (2TB). SMART ✅ 2026-07-02. Re-attach to blaine, relabel, start rsync.
- [ ] SOURCE_MATERIAL (1.4T) — no drive assigned. Inventory available drives first, then assign. On hold.
- [ ] sdc (20TB) — pulled from CRU rotation 2026-07-02. Relabel as spare. Shelf it — quick pivot if TRYAGAIN needs emergency replacement. History: prior anxious behavior in TrueNAS, passed SMART 2026-07-02.
- [ ] **Logitech sub recap** — caps blown on subwoofer, lab running 1 speaker. Drew to spec recap kit. Revisit Sunday.
- [ ] Establish offsite drive rotation schedule (Tier 3)
- [ ] Evaluate PBS tape backup to CRU bays (blaine-pve post-install)
- [ ] cru_stats.sh saves to /root/scripts/cru_stats/ (sudo) but backup_drives_update.sh reads ~/scripts/cru_stats/ — fix path mismatch

---

## This Week — Assigned

- [ ] **Jordan: amontillado C: drive audit** — 7% free, find what's consuming it. `WinDirStat` or `du` via WSL
- [ ] **Jordan: pihole-pi1-deb SD card** — 91% full, swap with replacement SD in reserve before it fails silently
- [ ] **Jordan: fail2ban rollout** — run fail2ban.yml across all SSH-exposed hosts via Ansible
- [ ] **Kai: KASM disk move** — migrate VM 111 disk from SDA_store (spinning rust) to local-lvm (NVMe) on aslan
- [ ] **Kai: swarm01 migration** — migrate VM 102 from shardik to aslan, then bring up 104 + 105, deploy Traefik in swarm mode
- [ ] **Sam: cru_stats path fix** — align cru_stats.sh and backup_drives_update.sh to same path. Alex to sign off first.
- [ ] **Sam: Telegram bot** — weekly_patch.yml results → Telegram channel after 3am Sunday run. Needs token + channel ID from Chris
- [ ] **Sam: auto network_inventory.md** — script combining arp-scan + masscan + ansible facts → outputs fresh network_inventory.md. Replaces manual scans.
- [ ] **Sam: expand cru_plexfolder_stats.sh** — add TrueNAS Libraries section (Movies, TV, Music, AudioBooksPlex, Books_Author, Comics) with du -sh per folder. Draft ready for Sunday meeting.
- [ ] **Sam: refactor backup_drives_update.sh** — use Gitea API instead of local mkdocs clone on restic-deb. Eliminate git conflicts between restic-deb and git-ansible. Top priority.
- [ ] **Sam: auto backup date in cru_stats** — write `Backup: <date>` to stats file when SMART passes. update_drives_table.py to read and update Backup column automatically.
- [ ] **Sam + Kai: CRU hotplug automation** — cru_mount_vm.sh to handle qm set attach/detach automatically on drive swap. VM should start without CRU drives. Working solution by Sunday.
- [ ] **Kai: pve3 Tailscale clustering** — spec corosync over Tailscale, WAN timeout tuning, cold/warm failover runbook. Sunday meeting deliverable.
- [ ] **Kai: formal warning** — CRU passthrough implemented as static VM config instead of hotplug per spec. One more significant miss = PIP.
- [ ] **Jordan: git identity on restic-deb** — set user.email and user.name globally so commits don't fail.
- [x] **Jordan: clean up inventory_auto** — ✅ COMPLETE 2026-07-01. Stale pi# names removed, idee-deb removed (now aslan), linux_skip group added for batocera/retropi. 4 stale inventory files deleted (inventory, inventory1, inventory2, inventory_web). inventory_auto is sole source of truth.
- [x] **Jordan: move /etc/hosts push + SSH key sync to homelab_baseline.yml** — ✅ COMPLETE 2026-06-30. Both tasks added to homelab_baseline.yml. Fleet run: 18 hosts, 0 failures.
- [ ] **Jordan: BIOS download links** — Jordan to find and provide direct download links for Chris to apply. Current status per dmidecode 2026-07-02:
  - shardik (ASRock AB350M Pro4): P10.43 Jun 2025 — https://www.asrock.com/mb/AMD/AB350M%20Pro4/index.asp#BIOS
  - maturin (Dell OptiPlex 7050): 1.27.0 Sep 2023 — https://www.dell.com/support/product-details/en-us/product/optiplex-7050-desktop/drivers — appears current, confirm ✅
  - aslan (Gigabyte AB350-Gaming 3-CF): F50a Nov 2019 — https://www.gigabyte.com/Motherboard/GA-AB350-Gaming-3-rev-1x/support#support-dl-bios — F52 available ⚠️
  - blaine (Gigabyte GA-Z77-DS3H): F8 Aug 2012 — Rev 1.0: https://www.gigabyte.com/Motherboard/GA-Z77-DS3H-rev-10/support | Rev 1.1: https://www.gigabyte.com/Motherboard/GA-Z77-DS3H-rev-11/support — physical inspection required to confirm revision before flashing
- [x] **Jordan: microcode patch verification** — ✅ COMPLETE 2026-07-02. shardik (amd64-microcode) and maturin (intel-microcode) were missing — installed and activated via reboot. blaine and aslan were already current. maturin also missing non-free-firmware repo — added via sed to sources.list.
- [ ] **Jordan: add microcode + non-free-firmware to homelab_baseline.yml** — ensure amd64-microcode/intel-microcode installed on all Debian nodes based on CPU vendor, and non-free-firmware repo present. Prevents future drift.
- [ ] **Jordan: onboard pbs-deb** — run onboard2.yml, confirm passwordless sudo and SSH key auth working.
- [ ] **Jordan: octopi-pi4-deb SSH key auth** — confirm key auth works after baseline run; if not, run onboard2.yml individually.
- [x] **Jordan: run homelab_baseline.yml against plow-rpm** — ✅ COMPLETE 2026-07-01. Rocky BaseOS/AppStream repos added, git/vim/curl installed, baselined ok=16.
- [ ] **Jordan: blaine sdc SMART long test** — started ~2026-06-29. Expected completion ~Wed Jul 1 5am. Check results, relabel, attach to VM 100 for STL rsync.
- [ ] **Jordan: add Zabbix repo task to homelab_baseline.yml** — restic-deb had no Zabbix repo, agent2 install failed. Add repo setup task before agent install. Sam to implement.
- [ ] **Jordan: fix SSH service name for DietPi hosts** — baseline uses 'ssh' service name but DietPi uses dropbear. Add conditional or ignore for DietPi hosts.
- [ ] **Jordan: fix ansible_facts deprecation warnings** — update homelab_baseline.yml to use ansible_facts["fact_name"] syntax before ansible-core 2.24 drops support. Sam to implement.
- [ ] **Riley: DHCP reservation for octopi-pi4-deb** — lock to 192.168.1.122 on router to prevent drift.
- [ ] **Jordan: document mkdocs_dev_material on restic-deb** — note it lives there intentionally (required by backup_drives_update.sh until Sam refactors).
- [ ] **Riley: pve3 Tailscale setup** — configure Tailscale on ThinkStation offsite node.
- [ ] **Morgan: session documentation** — shardik recovery runbook, red case inventory page, PBS migration decision log, pve3 DR node page. First active assignment.
- [ ] **Morgan: cluster capacity page** — MkDocs page showing each node: mobo, CPU, current RAM, max RAM, slot config, current VM/CT placement and allocation, upgrade path. Reference before every hardware decision. Kai provides VM data, Jordan provides dmidecode, Morgan builds the page.
- [ ] **Morgan: hardware target state page** — MkDocs page documenting where the homelab is headed: desired node specs, RAM targets, storage goals, network end state, hardware to acquire. Living document — updated as decisions are made. ED owns content, Morgan owns structure.
- [ ] **Morgan + Riley: MkDocs Network section overhaul** — create dedicated Network section in nav. Move network_inventory.md, network_diagram.md, hosts.md here. Add vlan_design.md. Riley owns content accuracy, Morgan owns structure and nav.
- [ ] **Sam: add -tree flag to cru_plexfolder_stats.sh** — dumps per-creator folder sizes for a given drive label (e.g. `--tree STL_#-B`). Run weekly via cron, save output, `--view` returns instant results. Draft ready for Sunday meeting.

---

## Immediate Maintenance (Sysadmin)

- [ ] **Patch all hosts** — weekly_patch.yml runs Sundays 3am (automated). Manual run if urgent.
- [x] **Reboot docker-deb** — ✅ COMPLETE 2026-06-28. Kernel current. Static IP still needed.
- [x] Update Portainer — ✅ COMPLETE 2026-06-28
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
- [ ] swarm01 (102) — pending migration from shardik to aslan
- [ ] **Confirm swarm VM status** — 102/104/105 all showing STOPPED on aslan. Intentional or not? ⚠️
- [ ] KASM (111) — move disk from SDA_store to local-lvm NVMe on aslan for performance
- [ ] onboard pbs-deb via Ansible (onboard_host.yml not yet run — passwordless sudo added manually)
- [ ] **Manyfold** — remove from docker-deb :3214 (poor performance). blaine LXC (CT 103) is the candidate — promising results. Kai to complete evaluation and confirm as permanent home before go-live.
- [ ] **Set Uptime Kuma TrueNAS poll to 30 seconds** — Taylor (USB NIC fragility mitigation)
- [ ] **Check pihole-pi1-deb SD card** — was 91% full 2026-06-21, run `df -h` on pihole-pi1-deb (192.168.1.120)
- [x] **Confirm which 6 Pis are racked** — ✅ COMPLETE 2026-06-30. All 6 slots documented: ha-net, blank-dietpi-deb, backup-dietpi-deb, retropi, batocera-deb, pihole-pi-deb. hw_inv.md updated.
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

- [x] **DC1 survey** — ✅ COMPLETE 2026-06-30. All rooms inventoried. dc_salvage.md created.
- [ ] **DC1 authorization follow-up** — Dell N4032F x2, Lambda GPU workstations, Dell Precision 7920
- [ ] **DC1 NEEDS MORE INFO checklist** — work through on next visit (see dc_salvage.md)
- [ ] **Dell R730 pickup** — get CPU model + RAM when collecting
- [ ] **Dell JBOD (4TB SAS)** — confirm chassis/bay count, pair with Dell SAS 12G HBA for TrueNAS
- [ ] **DC2 walkthrough** — schedule and inventory
- [ ] **DC3/DC4 status** — confirm if going down, schedule walkthrough
- [ ] **Cisco SG200-50** — retrieve, use for VLAN project (solves switch gap)
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
- [x] **Execute RAM swap** — ✅ COMPLETE 2026-07-02. Aslan upgraded to 64GB (2x Ballistix from shardik + 2x SK Hynix from maturin). Maturin back to 4×8GB. Shardik down to 32GB (4×8GB).
- [x] **Confirm blaine RAM** — ✅ COMPLETE 2026-07-02. 32GB DDR3-1333 (4×8GB). i5-2500K Sandy Bridge — DDR3 only, no meaningful upgrade path.

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
- [x] **HBA found** — ✅ IBM ServeRAID M1115 (LSI 2008 chip) located 2026-07-01. Needs cross-flash to IT mode before use.
- [ ] **Flash M1115 to LSI IT mode** — Jordan to execute. Chris has done this before. Do NOT attach TrueNAS drives before flashing.
- [ ] Order 2x SFF-8087 to SATA breakout cables (~$5-10 each eBay)
- [ ] Install hardware into existing FreeNAS beige full tower
- [ ] Install TrueNAS on 500GB SSD — replace USB boot drives
- [ ] Boot TrueNAS, import TRYAGAIN pool
- [x] Reconfigure SMB shares, cifs1 user, services — ✅ COMPLETE 2026-06-28
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

### 5. TrueNAS NIC Swap + Boot Test
**Goal:** Replace fragile USB NIC with Intel X540-T2 PCIe card; confirm Kingston boot mirror

- [ ] Shut down TrueNAS gracefully
- [ ] Install Intel X540-T2 into primary PCIe x16 slot
- [ ] Remove SanDisk USB — boot from Kingston only to confirm mirror works
- [ ] Re-insert SanDisk — confirm both da0 and da1 still in mirror (`zpool status boot-pool`)
- [ ] Boot TrueNAS — confirm X540-T2 detected (`pciconf -lv | grep ix`)
- [ ] Assign static IP 192.168.1.5 to new interface in TrueNAS UI (Network → Interfaces)
- [ ] Remove/disable old USB NIC (ue0) interface
- [ ] Confirm CIFS/NFS mounts come back on client machines

### 6. Shardik PSU Replacement
**Goal:** Replace confirmed-dead PSU — 1-month uptime target starts when she's back online

- [x] **Replace PSU** — ✅ COMPLETE 2026-06-28
- [x] Verify all VMs stable after swap — ✅ COMPLETE 2026-06-28. Cluster quorate, 4 nodes.
- [x] Start 1-month uptime clock — ✅ restarted 2026-07-02 after microcode reboot. Target: 2026-08-01.

### 7. Network Inventory & Documentation
**Goal:** Full enumeration of all hosts, services, and ports on the homelab network

- [x] arp-scan 192.168.1.0/24 — ✅ COMPLETE 2026-06-28. 30 hosts.
- [x] nmap -sV full subnet — ✅ COMPLETE 2026-06-28. All services identified.
- [x] masscan -p1-65535 full subnet — ✅ COMPLETE 2026-06-28. 177 open ports found.
- [x] docker ps on docker-deb and mediastack-deb — ✅ COMPLETE 2026-06-28.
- [x] qm/pct list on all Proxmox nodes — ✅ COMPLETE 2026-06-28.
- [x] Hyper-V VM inventory from amontillado — ✅ COMPLETE 2026-06-28.
- [x] network_inventory.md created — ✅ COMPLETE 2026-06-28.

- [ ] SCP network_inventory.md to git-ansible MkDocs docs
- [ ] Resolve open questions (see network_inventory.md)

### 8. Rack Build + pfSense + VLANs ⭐
**Goal:** APC half rack, Dell managed switch, pfSense on SG-1100, full VLAN segmentation
**Hardware in hand:** APC 4-post enclosed half rack, Netgate SG-1100, Dell managed switch (model TBD), Netgear GS116 (retire)
**Owner:** Riley (network), Jordan (power/rack), Alex (TrueNAS chassis future)

**Phase 1 — Pre-flight (no downtime)**
- [ ] Identify Dell switch model — confirm 802.1Q VLAN support and port count
- [ ] Place rack in final location
- [ ] Install Dell switch, patch panel, PDU in rack
- [ ] Set Flint 2 to AP mode while still live on existing network
- [ ] Configure SG-1100 offline (laptop direct to LAN port): WAN, DHCP, DNS relay, VLAN interfaces
- [ ] Configure Dell switch offline: VLAN 10/20/30/99, trunk port to SG-1100, access ports per device

**Phase 2 — Cutover (planned outage ~1 hour)**
- [ ] ⚠️ Announce maintenance window — everything goes down briefly
- [ ] Pull WAN ethernet from Flint 2 → plug into SG-1100 WAN port
- [ ] SG-1100 LAN → Dell switch trunk port
- [ ] Move all cables from GS116 → Dell switch (correct VLAN per port)
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
- [x] **Fix root SSH git-ansible → blaine** — ✅ COMPLETE 2026-07-02. Added cos public key to root authorized_keys, set PermitRootLogin prohibit-password, sshd restarted. Confirmed working.
- [ ] **GPU transcoding** — revisit mediastack on aslan with GTX 1080 Ti passthrough once RAM allows. Casey + Kai.
- [ ] **kasm-2404-deb (111)** — move disk from SDA_store → local-lvm NVMe, then start.
- [ ] **Manyfold permanent home** — blaine LXC test (CT 103) outperforming docker-deb. Kai to report on LXC results, then decide: keep on blaine or move to dedicated LXC on better node. DO NOT delete CT 103.

### Completed Sunday Projects
- [x] restic-deb → blaine-pve — ✅ COMPLETE 2026-06-22. Blaine joined cluster, onboarded via onboard2.yml. restic-deb rebuilt as VM on blaine.
- [x] Pi rack Phase 1 — ✅ COMPLETE 2026-06-28. 6 Pis mounted and running. Batocera off-rack.
- [x] Shardik hardware upgrade (CPU 2700X, RAM to 64GB) — ✅ COMPLETE 2026-06
- [x] Router/AP rewire — ✅ COMPLETE
- [x] Beryl AP setup (GL-MT3000, AP mode, 192.168.1.10) — ✅ COMPLETE 2026-06-15
- [x] idee-deb → aslan Proxmox hypervisor — ✅ COMPLETE 2026-06-16
- [x] TrueNAS boot-pool mirror — ✅ COMPLETE 2026-06-28. da0 (SanDisk) + da1 (Kingston), bootloader written, scrub clean.

---

## Planned Projects

### PVE Cluster — blaine-pve + pve3

- [ ] Add blaine-pve to cluster after Proxmox install (Sunday)
- [ ] **Wednesday Jul 1** — Check SMART results on blaine drives (sda 16TB ~1am, sdb 2TB ~7am Tue, sdc 20TB ~5am Wed). Re-attach to VM 100, relabel, begin STL ACCESSORIES rsync.
- [ ] **Shardik: SMART test** — run short SMART on 4x 6TB drives (sda/sdb/sdc/sdd), results pending.
- [ ] **Shardik: PBS decision** — migrate PBS back to shardik or keep on aslan. Alex + Kai. Sunday.
- [x] **Shardik: ZFS pool** — ✅ COMPLETE 2026-07-02. RAIDZ1 "tank" pool created on 4×5.5TB HDDs (sda/sdb/sdc/sdd, ashift=12). 15.7TB usable. pvesm added as tank-storage. Survives reboot with auto-import.
- [ ] **Red case (ASRock B450M Steel Legend)** — hostname and role TBD. Sunday team discussion. Specs: Ryzen 5 1600X, 32GB DDR4-2133, 1TB SSD.
- [ ] **hw_reserve.md** — SCP to git-ansible + git commit + push (updated this session).
- [ ] Configure Tailscale on pve3
- [ ] Full hardware inventory pve3 (dmidecode, photos)
- [ ] Add pve3 to Proxmox cluster (shardik + maturin + aslan + blaine + pve3)
- [ ] Add pve3 to inventory_auto and MkDocs
- [ ] Configure Proxmox HA for automatic VM failover
- [ ] Set up shared storage — NFS from TrueNAS

### Docker Swarm

- [ ] Migrate swarm01 (102) from shardik to aslan
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
- [x] Kometa — ✅ running on mediastack-deb
- [ ] Add Plex Music library fix for mobile (Plex Pass confirmed, unresolved)
- [ ] Add Training and Photos libraries to Plex
- [x] FlareSolverr redeployment — ✅ COMPLETE (running on mediastack-deb :8191)
- [x] Prowlarr integration — ✅ COMPLETE (running on mediastack-deb :9696)
- [x] Audiobookshelf — ✅ installed, running on mediastack-deb :13378
- [x] RomM — ✅ installed, running on mediastack-deb :8998
- [x] Jellyfin — ✅ installed, running on tools-deb/ha-pi4-net :8096
- [x] Tube Archivist — ✅ installed, running on docker-deb :8090
- [x] Manyfold — ✅ installed, running on docker-deb :3214
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
