# Homelab Todo & Roadmap
_Last updated: 2026-05-18_

---

## Critical / Security
- [ ] ZFS plugin — monitor RAIDZ1 health, drive errors on TrueNAS ⚠️
- [ ] Disk space alerts — eld D: (10%), amontillado D: (11%), pi1 SD (91%) ⚠️
- [ ] **Telegram alerts** — bot notifications when something looks wrong
- [ ] Alert on: drive errors, disk >85%, service down, high temp, RAM pressure
- [ ] sudoers drop-in for docker group auto-add script (per-user, NOPASSWD usermod)

### Backup Strategy (restic-deb)
- [ ] Configure 2x CRU bays on restic-deb for rotating manual drives (Tier 2)
- [ ] Establish offsite drive rotation schedule (Tier 3)
- [ ] Expand backup coverage — currently only Patreon O-Z backed up, A-N missing
- [ ] Expand restic-deb storage — 3TB internal nearly full (10% free)
- [ ] Upgrade restic-deb RAM to 32GB DDR3 — found 1x8GB stick, need 3 more

---

## In Progress
- [ ] Inventory 5 remaining waiting systems — match hardware to roles
- [ ] Inventory pve3 (ThinkStation offsite) — specs, storage, role
- [ ] Purchase Hologram.io SIM for argos-deb LTE
- [ ] Purchase larger SD card for pi1-deb (3.8GB, 91% full)
- [ ] Pi rack — 3D print or buy, house all 8 Pis cleanly
- [ ] PoE switch + PoE HATs — single cable per Pi for power + network
- [ ] Shrink maturin pve-data pool — only cloudinit template remains on local-lvm

### Hardware Inventory Completion
- [ ] Photo and dmidecode all 5 waiting systems
- [ ] Photo pve3 (ThinkStation offsite)
- [ ] Photo Elegoo Mars 3 resin printer
- [ ] Photo Creality Ender 3 V1
- [ ] Photo Flashforge Dreamer
- [ ] Photo GTX 1080 and GTX 1080 Ti cards
- [ ] Photo all laptops
- [ ] SCP all new photos to MkDocs docs/images/hw/
- [ ] Import all hardware into Snipe-IT (192.168.1.53)
- [ ] Push completed hw_inventory.md to MkDocs

---

## Planned Projects

### PVE3 — temerant → Proxmox node 3
- [ ] Check temerant-win 2x 3TB HDDs (Seagate ST3000DM001) for important data ⚠️
- [ ] Pull drives, wipe Windows, install Proxmox VE
- [ ] Add to wheel cluster (shardik + maturin)
- [ ] Configure Tailscale on pve3
- [ ] Add to inventory_auto and MkDocs
- [ ] Eventually: GPU passthrough of GTX 1080 Ti for RPCS3/AI workloads
- [ ] Check AB350 IOMMU groupings before passthrough attempt

### Maturin Hardware
- [ ] Investigate VM 112 leftover disk on shardik NVMe (164GB orphan)

### Docker Swarm — Good Candidates
- [ ] Rebuild swarm01/02/03 (currently stopped)
- [ ] Deploy Traefik in Swarm mode — cluster-wide reverse proxy
- [ ] Deploy Uptime Kuma in Swarm
- [ ] Deploy Homepage dashboard in Swarm
- [ ] Deploy Zabbix frontend in Swarm — monitoring survives node failure
- [ ] Evaluate MkDocs in Swarm (or keep co-located with Gitea on git-ansible)
- [ ] Decide: Docker Swarm vs k8s

### Monitoring Stack (monitor-deb 192.168.1.29)
- [ ] Add Uptime Kuma to Homepage widget (fix slug)
- [ ] Configure Zabbix → Telegram alerting
- [ ] Deploy Loki for log aggregation
- [ ] Uptime Kuma monitoring of mediastack-deb containers (via Kuma agent)

### TrueNAS Hardware Rebuild ⭐
- [ ] Check temerant-win 2x 3TB HDDs for important data before touching hardware
- [ ] Pull mobo, Ryzen 5 1600X, 32GB DDR4, GTX 1080 Ti, 500GB SSD from temerant
- [ ] Install into existing FreeNAS beige full tower
- [ ] Order LSI 9207-8i or 9211-8i HBA card (~$20-40 eBay)
- [ ] Order 2x SFF-8087 to SATA breakout cables (~$5-10 each eBay)
- [ ] Install TrueNAS on 500GB SSD — no more USB boot drives
- [ ] Boot TrueNAS, import TRYAGAIN pool
- [ ] Reconfigure SMB shares, cifs1 user, services
- [ ] Update mediastack-deb fstab if IP changes

### TrueNAS — Current State
- [ ] Set ue0 (USB NIC) to static 192.168.1.5 — survives reboots
- [ ] Fix alc0 onboard NIC
- [ ] Add second USB boot drive to freenas-boot mirror (da0 dead)
- [ ] **Order 20TB CMR replacement drive for ada4 (FAULTED, 57 read errors) — target June 1** ⚠️
- [ ] Replace ada4 in TRYAGAIN RAIDZ1 pool once drive arrives
- [ ] Dedupe/find duplicate filenames on TRYAGAIN pool — fdupes or rdfind (wait until pool healthy)
- [ ] Delete iocage datasets — Weltgeist and Alea Iacta Est jails (91GB)
- [ ] Explore LaunchBox ROM archive on NAS — migrate to RomM

### RomM / Gaming
- [ ] Complete tactical RPG collections across all supported platforms
- [ ] Deduplicate DS ROMs (Fire Emblem Shadow Dragon appears 3x)

### Mediastack / Plex
- [ ] Kometa — verify Trakt/MDBList working after next run
- [ ] Add Tautulli — Plex analytics
- [ ] Bazarr — subtitle automation
- [ ] Tdarr — transcoding (needs GPU node first)
- [ ] Add Plex Music library fix for mobile (Plex Pass confirmed, unresolved)
- [ ] Add Training and Photos libraries to Plex
- [ ] FlareSolverr redeployment + Prowlarr integration (post mediastack-deb rebuild)

### Proxmox Cluster
- [ ] Add pve3 (temerant → ThinkStation) to cluster
- [ ] Configure Proxmox HA for automatic VM failover
- [ ] Set up shared storage — NFS from TrueNAS

### PBS — Next Steps
- [ ] Mirror PBS backups to restic-deb
- [ ] Evaluate PBS tape backup to CRU bays

### Local AI Assistant
- [ ] Deploy Ollama on idee-deb (GPU node) with GTX 1080 Ti passthrough
- [ ] Deploy Open WebUI
- [ ] Create sysadmin / homelab / casual assistant personalities
- [ ] Add Whisper (STT) and Piper (TTS)
- [ ] Feed MkDocs docs as RAG knowledge base

### Vaultwarden / Secrets
- [ ] Fix Vaultwarden autofill port matching issue in browser extension
- [ ] Store all service credentials with full URL including port
- [ ] Evaluate HashiCorp Vault for Ansible secrets management

### Home Assistant
- [ ] Phase 1 — backup to TrueNAS, Tailscale
- [ ] Phase 2 — Zigbee, MQTT, ESPHome, Frigate
- [ ] Phase 3 — automations, Music Assistant, OctoPrint
- [ ] Phase 4 — argos-deb wall kiosk

### Documentation
- [ ] Create Proxmox cluster diagram
- [ ] Document monitoring stack architecture
- [ ] hw_inv.md update — ST6000VN0001 Z4D2EJ31 retired, ST6000DX000 Z4D07FQ5 added as SDD_store/PBS datastore

### Network
- [ ] Clarify Flint2 + Netgate topology
- [ ] Evaluate VLANs for IoT/media/server segmentation
- [ ] Unbound — local DNS resolver
- [ ] Authelia — auth layer for exposed services

### Ansible
- [ ] Pin ansible_python_interpreter per host in inventory_auto
- [ ] Add fail2ban to homelab_baseline.yml
- [ ] Add chrony LXC skip to sync_time.yml
- [ ] Update check_services.yml to reflect current services
- [ ] Update fail2ban.yml — add pause before verify task

### MkDocs / Checkbox
- [ ] completed.md auto-population — move checked items from todo.md to completed.md via checkbox_persist.js

---

## Mediastack — Current Stack
| App | Port | Status |
|---|---|---|
| Sonarr | 8989 | ✅ Running |
| Radarr | 7878 | ✅ Running |
| Lidarr | 8686 | ✅ Running |
| Mylar3 | 8091 | ✅ Running |
| SABnzbd | 8090 | ✅ Running |
| Prowlarr | 9696 | ✅ Running |
| Seerr | 5055 | ✅ Running |
| Komga | 8085 | ✅ Running |
| Audiobookshelf | 13378 | ✅ Running |
| RomM | 8998 | ✅ Running |
| Kometa | — | ✅ Running |
| Gluetun VPN | — | ✅ Running |
| qBittorrent | 8082 | ✅ Running |
| Unpackerr | — | ✅ Running |
| FlareSolverr | 8191 | ✅ Running |
| MariaDB | — | ✅ Running |
| Plex | 32400 | ✅ Running |

---

## Maintenance Backlog
- [x] Clarify MariaDB and nginx role on git-ansible-deb
- [x] Confirm git-ansible physical host specs with dmidecode
- [ ] Inventory offsite ThinkStation (pve3)
- [ ] Add pve3 to Tailscale and Ansible inventory
- [ ] Remove snipeit-deb from all docs (LXC destroyed 2026-05-10)
- [ ] Remove grafana-docker-deb, ubuntu-ansible-deb, apache-deb from all docs

---

## Hardware Wishlist
- [ ] LSI 9207-8i or 9211-8i HBA card (~$20-40 eBay)
- [ ] 2x SFF-8087 to SATA breakout cables (~$5-10 each eBay)
- [ ] 2TB SSD for PVE3 VM storage
- [ ] 20TB CMR drive to replace ada4 in TRYAGAIN pool ⚠️
- [ ] 4x 8GB DDR3 sticks for restic-deb RAM upgrade
- [ ] Inventory all spare/removable hard drives — identify reusable drives for restic-deb CRU bays
- [ ] Physical inventory of hardware reserves — hard drives, RAM, graphics cards, NICs, HBAs — build hw_reserve.md
- [ ] Physical inventory of hardware reserves — hard drives, RAM, graphics cards, NICs, HBAs — build hw_reserve.md
- [ ] RAM upgrades — free, no purchases needed:
  - truenas: replace 2x Hynix 4GB with 2x Crucial Ballistix 8GB DDR3-1600 + 2x Crucial UDIMM 8GB DDR3-1600 = 32GB
  - restic-deb: replace 4x 4GB with 2x Samsung 8GB DDR3-1600 (pulled from truenas) + 2x Timetec 8GB DDR3-1333 = 32GB
  - Do truenas first, move pulled Samsung sticks directly to restic
- [ ] Shardik RAM — pull 3 unknown sticks, identify them, install 2x PNY XLR8 16GB DDR4-3200 matched pair (1 in shardik, 1 in reserve). If instability persists try 4x 8GB DDR4-2133 (2x Samsung + 2x Micron from reserve). Do during Sunday rebuild if it happens.
- [ ] idee-deb RAM — install 2x Samsung 8GB DDR4-2133 in empty slots = 32GB total (matches existing Samsung stick)
- [ ] urnst-deb RAM — identify existing 8GB stick (dmidecode), fill remaining slots to 16GB max from reserve
- [ ] Verify M.2 slot status on urnst-deb, lee-deb, and amontillado — update hw_inv with NVMe/SSD slot info for all machines
- [ ] P2V Goodwim CentOS drive — image to Proxmox VM before disposing of drive
- [ ] Create backup_policy.md — document disk rotation schedule, Restic strategy, Patreon archive policy, and 3-2-1 approach
- [ ] Diff 3D/4TB drive contents against TrueNAS — rsync --dry-run to identify what needs migrating before retiring Aug 2022 backup
