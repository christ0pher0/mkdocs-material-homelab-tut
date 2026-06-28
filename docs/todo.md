# Homelab Todo & Roadmap
_Last updated: 2026-06-28_
---

## Critical / Security

- [ ] **Shardik PSU** — suspected failure, primary hypervisor — Sunday replacement planned
- [ ] docker-deb static IP or confirmed DHCP reservation — hosts Vaultwarden, Traefik, Portainer ⚠️
- [ ] Disk space alerts — amontillado D: (11%), pi1 SD (91%) ⚠️
- [ ] **Telegram bot** — Sam building patch notification bot (weekly_patch.yml results → Telegram after 3am run). Needs token + channel ID from Chris.
- [ ] **docker-deb watchdog** — Sam building script to alert Uptime Kuma if container stack hasn't restarted in >1 week
- [ ] Alert on: drive errors, disk >85%, service down, high temp, RAM pressure
- [ ] sudoers drop-in for docker group auto-add script (per-user, NOPASSWD usermod)
- [ ] Investigate amontillado D: (2.79TB, 11% free) — audit VMs and junk, clear or expand

### Backup Strategy

- [x] STL Non-Fantasy — ✅ COMPLETE 2026-06-28. cru3 now labeled STL_FIGURES. Sync confirmed complete.
- [ ] STL_FIGURES — audit all scripts for hardcoded old label references (cru3 was: STL_Non-Fantasy → STL_#CRUNCH → STL_FIGURES)
- [ ] STL T-Z — cru2 reformatted, rsync running, currently in T (Titan Forge) — monitor to completion
- [ ] Establish offsite drive rotation schedule (Tier 3)
- [ ] Evaluate PBS tape backup to CRU bays (blaine-pve post-install)
- [ ] cru_stats.sh saves to /root/scripts/cru_stats/ (sudo) but backup_drives_update.sh reads ~/scripts/cru_stats/ — fix path mismatch

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
- [ ] Manyfold — Kai testing creator-population fix via LXC on blaine (2026-06-28)
- [ ] **Set Uptime Kuma TrueNAS poll to 30 seconds** — Taylor (USB NIC fragility mitigation)
- [ ] **Check pihole-pi1-deb SD card** — was 91% full 2026-06-21, run `df -h` on pihole-pi1-deb (192.168.1.120)
- [ ] **Confirm which 6 Pis are racked** — update fleet inventory (Drew)
- [ ] **Ender 3 V2 yellow PLA** — run temp tower first to dial in profile before printing anything structural (Drew)
- [ ] **Pi Status page** — build in MkDocs with uploaded Pi photos (Morgan)
- [ ] **Netgate clarification** — confirm model and role in topology (Riley)

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
- [ ] **Order LSI 9207-8i or 9211-8i HBA** (~$20-40 eBay) — blocking item
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
- [x] Start 1-month uptime clock — ✅ started 2026-06-28. Target: 2026-07-28.

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

- [x] Add blaine-pve to cluster after Proxmox install (Sunday)
- [ ] Configure Tailscale on pve3
- [ ] Full hardware inventory pve3 (dmidecode, photos)
- [ ] Add pve3 to Proxmox cluster (shardik + maturin + aslan + blaine + pve3)
- [ ] Add pve3 to inventory_auto and MkDocs
- [ ] Configure Proxmox HA for automatic VM failover
- [ ] Set up shared storage — NFS from TrueNAS

### Docker Swarm

- [x] Migrate swarm01 (102) from shardik to aslan
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
- [ ] Kometa — verify Trakt/MDBList working after next run
- [ ] Add Plex Music library fix for mobile (Plex Pass confirmed, unresolved)
- [ ] Add Training and Photos libraries to Plex
- [ ] FlareSolverr redeployment + Prowlarr integration (post mediastack-deb rebuild)

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

### Documentation

- [ ] Create Proxmox cluster diagram
- [ ] Document monitoring stack architecture
- [ ] Create backup_policy.md — 3-2-1 approach, rotation schedule, STL archive policy
- [ ] hw_inv.md — document ST6000VN0001 Z4D2EJ31 retired, ST6000DX000 Z4D07FQ5 added
- [ ] Update hosts.md with aslan and Beryl AP (192.168.1.10)

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
- [ ] **YouTube channel tech scouting** — Chris to provide channel list, 
