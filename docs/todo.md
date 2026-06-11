# Homelab Todo & Roadmap
_Last updated: 2026-06-11_
---

## Critical / Security
- [ ] **Shardik PSU** — suspected failure, primary hypervisor — monitor uptime, plan Sunday replacement
- [ ] docker-deb static IP or confirmed DHCP reservation — hosts Vaultwarden, Traefik, Portainer ⚠️
- [ ] Disk space alerts — amontillado D: (11%), pi1 SD (91%) ⚠️
- [ ] **Telegram alerts** — bot notifications when something looks wrong
- [ ] Alert on: drive errors, disk >85%, service down, high temp, RAM pressure
- [ ] sudoers drop-in for docker group auto-add script (per-user, NOPASSWD usermod)
- [ ] Investigate amontillado D: (2.79TB, 11% free) — audit VMs and junk, clear or expand

### Backup Strategy (restic-deb)
- [ ] STL drive rotation — in progress: TV ✅ Movies ✅ STL E-H ✅ currently mid E-K (at H), I-K drive pending, L-O and O-S remaining
- [ ] Configure 2x CRU bays on restic-deb for rotating manual drives (Tier 2)
- [ ] Establish offsite drive rotation schedule (Tier 3)
- [ ] Expand restic-deb storage — 3TB internal nearly full (10% free)

---

## Immediate Maintenance (Sysadmin)
- [ ] **Patch all hosts** — full OS update run across entire fleet ⚠️
- [ ] **Reboot docker-deb** — kernel update pending 2+ weeks, critical (runs Vaultwarden/Traefik/Portainer)
- [ ] Update Portainer — 13 months old
- [ ] Fix pi1-deb SD card — 91% full, will fail silently (replacement SD in reserve)
- [ ] Clean stale entries from GL-MT6000 /etc/hosts: snipeit-deb, grafana-docker-deb, ubuntu-ansible-deb, apache-deb, weltgeist-media, alea_iacta_est-media
- [ ] Investigate orphaned Docker network br-ca523ef71531 on docker-deb — prune if safe
- [ ] Remove snipeit-deb from all docs (LXC destroyed 2026-05-10)
- [ ] Remove grafana-docker-deb, ubuntu-ansible-deb, apache-deb from all docs

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

### 1. TrueNAS Hardware Rebuild ⭐
**Goal:** Replace aging Z77/i5-3570K with temerant hardware (Ryzen 5 1600X, 32GB DDR4, GTX 1080 Ti)
**Blocker:** LSI HBA not yet found — order now if not located
- [ ] Check temerant-win 2x 3TB HDDs (Seagate ST3000DM001) for important data ⚠️
- [ ] Pull mobo, Ryzen 5 1600X, 32GB DDR4, GTX 1080 Ti, 500GB SSD from temerant
- [ ] **Order LSI 9207-8i or 9211-8i HBA** (~$20-40 eBay) — blocking item
- [ ] Order 2x SFF-8087 to SATA breakout cables (~$5-10 each eBay)
- [ ] Install hardware into existing FreeNAS beige full tower
- [ ] Install TrueNAS on 500GB SSD — replace USB boot drives
- [ ] Boot TrueNAS, import TRYAGAIN pool
- [ ] Reconfigure SMB shares, cifs1 user, services
- [ ] Update mediastack-deb fstab if IP changes
- [ ] Fix onboard NIC (alc0) or install reserved NIC
- [ ] Dedupe/find duplicate filenames on TRYAGAIN — fdupes or rdfind (post-rebuild)
- [ ] Delete iocage datasets — Weltgeist and Alea Iacta Est jails (91GB)

### 2. Shardik Hardware Upgrade
**Goal:** Replace PSU, upgrade CPU to Ryzen 7 2700X, max RAM to 64GB
- [ ] Replace PSU — suspected failure, 1-month uptime target ⚠️
- [ ] Upgrade CPU: Ryzen 7 2700X (~$30-50 eBay, drop-in AM4, BIOS supports it)
- [ ] Replace 8GB RAM stick with 16GB DDR4 2667 to reach 64GB max
- [ ] Verify ZFS mask still appropriate post-rebuild
- [ ] Confirm all VMs stable after hardware swap

### 3. 192.168.1.8 Router → Access Point Conversion
**Goal:** Repurpose existing router hardware at .1.8 as a wireless access point
- [ ] Identify hardware at 192.168.1.8
- [ ] Plan AP placement and coverage
- [ ] Configure as AP (disable DHCP, bridge mode)
- [ ] Test coverage and handoff with main router (GL-MT6000)

---

## Planned Projects

### PVE3 — Add to Proxmox Cluster
- [ ] Configure Tailscale on pve3
- [ ] Full hardware inventory (dmidecode, photos)
- [ ] Add to Proxmox cluster (shardik + maturin + pve3 = proper 3-node quorum)
- [ ] Add to inventory_auto and MkDocs
- [ ] Eventually: GPU passthrough of GTX 1080 Ti for RPCS3/AI workloads
- [ ] Check AB350 IOMMU groupings before passthrough attempt

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

### Local AI Assistant (idee-deb)
- [ ] Install GTX 1080 Ti from stock into idee-deb (drop-in, biggest single upgrade)
- [ ] Deploy Ollama with GPU passthrough
- [ ] Deploy Open WebUI
- [ ] Create sysadmin / homelab / casual assistant personalities
- [ ] Add Whisper (STT) and Piper (TTS)
- [ ] Feed MkDocs docs as RAG knowledge base

### Proxmox Cluster
- [ ] Configure Proxmox HA for automatic VM failover
- [ ] Set up shared storage — NFS from TrueNAS

### PBS — Next Steps
- [ ] Mirror PBS backups to restic-deb
- [ ] Evaluate PBS tape backup to CRU bays

### Mediastack / Plex
- [ ] Add Tautulli — Plex analytics
- [ ] Bazarr — subtitle automation
- [ ] Tdarr — transcoding (needs GPU node first — idee-deb)
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

### Ansible
- [ ] Pin ansible_python_interpreter per host in inventory_auto
- [ ] Add fail2ban to homelab_baseline.yml
- [ ] Add chrony LXC skip to sync_time.yml
- [ ] Update check_services.yml to reflect current services
- [ ] Update fail2ban.yml — add pause before verify task

### MkDocs / Automation
- [ ] Automate doc updates — push from ED session to git-ansible without manual paste
- [ ] completed.md auto-population — move checked items from todo.md via checkbox_persist.js

---

## Parking Lot (Research Needed — Not Yet Scheduled)
- [ ] **Swarm architecture** — should monitoring stack move to swarm? Evaluate what makes sense
- [ ] **Ceph** — second attempt, needs planning and dedicated hardware evaluation
- [ ] **YouTube channel tech scouting** — Chris to provide channel list, ED to filter for lab-relevant technologies

---

## Hardware Policy
- **No HDDs under 3TB** in any active role — sub-3TB drives are disposal/ewaste candidates after data check

## Hardware Wishlist
- [ ] LSI 9207-8i or 9211-8i HBA card (~$20-40 eBay) — **blocking TrueNAS rebuild**
- [ ] 2x SFF-8087 to SATA breakout cables (~$5-10 each eBay)
- [ ] Replacement SD card for pi1-deb (3.8GB, 91% full)

---

## Maintenance Backlog
- [x] Clarify MariaDB and nginx role on git-ansible-deb
- [x] Confirm git-ansible physical host specs with dmidecode
- [x] Order 20TB CMR replacement drive for ada4 — DONE
- [x] Replace ada4 in TRYAGAIN RAIDZ1 pool — DONE, resilvering complete, pool HEALTHY
- [x] RAM upgrades — truenas (32GB DDR3), restic-deb (32GB DDR3), urnst-deb (16GB DDR4), idee-deb (32GB DDR4) — ALL COMPLETE
- [ ] Inventory offsite ThinkStation (pve3)
- [ ] Add pve3 to Tailscale and Ansible inventory
- [ ] Diff 3D/4TB drive contents against TrueNAS — rsync --dry-run before retiring Aug 2022 backup
- [ ] Add second USB boot drive to freenas-boot mirror (da0 dead) — or replace via rebuild
- [ ] Set ue0 (USB NIC) to static 192.168.1.5 — survives reboots (or fix via rebuild)
