# Homelab Todo & Roadmap
_Last updated: 2026-05-17_
---
## Critical / Security
- [ ] ZFS plugin — monitor RAIDZ1 health, drive errors on TrueNAS ⚠️
- [ ] Disk space alerts — eld D: (10%), amontillado D: (11%), pi1 SD (91%) ⚠️
- [ ] **Telegram alerts** — bot notifications when something looks wrong
- [ ] Alert on: drive errors, disk >85%, service down, high temp, RAM pressure
- [ ] sudoers drop-in for docker group auto-add script (per-user, NOPASSWD usermod)
### Backup Strategy (eld)
- [ ] Migrate eld to Ubuntu 26.04
- [ ] Deploy Restic — automated backups from TrueNAS (Tier 1)
- [ ] Configure 2x CRU bays on eld for rotating manual drives (Tier 2)
- [ ] Establish offsite drive rotation schedule (Tier 3)
- [ ] Expand backup coverage — currently only Patreon O-Z backed up, A-N missing
- [ ] Expand eld storage — 3TB internal nearly full (10% free)
- [ ] Upgrade eld RAM to 32GB DDR3 before migration
---
## In Progress
- [ ] Inventory 5 remaining waiting systems — match hardware to roles
- [ ] Inventory pve3 (ThinkStation offsite) — specs, storage, role
- [ ] Purchase [Hologram.io](http://Hologram.io) SIM for argos-deb LTE
- [ ] Purchase larger SD card for pi1-deb (3.8GB, 91% full)
- [ ] Pi rack — 3D print or buy, house all 8 Pis cleanly
- [ ] PoE switch + PoE HATs — single cable per Pi for power + network
- [x] Verify swarm VM migration complete (102/104/105 → shardik SDA_store) ✅ 2026-05-16
- [x] Verify Kometa Trakt/MDBList working ✅ 2026-05-16
- [ ] Set up scheduled backup for maturin VMs to maturin nvme_store (local backup)
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
- [x] Install Samsung 980 Pro 1TB NVMe in maturin M.2 slot ✅ 2026-05-16
- [x] Add nvme_store as Proxmox dir storage pool on maturin ✅ 2026-05-16
### Monitoring Stack (monitor-deb 192.168.1.29)
- [x] Deploy Homepage, Zabbix, Grafana, Uptime Kuma on monitor-deb ✅ 2026-05-10
- [x] Deploy Prometheus + node-exporter + PVE-exporter + cAdvisor ✅ 2026-05-10
- [x] Import Node Exporter Full, cAdvisor, Proxmox dashboards in Grafana ✅ 2026-05-10
- [x] Add Zabbix as Grafana data source ✅ 2026-05-10
- [x] Push monitoring configs to Gitea (cos/monitor-deb) ✅ 2026-05-10
- [ ] Deploy node-exporter to non-Docker hosts (plow-rpm, pihole-book-deb, restic-deb)
- [ ] Add Uptime Kuma to Homepage widget (fix slug)
- [ ] Configure Zabbix → Telegram alerting
- [ ] Deploy Loki for log aggregation
### Portainer Fleet
- [x] Deploy Portainer agent fleet-wide ✅ 2026-05-10
- [x] Register all Docker hosts in Portainer ✅ 2026-05-10
- [ ] Write portainer_sync.py scheduled task — detect Docker hosts, auto-register missing ones
- [ ] Fix TLS registration API issue in portainer_sync.py
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
- [ ] Add second USB boot drive to freenas-boot mirror
- [ ] Investigate ada4 bad sectors alert from February 2026 ⚠️
- [ ] Delete iocage datasets — Weltgeist and Alea Iacta Est jails (91GB)
- [ ] Dedupe/find duplicate filenames on TRYAGAIN pool — fdupes or rdfind
- [ ] Explore LaunchBox ROM archive on NAS — migrate to RomM
### RomM / Gaming
- [x] Deploy RomM on mediastack-deb ✅
- [x] Clean ROM folder structure — rename to IGDB slugs ✅ 2026-05-10
- [x] Run Skraper against all 12 platforms ✅ 2026-05-10
- [x] RomM cleanup — orphaned resources, WebP conversion, segacd rescan, unidentified games, Dragon_warrior filenames ✅ 2026-05-15
- [x] LaunchBox 13.26 installed, all platforms imported ✅ 2026-05-15
- [ ] Complete tactical RPG collections across all supported platforms
- [ ] Deduplicate DS ROMs (Fire Emblem Shadow Dragon appears 3x)
### Mediastack / Plex
- [x] Deploy Kometa on mediastack-deb ✅ 2026-05-10
- [x] FlareSolverr deployed and wired to Prowlarr ✅ 2026-05-15
- [x] Unpackerr deployed and wired to Sonarr/Radarr/Lidarr ✅ 2026-05-15
- [x] Kometa Trakt and MDBList configured ✅ 2026-05-15
- [x] Dead indexers cleaned in Prowlarr ✅
- [x] 1337x and KickassTorrents added to Prowlarr ✅ 2026-05-15
- [ ] Kometa — verify Trakt/MDBList working after next run
- [ ] Add Tautulli — Plex analytics
- [ ] Bazarr — subtitle automation
- [ ] Tdarr — transcoding (needs GPU node first)
- [ ] Add Plex Music library fix for mobile (Plex Pass confirmed, unresolved)
- [ ] Add Training and Photos libraries to Plex
### Proxmox Cluster
- [x] Build 2-node wheel cluster — shardik + maturin ✅
- [x] QDevice on git-ansible ✅
- [x] Rebuild lost VMs: 101 (monitor-deb ✅), 106 (git-ansible ✅), 107 (docker-deb ✅) ✅ 2026-05-15
- [x] Migrate swarm VMs 102/104/105 from maturin → shardik SDA_store ✅ 2026-05-15
- [x] Verify swarm VM migration fully complete ✅ 2026-05-16
- [ ] Add pve3 (temerant → ThinkStation) to cluster
- [ ] Configure Proxmox HA for automatic VM failover
- [ ] Set up shared storage — NFS from TrueNAS
### Local AI Assistant
- [ ] Deploy Ollama on idee-deb (GPU node) with GTX 1080 Ti passthrough
- [ ] Deploy Open WebUI
- [ ] Create sysadmin / homelab / casual assistant personalities
- [ ] Add Whisper (STT) and Piper (TTS)
- [ ] Feed MkDocs docs as RAG knowledge base
### Vaultwarden / Secrets
- [x] Vaultwarden deployed behind Caddy + Tailscale TLS ✅
- [ ] Fix Vaultwarden autofill port matching issue in browser extension
- [ ] Store all service credentials with full URL including port
- [ ] Evaluate HashiCorp Vault for Ansible secrets management
### Home Assistant
- [ ] Phase 1 — backup to TrueNAS, Tailscale
- [ ] Phase 2 — Zigbee, MQTT, ESPHome, Frigate
- [ ] Phase 3 — automations, Music Assistant, OctoPrint
- [ ] Phase 4 — argos-deb wall kiosk
### Documentation
- [x] Rename typo'd MkDocs files: git_nfo.md → git_info.md, mdeiastack_apps.md → mediastack_apps.md ✅ 2026-05-15
- [x] mediastack_apps.md overhauled with deployment status table ✅ 2026-05-15
- [x] Organize mkdocs.yml nav into sections ✅ 2026-05-16
- [x] Update network_context.md — full rewrite ✅ 2026-05-16
- [x] Update hw_inventory.md ✅ 2026-05-16
- [ ] Create Proxmox cluster diagram
- [ ] Document monitoring stack architecture
### Network
- [x] Dirty Frag mitigation — disable esp4/esp6/rxrpc fleet-wide ✅ 2026-05-15
- [ ] Clarify Flint2 + Netgate topology
- [ ] Evaluate VLANs for IoT/media/server segmentation
- [ ] Unbound — local DNS resolver
- [ ] Authelia — auth layer for exposed services
### Ansible
- [x] Silence interpreter_python discovery warnings fleet-wide ✅ 2026-05-15
- [ ] Pin ansible_python_interpreter per host in inventory_auto
- [ ] Add fail2ban to homelab_baseline.yml
- [ ] Add chrony LXC skip to sync_time.yml
- [ ] Update check_services.yml to reflect current services
- [ ] Update fail2ban.yml — add pause before verify task
---
## Mediastack — Current Stack
| App            | Port  | Status      |
|----------------|-------|-------------|
| Sonarr         | 8989  | ✅ Running  |
| Radarr         | 7878  | ✅ Running  |
| Lidarr         | 8686  | ✅ Running  |
| Mylar3         | 8091  | ✅ Running  |
| SABnzbd        | 8090  | ✅ Running  |
| Prowlarr       | 9696  | ✅ Running  |
| Seerr          | 5055  | ✅ Running  |
| Komga          | 8085  | ✅ Running  |
| Audiobookshelf | 13378 | ✅ Running  |
| RomM           | 8998  | ✅ Running  |
| Kometa         | —     | ✅ Running  |
| Gluetun VPN    | —     | ✅ Running  |
| qBittorrent    | 8082  | ✅ Running  |
| Unpackerr      | —     | ✅ Running  |
| FlareSolverr   | 8191  | ✅ Running  |
| MariaDB        | —     | ✅ Running  |
| Plex           | 32400 | ✅ Running  |
---
## Maintenance Backlog
- [ ] Clarify MariaDB and nginx role on git-ansible-deb
- [ ] Confirm git-ansible physical host specs with dmidecode
- [ ] Inventory offsite ThinkStation (pve3)
- [ ] Add pve3 to Tailscale and Ansible inventory
- [ ] Remove snipeit-deb from all docs (LXC destroyed 2026-05-10)
- [ ] Remove grafana-docker-deb, ubuntu-ansible-deb, apache-deb from all docs
---
## Hardware Wishlist
- [ ] LSI 9207-8i or 9211-8i HBA card (~$20-40 eBay)
- [ ] 2x SFF-8087 to SATA breakout cables (~$5-10 each eBay)
- [ ] 2TB SSD for PVE3 VM storage
- [ ] Replace sdd drive (Z4D2EJ31) — 24 pending/uncorrectable sectors ⚠️
- [x] Dirty Frag CVE-2026-43284/43500 mitigated fleet-wide — 2026-05-15
- [x] FlareSolverr deployed, 1337x and KickassTorrents added to Prowlarr — 2026-05-15
- [x] Unpackerr deployed and wired to Sonarr/Radarr/Lidarr — 2026-05-15
- [x] Kometa Trakt and MDBList configured — 2026-05-15
- [x] Renamed typo'd MkDocs files (git_nfo.md, mdeiastack_apps.md) — 2026-05-15
- [x] mediastack_apps.md overhauled with deployment status table — 2026-05-15
- [x] Ansible interpreter warnings silenced (auto_silent) — 2026-05-15
- [x] Swarm VMs 102/104/105 migrated from maturin → shardik SDA_store — 2026-05-15
- [x] ZFS recovery failed — shardik rebuilt, ZFS masked off — 2026-05-15
- [x] RomM cleanup complete — orphaned resources, WebP, segacd rescan, filenames — 2026-05-15
- [x] LaunchBox 13.26 installed, all platforms imported — 2026-05-15
- [x] MkDocs nav reorganized into sections — 2026-05-16
- [x] network_context.md fully rewritten — 2026-05-16
- [x] hw_inv.md updated — 2026-05-16
- [x] /etc/hosts cleaned, sorted, synced to router reservations — 2026-05-16
- [x] inventory_auto cleaned — removed duplicate linux/debian/redhat groups — 2026-05-16
- [x] Network diagram overhauled — Proxmox topology, no duplicates — 2026-05-16
- [x] Proxmox services restored on shardik (full-upgrade fixed Perl conflict) — 2026-05-16
- [x] noVNC console working on shardik — 2026-05-16
- [x] Samsung 980 Pro 1TB NVMe installed in maturin, nvme_store created — 2026-05-16
- [x] rocky-rpm rebuilt (VM 109) on maturin nvme_store — Rocky 9.7 — 2026-05-16
- [x] rocky-rpm onboarded — baseline, EPEL, fail2ban, Dirty Frag, Zabbix agent — 2026-05-16
- [x] rocky-rpm IP changed to 192.168.1.20 — 2026-05-16
- [x] VM load balancing complete — maturin: monitor/docker/mediastack/git-ansible; shardik: alma/rocky/kasm/pihole/swarm — 2026-05-17
- [x] Cross-node backup strategy implemented — maturin VMs → shardik SDC_store; shardik VMs → shardik SDB_store — 2026-05-17
- [x] Scheduled backup jobs configured — shardik VMs @ 2am, maturin VMs @ 3am, maxfiles=2 — 2026-05-17
- [x] SDB_store and SDC_store formatted and mounted on shardik — 2026-05-17
- [x] SDD drive (Z4D2EJ31) condemned — 24 pending/uncorrectable sectors — 2026-05-17
- [x] Old 2025 backup files purged from SDA_store and DIR_SDA — 2026-05-17
- [x] Swarm VMs (102/104/105) onboot=0, kept stopped — 2026-05-17
- [x] Kasm added to Homepage dashboard (Infrastructure section) — 2026-05-17
- [x] vzdump.conf tmpdir set to /mnt/nvme_store on maturin — 2026-05-17
- [x] Direct SSH backdoor confirmed to mediastack-deb (192.168.1.36) — 2026-05-17

