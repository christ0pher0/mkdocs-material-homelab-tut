# Homelab Todo & Roadmap
_Last updated: 2026-05-10_
---
## Critical / Security
- [ ] **Dirty Frag mitigation** (CVE-2026-43284/43500) — disable esp4, esp6, rxrpc fleet-wide ⚠️
- [ ] **Copy Fail** (CVE-2026-31431) — verify patches applied fleet-wide ⚠️
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

### Monitoring Stack (monitor-deb 192.168.1.29)
- [x] Deploy Homepage, Zabbix, Grafana, Uptime Kuma on monitor-deb ✅ 2026-05-10
- [x] Deploy Prometheus + node-exporter + PVE-exporter + cAdvisor ✅ 2026-05-10
- [x] Import Node Exporter Full, cAdvisor, Proxmox dashboards in Grafana ✅ 2026-05-10
- [x] Add Zabbix as Grafana data source ✅ 2026-05-10
- [x] Push monitoring configs to Gitea (cos/monitor-deb) ✅ 2026-05-10
- [ ] Deploy node-exporter to non-Docker hosts (plow-rpm, pihole-book-deb, restic-deb)
- [ ] Fix Python 3.12 interpreter issue for restic-deb, octopi-deb in Ansible
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
- [ ] Add SNES folder — Lufia I & II, other SNES RPGs
- [ ] Add PSP folder — FFT War of the Lions, Tactics Ogre, Jeanne d'Arc
- [ ] Complete tactical RPG collections across all supported platforms
- [ ] Deduplicate DS ROMs (Fire Emblem Shadow Dragon appears 3x)
- [ ] RomM full scan after cleanup to pick up Skraper metadata

### Mediastack / Plex
- [x] Deploy Kometa on mediastack-deb ✅ 2026-05-10
- [ ] Kometa — configure Trakt, MDBList integrations
- [ ] Add Tautulli — Plex analytics
- [ ] Bazarr — subtitle automation
- [ ] Tdarr — transcoding (needs GPU node first)
- [ ] FlareSolverr — Cloudflare bypass for indexers
- [ ] Clean dead indexers in Prowlarr
- [ ] Add Plex Music library fix for mobile (Plex Pass confirmed, unresolved)
- [ ] Add Training and Photos libraries to Plex

### Proxmox Cluster
- [x] Build 2-node wheel cluster — shardik + maturin ✅
- [x] QDevice on git-ansible ✅
- [ ] Add pve3 (temerant → ThinkStation) to cluster
- [ ] Migrate swarm VMs (102/104/105) to SDA_store on maturin
- [ ] Rebuild lost VMs: 101 (monitor-deb rebuilt ✅), 106 (git-ansible rebuilt ✅), 107 (docker-deb rebuilt ✅)
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
- [ ] Rename typo'd MkDocs files: git_nfo.md → git_info.md, mdeiastack_apps.md → mediastack_apps.md
- [ ] Organize mkdocs.yml nav into sections
- [ ] Update network_context.md — remove dead VMs (101/106/107 rebuilt, grafana-docker-deb gone)
- [ ] Update hw_inventory.md — freenas-bsd → TrueNAS, add monitor-deb
- [ ] Create Proxmox cluster diagram
- [ ] Document monitoring stack architecture

### Network
- [ ] Dirty Frag mitigation — disable esp4/esp6/rxrpc fleet-wide
- [ ] Clarify Flint2 + Netgate topology
- [ ] Evaluate VLANs for IoT/media/server segmentation
- [ ] Unbound — local DNS resolver
- [ ] Authelia — auth layer for exposed services

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
| MariaDB        | —     | ✅ Running  |
| Plex           | 32400 | ✅ Running  |

---
## Maintenance Backlog
- [ ] Add fail2ban to homelab_baseline.yml
- [ ] Add chrony LXC skip to sync_time.yml
- [ ] Update check_services.yml to reflect current services
- [ ] Update fail2ban.yml — add pause before verify task
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

---
## Completed ✅
- [x] Deleted frodo user from rocky-rpm, alma-rpm, plow-rpm — 2026-04-09
- [x] fail2ban deployed fleet-wide — 2026-04-09
- [x] Fleet packages updated — 2026-04-09
- [x] mediastack-deb root disk expanded 30GB → 164GB — 2026-04-09
- [x] Traefik deployed on docker-deb — 2026-04-13
- [x] Vaultwarden deployed behind Caddy + Tailscale TLS — 2026-04-13
- [x] Passwords migrated from Google to Vaultwarden — 2026-04-13
- [x] FreeNAS 11.3 → TrueNAS CORE 13.0-U6.8 — 2026-04-27
- [x] TRYAGAIN pool imported — 45TB intact — 2026-04-27
- [x] Plex migrated from FreeNAS jail to Docker — 2026-04-27
- [x] wheel cluster built — shardik + maturin + QDevice — 2026-04-12
- [x] Gitea deployed on git-ansible — 2026-04-15
- [x] Kasm Workspaces 1.17.0 deployed on kasm-2404-deb — 2026-04-27
- [x] Portainer agents deployed fleet-wide — 2026-05-10
- [x] monitor-deb deployed (192.168.1.29) — Homepage, Zabbix, Grafana, Kuma — 2026-05-10
- [x] Prometheus + node-exporter + PVE-exporter + cAdvisor deployed — 2026-05-10
- [x] Grafana dashboards: Node Exporter Full, cAdvisor, Proxmox via Prometheus — 2026-05-10
- [x] Fleet packages patched (Copy Fail CVE-2026-31431) — 2026-05-10
- [x] snipeit-deb LXC destroyed (Snipe-IT moved to plow-rpm) — 2026-05-10
- [x] Dead inventory entries removed (grafana-docker-deb, ubuntu-ansible-deb, apache-deb) — 2026-05-10
- [x] monitor-deb configs pushed to Gitea — 2026-05-10
- [x] Kometa deployed on mediastack-deb — 2026-05-10
- [x] RomM ROM folders renamed to IGDB slugs — 2026-05-10
- [x] Skraper run complete — all 12 platforms scraped — 2026-05-10
- [x] mediastack-deb RAM doubled to 16GB — 2026-05-10
- [x] monitor-deb root LV expanded 15GB → 30GB — 2026-05-10
