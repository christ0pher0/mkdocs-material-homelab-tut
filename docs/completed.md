# Homelab Completed Work Log
_Last updated: 2026-05-17_

---
## Proxmox / Infrastructure

### Cluster "wheel" (shardik + maturin + QDevice)
- Built 2-node wheel cluster — shardik + maturin — 2026-05-10
- QDevice on git-ansible for quorum — 2026-05-10
- Painful node rename (proxmox-deb → shardik, pve2 → maturin) requiring SQLite surgery on config.db — 2026-05-10
- ZFS recovery failed on shardik — rebuilt node, ZFS masked off (systemd.mask=zfs-mount.service) — 2026-05-15
- Proxmox services restored on shardik — full-upgrade fixed Perl dependency conflict — 2026-05-16
- noVNC console working on shardik after full-upgrade — 2026-05-16
- Swarm VMs (102/104/105) onboot=0, kept stopped — 2026-05-17

### VM Load Balancing (2026-05-16 to 2026-05-17)
- Migrated mediastack-deb (113) shardik → maturin nvme_store — 2026-05-16
- Migrated monitor-deb (101) shardik → maturin nvme_store — 2026-05-16
- Migrated docker-deb (107) shardik → maturin nvme_store — 2026-05-16
- Migrated git-ansible (106) shardik → maturin nvme_store — 2026-05-17
- Migrated alma-rpm (108) maturin → shardik SDA_store — 2026-05-17
- Migrated rocky-rpm (109) maturin → shardik SDA_store — 2026-05-17
- Migrated kasm-2404-deb (111) maturin → shardik SDA_store — 2026-05-17
- Migrated pihole-book-deb (110 LXC) maturin → shardik local-lvm — 2026-05-17
- Final layout: maturin = core services; shardik = utility/test VMs — 2026-05-17

### Backup Strategy
- SDB_store and SDC_store formatted and mounted on shardik — 2026-05-17
- Cross-node backup strategy implemented — maturin VMs → shardik SDC_store; shardik VMs → shardik SDB_store — 2026-05-17
- Scheduled backup jobs: shardik VMs @ 2am, maturin VMs @ 3am, maxfiles=2 — 2026-05-17
- Proxmox /etc/pve config backup via rsync to git-ansible daily @ 4am — 2026-05-17
- Old 2025 backup files purged from SDA_store and DIR_SDA — 2026-05-17

### VM Rebuilds
- Rebuilt monitor-deb (101) — 2026-05-15
- Rebuilt git-ansible (106) — 2026-05-15
- Rebuilt docker-deb (107) — 2026-05-15
- Rebuilt rocky-rpm (109) — Rocky 9.7 minimal, IP 192.168.1.20 — 2026-05-16

---
## Maturin (192.168.1.7)
- Upgraded RAM to 32GB DDR4 — 2026-05-10
- Changed SATA mode from RAID to AHCI in BIOS — 2026-05-16
- Samsung 980 Pro 1TB NVMe installed in M.2 slot — 2026-05-16
- nvme_store dir storage pool created at /mnt/nvme_store — 2026-05-16
- vzdump.conf tmpdir set to /mnt/nvme_store — 2026-05-17
- QEMU upgraded via full-upgrade to support pc-i440fx-11.0 machine type — 2026-05-16
- Kasm disk moved from local-lvm to nvme_store (freed 23GB on root) — 2026-05-17

---
## Shardik (192.168.1.2)
- ZFS masked off — 2026-05-15
- SDD drive (Z4D2EJ31, Seagate ST6000VN0001) condemned — 24 pending/uncorrectable sectors, 2436 CRC errors — 2026-05-17
- SDB_store formatted ext4, used for shardik VM backups — 2026-05-17
- SDC_store formatted ext4, used for maturin VM backups — 2026-05-17

---
## Maturin — Core Services
- monitor-deb (192.168.1.29): Grafana, Zabbix, Uptime Kuma, Homepage, Prometheus — deployed 2026-05-10
- docker-deb (192.168.1.34): Portainer, Vaultwarden, Caddy — deployed 2026-05-10
- mediastack-deb (192.168.1.36): full arr-stack, Plex, RomM — deployed 2026-05-10
- git-ansible (192.168.1.3): Ansible control, MkDocs, Gitea — running

---
## Mediastack (192.168.1.36)
- Full arr-stack deployed: Sonarr, Radarr, Lidarr, Mylar, Prowlarr, SABnzbd, qBittorrent via Gluetun — 2026-05-10
- Kometa deployed and configured with Trakt + MDBList — 2026-05-10/15
- FlareSolverr deployed (port 8191), wired to Prowlarr — 2026-05-15
- Unpackerr deployed and wired to Sonarr/Radarr/Lidarr — 2026-05-15
- 1337x and KickassTorrents.ws added to Prowlarr — 2026-05-15
- Dead indexers cleaned from Prowlarr — 2026-05-15
- Direct SSH backdoor confirmed (cos@192.168.1.36) — 2026-05-17

---
## RomM / Gaming
- RomM deployed on mediastack-deb — 2026-05-10
- ROM folder structure cleaned — renamed to IGDB slugs — 2026-05-10
- Skraper run against all 12 platforms — 2026-05-10
- RomM cleanup — orphaned resources, WebP conversion, segacd rescan, unidentified games, Dragon_warrior filenames — 2026-05-15
- LaunchBox 13.26 installed on temerant-win, all platforms imported — 2026-05-15

---
## Vaultwarden / Remote Access
- Vaultwarden deployed behind Caddy + Tailscale TLS on port 8443 — 2026-05-10
- Accessible at https://docker-deb.taild502ad.ts.net:8443

---
## Monitoring
- Homepage, Zabbix, Grafana, Uptime Kuma deployed on monitor-deb — 2026-05-10
- Prometheus + node-exporter + PVE-exporter + cAdvisor deployed — 2026-05-10
- Node Exporter Full, cAdvisor, Proxmox dashboards imported to Grafana — 2026-05-10
- Zabbix added as Grafana data source — 2026-05-10
- Portainer agent fleet-wide, all Docker hosts registered — 2026-05-10
- Monitoring configs pushed to Gitea (cos/monitor-deb) — 2026-05-10
- Kasm added to Homepage Infrastructure section — 2026-05-17

---
## Ansible / Documentation
- Dirty Frag mitigation (CVE-2026-43284/43500) — disable esp4/esp6/rxrpc fleet-wide — 2026-05-15
- Ansible interpreter_python warnings silenced (auto_silent) — 2026-05-15
- MkDocs nav reorganized into sections — 2026-05-16
- network_context.md fully rewritten — 2026-05-16
- hw_inv.md updated — 2026-05-16
- Renamed typo'd MkDocs files (git_nfo.md, mdeiastack_apps.md) — 2026-05-15
- mediastack_apps.md overhauled with deployment status table — 2026-05-15
- /etc/hosts cleaned, sorted, synced to router reservations — 2026-05-16
- inventory_auto cleaned — removed duplicate linux/debian/redhat groups — 2026-05-16
- Network diagram overhauled — Proxmox topology, no duplicates — 2026-05-16

---
## rocky-rpm (192.168.1.20, VM 109)
- Rebuilt from scratch on maturin nvme_store — Rocky 9.7 minimal — 2026-05-16
- EPEL installed — 2026-05-16
- Onboarded: homelab_baseline, fail2ban, Dirty Frag mitigation, Zabbix agent — 2026-05-16
- IP set to 192.168.1.20, hostname set to rocky-rpm — 2026-05-16

