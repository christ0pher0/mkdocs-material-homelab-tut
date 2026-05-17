# Homelab Todo & Roadmap
_Last updated: 2026-05-17_
---
## Critical / Security
- [ ] ZFS plugin â monitor RAIDZ1 health, drive errors on TrueNAS â ï¸
- [ ] Disk space alerts â eld D: (10%), amontillado D: (11%), pi1 SD (91%) â ï¸
- [ ] **Telegram alerts** â bot notifications when something looks wrong
- [ ] Alert on: drive errors, disk >85%, service down, high temp, RAM pressure
- [ ] sudoers drop-in for docker group auto-add script (per-user, NOPASSWD usermod)
### Backup Strategy (eld)
- [ ] Migrate eld to Ubuntu 26.04
- [ ] Deploy Restic â automated backups from TrueNAS (Tier 1)
- [ ] Configure 2x CRU bays on eld for rotating manual drives (Tier 2)
- [ ] Establish offsite drive rotation schedule (Tier 3)
- [ ] Expand backup coverage â currently only Patreon O-Z backed up, A-N missing
- [ ] Expand eld storage â 3TB internal nearly full (10% free)
- [ ] Upgrade eld RAM to 32GB DDR3 before migration
---
## In Progress
- [ ] Inventory 5 remaining waiting systems â match hardware to roles
- [ ] Inventory pve3 (ThinkStation offsite) â specs, storage, role
- [ ] Purchase [Hologram.io](http://Hologram.io) SIM for argos-deb LTE
- [ ] Purchase larger SD card for pi1-deb (3.8GB, 91% full)
- [ ] Pi rack â 3D print or buy, house all 8 Pis cleanly
- [ ] PoE switch + PoE HATs â single cable per Pi for power + network
- [ ] Set up scheduled backup for maturin VMs to maturin nvme_store (local backup)
- [ ] Shrink maturin pve-data pool â only cloudinit template remains on local-lvm
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
### PVE3 â temerant â Proxmox node 3
- [ ] Check temerant-win 2x 3TB HDDs (Seagate ST3000DM001) for important data â ï¸
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
- [ ] Configure Zabbix â Telegram alerting
- [ ] Deploy Loki for log aggregation
### Portainer Fleet
- [ ] Write portainer_sync.py scheduled task â detect Docker hosts, auto-register missing ones
- [ ] Fix TLS registration API issue in portainer_sync.py
### TrueNAS Hardware Rebuild â­
- [ ] Check temerant-win 2x 3TB HDDs for important data before touching hardware
- [ ] Pull mobo, Ryzen 5 1600X, 32GB DDR4, GTX 1080 Ti, 500GB SSD from temerant
- [ ] Install into existing FreeNAS beige full tower
- [ ] Order LSI 9207-8i or 9211-8i HBA card (~$20-40 eBay)
- [ ] Order 2x SFF-8087 to SATA breakout cables (~$5-10 each eBay)
- [ ] Install TrueNAS on 500GB SSD â no more USB boot drives
- [ ] Boot TrueNAS, import TRYAGAIN pool
- [ ] Reconfigure SMB shares, cifs1 user, services
- [ ] Update mediastack-deb fstab if IP changes
### TrueNAS â Current State
- [ ] Set ue0 (USB NIC) to static 192.168.1.5 â survives reboots
- [ ] Fix alc0 onboard NIC
- [ ] Add second USB boot drive to freenas-boot mirror
- [ ] Investigate ada4 bad sectors alert from February 2026 â ï¸
- [ ] Delete iocage datasets â Weltgeist and Alea Iacta Est jails (91GB)
- [ ] Dedupe/find duplicate filenames on TRYAGAIN pool â fdupes or rdfind
- [ ] Explore LaunchBox ROM archive on NAS â migrate to RomM
### RomM / Gaming
- [ ] Complete tactical RPG collections across all supported platforms
- [ ] Deduplicate DS ROMs (Fire Emblem Shadow Dragon appears 3x)
### Mediastack / Plex
- [ ] Kometa â verify Trakt/MDBList working after next run
- [ ] Add Tautulli â Plex analytics
- [ ] Bazarr â subtitle automation
- [ ] Tdarr â transcoding (needs GPU node first)
- [ ] Add Plex Music library fix for mobile (Plex Pass confirmed, unresolved)
- [ ] Add Training and Photos libraries to Plex
### Proxmox Cluster
- [ ] Add pve3 (temerant â ThinkStation) to cluster
- [ ] Configure Proxmox HA for automatic VM failover
- [ ] Set up shared storage â NFS from TrueNAS
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
- [ ] Phase 1 â backup to TrueNAS, Tailscale
- [ ] Phase 2 â Zigbee, MQTT, ESPHome, Frigate
- [ ] Phase 3 â automations, Music Assistant, OctoPrint
- [ ] Phase 4 â argos-deb wall kiosk
### Documentation
- [ ] Create Proxmox cluster diagram
- [ ] Document monitoring stack architecture
### Network
- [ ] Clarify Flint2 + Netgate topology
- [ ] Evaluate VLANs for IoT/media/server segmentation
- [ ] Unbound â local DNS resolver
- [ ] Authelia â auth layer for exposed services
### Ansible
- [ ] Pin ansible_python_interpreter per host in inventory_auto
- [ ] Add fail2ban to homelab_baseline.yml
- [ ] Add chrony LXC skip to sync_time.yml
- [ ] Update check_services.yml to reflect current services
- [ ] Update fail2ban.yml â add pause before verify task
---
## Mediastack â Current Stack
| App            | Port  | Status      |
|----------------|-------|-------------|
| Sonarr         | 8989  | â Running  |
| Radarr         | 7878  | â Running  |
| Lidarr         | 8686  | â Running  |
| Mylar3         | 8091  | â Running  |
| SABnzbd        | 8090  | â Running  |
| Prowlarr       | 9696  | â Running  |
| Seerr          | 5055  | â Running  |
| Komga          | 8085  | â Running  |
| Audiobookshelf | 13378 | â Running  |
| RomM           | 8998  | â Running  |
| Kometa         | â     | â Running  |
| Gluetun VPN    | â     | â Running  |
| qBittorrent    | 8082  | â Running  |
| Unpackerr      | â     | â Running  |
| FlareSolverr   | 8191  | â Running  |
| MariaDB        | â     | â Running  |
| Plex           | 32400 | â Running  |
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
- [ ] Replace sdd drive (Z4D2EJ31) â 24 pending/uncorrectable sectors â ï¸

