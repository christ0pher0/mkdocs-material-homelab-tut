# Homelab Completed Work Log
_Last updated: 2026-05-17_
_Sorted by date and node/area_

---
## April 2026

### Security & Fleet
- fail2ban deployed fleet-wide — 2026-04-09
- Deleted frodo user from rocky-rpm, alma-rpm, plow-rpm — 2026-04-09
- Fleet packages updated — 2026-04-09
- Copy Fail CVE-2026-31431 patched fleet-wide — 2026-05-10
- Fix chrony on snipeit-deb and pihole-book-deb (disabled in LXC, time sync via PVE host) — 2026-04-09
- fail2ban whitelist updated to 192.168.1.0/24 — 2026-04-09
- Added Tailscale to git-ansible-deb (100.68.195.68) — 2026-04-10
- Passwordless sudo configured on git-ansible-deb — 2026-04-10

### Infrastructure
- wheel cluster built — shardik + maturin + QDevice on git-ansible — 2026-04-12
- Proxmox node rename (proxmox-deb → shardik, pve2 → maturin) via SQLite surgery — 2026-04-13
- Traefik v3 deployed on docker-deb — 2026-04-13
- Vaultwarden deployed behind Caddy + Tailscale TLS (port 8443) — 2026-04-13
- Passwords migrated from Google to Vaultwarden — 2026-04-13
- Gitea deployed on git-ansible (port 3000) — 2026-04-15
- Kasm Workspaces 1.17.0 deployed on kasm-2404-deb (192.168.1.26) — rebuilt after IP change corruption — 2026-04-27
- FreeNAS 11.3 → TrueNAS CORE 13.0-U6.8 — 2026-04-27
- TRYAGAIN pool imported — 45TB intact — 2026-04-27
- Plex migrated from FreeNAS jail to Docker on mediastack-deb — 2026-04-27
- Kasm added to Tailnet (Tailscale IP 100.80.14.29) — 2026-04-27

### mediastack-deb (192.168.1.36)
- mediastack-deb root disk expanded 30GB → 164GB — 2026-04-09
- qBittorrent + Gluetun (Surfshark WireGuard VPN) deployed — 2026-04-18
- SABnzbd, Sonarr, Radarr, Lidarr, Mylar, Prowlarr wired to download clients — 2026-04-18
- Homepage dashboard deployed (port 9898) with widgets for all services — 2026-04-18
- Unpackerr deployed and wired to Sonarr/Radarr/Lidarr — 2026-04-18
- Dead Prowlarr indexers cleaned up — 2026-04-18
- api_keys.env created documenting all service API keys — 2026-04-18

### Homepage Dashboard Widgets (all working)
- Sonarr, Radarr, Lidarr, Prowlarr, Mylar, SABnzbd, qBittorrent, Plex, Audiobookshelf
- Gitea, OctoPrint, Grafana, Zabbix, Uptime Kuma, Portainer
- Proxmox shardik + maturin (fixed SSL verify + token auth format)
- Pi-hole, Caddy (link only), Kasm (link only), Snipe-IT (link only), Vaultwarden (link only)

### RomM / Gaming
- RomM deployed on mediastack-deb — 2026-04-18
- ROM folder structure fixed — platform slugs: ngc, nds, 3ds, dc, arcade, snes, genesis, saturn, psp, gamegear, segacd — 2026-04-18/May-10
- PLAYMATCH_API_ENABLED=true, disable_hashing=true configured — 2026-04-18
- Sega CD games converted from ISO+MP3 to CHD format — 2026-04-18
- Fire Emblem New Mystery patched to English (xdelta3, FE12 v3.01) — 2026-05-10
- Skraper run complete — all 12 platforms scraped — 2026-05-10
- ROM library expanded to ~300 games across 12 platforms — 2026-05-10
- LaunchBox 13.26 installed on temerant-win, all platforms imported — 2026-05-15

---
## May 2026

### 2026-05-10 — Major Monitoring & Fleet Day

#### monitor-deb (192.168.1.29)
- monitor-deb VM deployed — Homepage, Zabbix, Grafana, Uptime Kuma — 2026-05-10
- Prometheus + node-exporter + PVE-exporter + cAdvisor deployed — 2026-05-10
- Node Exporter Full, cAdvisor, Proxmox dashboards imported to Grafana — 2026-05-10
- Zabbix added as Grafana data source — 2026-05-10
- Monitoring configs pushed to Gitea (cos/monitor-deb) — 2026-05-10
- monitor-deb root LV expanded 15GB → 30GB — 2026-05-10

#### Fleet / Ansible
- Portainer agent deployed fleet-wide — 2026-05-10
- All Docker hosts registered in Portainer (8 environments) — 2026-05-10
- Copy Fail CVE-2026-31431 patched fleet-wide — 2026-05-10
- snipeit-deb LXC destroyed (Snipe-IT moved to plow-rpm) — 2026-05-10
- Dead inventory entries removed (grafana-docker-deb, ubuntu-ansible-deb, apache-deb) — 2026-05-10

#### mediastack-deb
- Kometa deployed on mediastack-deb with TMDB and Trakt — 2026-05-10
- mediastack-deb RAM doubled to 16GB — 2026-05-10
- RomM cleanup complete — orphaned resources, WebP, segacd rescan, filenames — 2026-05-10/15

### 2026-05-15 — Security, Indexers, Documentation

- Dirty Frag CVE-2026-43284/43500 mitigated fleet-wide (disabled esp4/esp6/rxrpc) — 2026-05-15
- FlareSolverr deployed on mediastack-deb (port 8191), wired to Prowlarr — 2026-05-15
- 1337x added to Prowlarr via FlareSolverr — 2026-05-15
- KickassTorrents.ws added to Prowlarr — 2026-05-15
- Kometa Trakt + MDBList configured — 2026-05-15
- Ansible interpreter_python warnings silenced (auto_silent) — 2026-05-15
- Renamed typo'd MkDocs files (git_nfo.md → git_info.md, mdeiastack_apps.md → mediastack_apps.md) — 2026-05-15
- mediastack_apps.md overhauled with deployment status table — 2026-05-15
- ZFS recovery failed on shardik — node rebuilt, ZFS masked off (systemd.mask=zfs-mount.service) — 2026-05-15
- VMs 101/106/107 rebuilt from scratch — 2026-05-15
- Swarm VMs 102/104/105 migrated from maturin → shardik SDA_store — 2026-05-15

### 2026-05-16 — Proxmox Recovery, NVMe, rocky-rpm

#### Proxmox / shardik
- Proxmox pvedaemon/pveproxy restored on shardik via apt full-upgrade (Perl dependency conflict) — 2026-05-16
- noVNC console working on shardik after full-upgrade — 2026-05-16
- SDB_store and SDC_store formatted (ext4) and mounted on shardik — 2026-05-16

#### maturin
- BIOS SATA mode changed from RAID to AHCI — 2026-05-16
- Samsung 980 Pro 1TB NVMe installed in M.2 slot — 2026-05-16
- nvme_store dir storage pool created at /mnt/nvme_store — 2026-05-16
- QEMU upgraded via full-upgrade to support pc-i440fx-11.0 machine type — 2026-05-16
- vzdump.conf tmpdir set to /mnt/nvme_store on maturin — 2026-05-16
- Kasm disk moved from local-lvm → nvme_store (freed 23GB on root) — 2026-05-17

#### rocky-rpm (VM 109)
- Rebuilt from scratch — Rocky 9.7 minimal, IP 192.168.1.20 — 2026-05-16
- EPEL installed — 2026-05-16
- Onboarded: homelab_baseline, fail2ban, Dirty Frag mitigation, Zabbix agent — 2026-05-16

#### Documentation
- MkDocs nav reorganized into sections — 2026-05-16
- network_context.md fully rewritten — 2026-05-16
- hw_inv.md updated — 2026-05-16
- /etc/hosts cleaned, sorted, synced to router reservations — 2026-05-16
- inventory_auto cleaned — removed duplicate linux/debian/redhat groups — 2026-05-16
- Network diagram overhauled — Proxmox topology, no duplicates — 2026-05-16

### 2026-05-17 — VM Load Balancing, Backups, Final State

#### VM Migrations
- Migrated mediastack-deb (113) shardik → maturin nvme_store — 2026-05-16/17
- Migrated monitor-deb (101) shardik → maturin nvme_store — 2026-05-17
- Migrated docker-deb (107) shardik → maturin nvme_store — 2026-05-17
- Migrated git-ansible (106) shardik → maturin nvme_store — 2026-05-17
- Migrated alma-rpm (108) maturin → shardik SDA_store — 2026-05-17
- Migrated rocky-rpm (109) maturin → shardik SDA_store — 2026-05-17
- Migrated kasm-2404-deb (111) maturin → shardik SDA_store (live migration) — 2026-05-17
- Migrated pihole-book-deb (110 LXC) maturin → shardik local-lvm — 2026-05-17

**Final VM layout:**
- Maturin: 101 monitor-deb, 106 git-ansible, 107 docker-deb, 113 mediastack-deb
- Shardik: 108 alma-rpm, 109 rocky-rpm, 110 pihole-book-deb, 111 kasm-2404-deb, 102/104/105 swarm (stopped)

#### Backups
- Cross-node backup strategy: maturin VMs → shardik SDC_store; shardik VMs → shardik SDB_store — 2026-05-17
- Scheduled backup jobs: shardik VMs @ 2am, maturin VMs @ 3am, maxfiles=2 — 2026-05-17
- Proxmox /etc/pve config backup via rsync to git-ansible daily @ 4am — 2026-05-17
- Manual backups of all VMs completed — 2026-05-17
- Old 2025 backup files purged from SDA_store and DIR_SDA — 2026-05-17

#### Other
- SDD drive (Z4D2EJ31, Seagate ST6000VN0001) condemned — 24 pending/uncorrectable sectors — 2026-05-17
- Swarm VMs (102/104/105) onboot=0, kept stopped — 2026-05-17
- Kasm added to Homepage dashboard (Infrastructure section) — 2026-05-17
- Direct SSH backdoor confirmed to mediastack-deb (cos@192.168.1.36) — 2026-05-17
- SMART health audit of all shardik drives completed — 2026-05-17
