# Homelab Todo & Roadmap
_Last updated: 2026-05-17_
---
## Critical / Security
- [ ] ZFS plugin ÃÂ¢ÃÂÃÂ monitor RAIDZ1 health, drive errors on TrueNAS ÃÂ¢ÃÂÃÂ ÃÂ¯ÃÂ¸ÃÂ
- [ ] Disk space alerts ÃÂ¢ÃÂÃÂ eld D: (10%), amontillado D: (11%), pi1 SD (91%) ÃÂ¢ÃÂÃÂ ÃÂ¯ÃÂ¸ÃÂ
- [ ] **Telegram alerts** ÃÂ¢ÃÂÃÂ bot notifications when something looks wrong
- [ ] Alert on: drive errors, disk >85%, service down, high temp, RAM pressure
- [ ] sudoers drop-in for docker group auto-add script (per-user, NOPASSWD usermod)
### Backup Strategy (eld)
- [ ] Migrate eld to Ubuntu 26.04
- [ ] Deploy Restic ÃÂ¢ÃÂÃÂ automated backups from TrueNAS (Tier 1)
- [ ] Configure 2x CRU bays on eld for rotating manual drives (Tier 2)
- [ ] Establish offsite drive rotation schedule (Tier 3)
- [ ] Expand backup coverage ÃÂ¢ÃÂÃÂ currently only Patreon O-Z backed up, A-N missing
- [ ] Expand eld storage ÃÂ¢ÃÂÃÂ 3TB internal nearly full (10% free)
- [ ] Upgrade eld RAM to 32GB DDR3 before migration
---
## In Progress
- [ ] Inventory 5 remaining waiting systems ÃÂ¢ÃÂÃÂ match hardware to roles
- [ ] Inventory pve3 (ThinkStation offsite) ÃÂ¢ÃÂÃÂ specs, storage, role
- [ ] Purchase [Hologram.io](http://Hologram.io) SIM for argos-deb LTE
- [ ] Purchase larger SD card for pi1-deb (3.8GB, 91% full)
- [ ] Pi rack ÃÂ¢ÃÂÃÂ 3D print or buy, house all 8 Pis cleanly
- [ ] PoE switch + PoE HATs ÃÂ¢ÃÂÃÂ single cable per Pi for power + network
- [ ] Set up scheduled backup for maturin VMs to maturin nvme_store (local backup)
- [ ] Shrink maturin pve-data pool ÃÂ¢ÃÂÃÂ only cloudinit template remains on local-lvm
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
### PVE3 ÃÂ¢ÃÂÃÂ temerant ÃÂ¢ÃÂÃÂ Proxmox node 3
- [ ] Check temerant-win 2x 3TB HDDs (Seagate ST3000DM001) for important data ÃÂ¢ÃÂÃÂ ÃÂ¯ÃÂ¸ÃÂ
- [ ] Pull drives, wipe Windows, install Proxmox VE
- [ ] Add to wheel cluster (shardik + maturin)
- [ ] Configure Tailscale on pve3
- [ ] Add to inventory_auto and MkDocs
- [ ] Eventually: GPU passthrough of GTX 1080 Ti for RPCS3/AI workloads
- [ ] Check AB350 IOMMU groupings before passthrough attempt
### Maturin Hardware
### Monitoring Stack (monitor-deb 192.168.1.29)
- [ ] Deploy node-exporter to non-Docker hosts (plow-rpm, pihole-book-deb, restic-deb)
- [ ] Add Uptime Kuma to Homepage widget (fix slug)
- [ ] Configure Zabbix ÃÂ¢ÃÂÃÂ Telegram alerting
- [ ] Deploy Loki for log aggregation
### Portainer Fleet
- [ ] Write portainer_sync.py scheduled task ÃÂ¢ÃÂÃÂ detect Docker hosts, auto-register missing ones
- [ ] Fix TLS registration API issue in portainer_sync.py
### TrueNAS Hardware Rebuild ÃÂ¢ÃÂ­ÃÂ
- [ ] Check temerant-win 2x 3TB HDDs for important data before touching hardware
- [ ] Pull mobo, Ryzen 5 1600X, 32GB DDR4, GTX 1080 Ti, 500GB SSD from temerant
- [ ] Install into existing FreeNAS beige full tower
- [ ] Order LSI 9207-8i or 9211-8i HBA card (~$20-40 eBay)
- [ ] Order 2x SFF-8087 to SATA breakout cables (~$5-10 each eBay)
- [ ] Install TrueNAS on 500GB SSD ÃÂ¢ÃÂÃÂ no more USB boot drives
- [ ] Boot TrueNAS, import TRYAGAIN pool
- [ ] Reconfigure SMB shares, cifs1 user, services
- [ ] Update mediastack-deb fstab if IP changes
### TrueNAS ÃÂ¢ÃÂÃÂ Current State
- [ ] Set ue0 (USB NIC) to static 192.168.1.5 ÃÂ¢ÃÂÃÂ survives reboots
- [ ] Fix alc0 onboard NIC
- [ ] Add second USB boot drive to freenas-boot mirror
- [ ] Investigate ada4 bad sectors alert from February 2026 ÃÂ¢ÃÂÃÂ ÃÂ¯ÃÂ¸ÃÂ
- [ ] Delete iocage datasets ÃÂ¢ÃÂÃÂ Weltgeist and Alea Iacta Est jails (91GB)
- [ ] Dedupe/find duplicate filenames on TRYAGAIN pool ÃÂ¢ÃÂÃÂ fdupes or rdfind
- [ ] Explore LaunchBox ROM archive on NAS ÃÂ¢ÃÂÃÂ migrate to RomM
### RomM / Gaming
- [ ] Complete tactical RPG collections across all supported platforms
- [ ] Deduplicate DS ROMs (Fire Emblem Shadow Dragon appears 3x)
### Mediastack / Plex
- [ ] Kometa ÃÂ¢ÃÂÃÂ verify Trakt/MDBList working after next run
- [ ] Add Tautulli ÃÂ¢ÃÂÃÂ Plex analytics
- [ ] Bazarr ÃÂ¢ÃÂÃÂ subtitle automation
- [ ] Tdarr ÃÂ¢ÃÂÃÂ transcoding (needs GPU node first)
- [ ] Add Plex Music library fix for mobile (Plex Pass confirmed, unresolved)
- [ ] Add Training and Photos libraries to Plex
### Proxmox Cluster
- [ ] Add pve3 (temerant ÃÂ¢ÃÂÃÂ ThinkStation) to cluster
- [ ] Configure Proxmox HA for automatic VM failover
- [ ] Set up shared storage ÃÂ¢ÃÂÃÂ NFS from TrueNAS
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
- [ ] Phase 1 ÃÂ¢ÃÂÃÂ backup to TrueNAS, Tailscale
- [ ] Phase 2 ÃÂ¢ÃÂÃÂ Zigbee, MQTT, ESPHome, Frigate
- [ ] Phase 3 ÃÂ¢ÃÂÃÂ automations, Music Assistant, OctoPrint
- [ ] Phase 4 ÃÂ¢ÃÂÃÂ argos-deb wall kiosk
### Documentation
- [ ] Create Proxmox cluster diagram
- [ ] Document monitoring stack architecture
### Network
- [ ] Clarify Flint2 + Netgate topology
- [ ] Evaluate VLANs for IoT/media/server segmentation
- [ ] Unbound ÃÂ¢ÃÂÃÂ local DNS resolver
- [ ] Authelia ÃÂ¢ÃÂÃÂ auth layer for exposed services
### Ansible
- [ ] Pin ansible_python_interpreter per host in inventory_auto
- [ ] Add fail2ban to homelab_baseline.yml
- [ ] Add chrony LXC skip to sync_time.yml
- [ ] Update check_services.yml to reflect current services
- [ ] Update fail2ban.yml ÃÂ¢ÃÂÃÂ add pause before verify task
---
## Mediastack ÃÂ¢ÃÂÃÂ Current Stack
| App            | Port  | Status      |
|----------------|-------|-------------|
| Sonarr         | 8989  | ÃÂ¢ÃÂÃÂ Running  |
| Radarr         | 7878  | ÃÂ¢ÃÂÃÂ Running  |
| Lidarr         | 8686  | ÃÂ¢ÃÂÃÂ Running  |
| Mylar3         | 8091  | ÃÂ¢ÃÂÃÂ Running  |
| SABnzbd        | 8090  | ÃÂ¢ÃÂÃÂ Running  |
| Prowlarr       | 9696  | ÃÂ¢ÃÂÃÂ Running  |
| Seerr          | 5055  | ÃÂ¢ÃÂÃÂ Running  |
| Komga          | 8085  | ÃÂ¢ÃÂÃÂ Running  |
| Audiobookshelf | 13378 | ÃÂ¢ÃÂÃÂ Running  |
| RomM           | 8998  | ÃÂ¢ÃÂÃÂ Running  |
| Kometa         | ÃÂ¢ÃÂÃÂ     | ÃÂ¢ÃÂÃÂ Running  |
| Gluetun VPN    | ÃÂ¢ÃÂÃÂ     | ÃÂ¢ÃÂÃÂ Running  |
| qBittorrent    | 8082  | ÃÂ¢ÃÂÃÂ Running  |
| Unpackerr      | ÃÂ¢ÃÂÃÂ     | ÃÂ¢ÃÂÃÂ Running  |
| FlareSolverr   | 8191  | ÃÂ¢ÃÂÃÂ Running  |
| MariaDB        | ÃÂ¢ÃÂÃÂ     | ÃÂ¢ÃÂÃÂ Running  |
| Plex           | 32400 | ÃÂ¢ÃÂÃÂ Running  |
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
- [ ] Replace sdd drive (Z4D2EJ31) ÃÂ¢ÃÂÃÂ 24 pending/uncorrectable sectors ÃÂ¢ÃÂÃÂ ÃÂ¯ÃÂ¸ÃÂ

