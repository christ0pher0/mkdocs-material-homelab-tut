# Homelab Completed Work Log
_Last updated: 2026-07-12_
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
### 2026-05-18 — PBS, Backups, Fleet, Monitoring, Shardik
#### Proxmox Backup Server
- PBS 4.2 VM (115) deployed on shardik — 192.168.1.4 — 2026-05-18
- SDD datastore (5.65TB, ST6000DX000 Z4D07FQ5) configured on PBS — 2026-05-18
- PBS added as datacenter-level storage to both Proxmox nodes — 2026-05-18
- qemu-guest-agent installed on all VMs fleet-wide (101,106,107,108,109,110,111,113) — 2026-05-18
- Proxmox backup mode changed from stop → snapshot on all jobs — 2026-05-18
- Maturin backup job migrated to PBS (101,106,107,113) @ 03:00 — 2026-05-18
- Shardik backup job migrated to PBS (102,104,105,108,109,110,111) @ 02:00 — 2026-05-18
- Manual backup of all 11 VMs/containers completed — 182GB, 0 failures — 2026-05-18
- Prune policy set: 3 daily, 1 weekly, 1 monthly, 1 yearly — 2026-05-18
- SDD /mnt/SDD added to /etc/fstab on pbs-deb — persistent across reboots — 2026-05-18
- Old vzdump jobs deleted, SDC_store cleared — 2026-05-18
- Enterprise repo disabled on pbs-deb, no-subscription repo enabled — 2026-05-18
- pbs-deb onboarded to Ansible inventory (debian group, 192.168.1.4) — 2026-05-18
#### Proxmox Config Backup
- proxmox-metal-configs Gitea repo created (private) — 2026-05-18
- proxmox_config_backup.yml Ansible playbook deployed to shardik, maturin, pbs-deb — 2026-05-18
- Daily config backup timer @ 04:00 — commits /etc/pve, interfaces, hosts, fstab to Gitea — 2026-05-18
#### Fleet / Monitoring
- Fleet timezone set to America/New_York via set_timezone.yml — 2026-05-18
- node-exporter deployed to pihole-book-deb and restic-deb — 2026-05-18
- portainer_sync.py written — auto-registers Docker hosts in Portainer daily @ 06:00 — 2026-05-18
- Portainer API token regenerated (ptr_0AHPtJ...) — 2026-05-18
- onboard_host.yml updated — qemu-guest-agent for KVM VMs (Debian + RedHat) — 2026-05-18
- set_timezone.yml playbook added to ansible_dev — 2026-05-18
#### Shardik / Drives
- shardik RAM instability resolved — XMP/DOCP disabled, running at 2133MHz stock — 2026-05-18
- BIOS confirmed latest (P10.43, June 2025) on ASRock AB350M Pro4 — 2026-05-18
- ST6000DX000 Z4D07FQ5 installed, formatted, used as PBS SDD datastore — 2026-05-18
- ST6000VN0001 Z4D2EJ31 (72 bad sectors) retired and removed — 2026-05-18
- Toshiba 96S1KBE2F56D ICRC errors persist — backplane connector suspected — 2026-05-18
#### TrueNAS
- ada4 (OOS20000G 00013AJR) identified as FAULTED — 57 read errors, 3 pending sectors — 2026-05-18
- TRYAGAIN scrub completed — repaired 1.11M, 0 data errors — 2026-05-18
- Boot pool DEGRADED — da0 USB boot drive confirmed dead — 2026-05-18
#### MkDocs / Checkbox Persistence
- UTF-8 triple-encoding bug fixed in todo.md — 2026-05-18
- checkbox_persist.js fixed: UTF-8 safe base64, correct MkDocs Material inverted checkbox logic, preventDefault on checkbox click — 2026-05-18
- webhook.py systemd service deployed on git-ansible (port 9999) — 2026-05-18
#### Restic-deb
- restic-deb confirmed at 192.168.1.40 (Ubuntu 26.04, formerly eld/Windows) — 2026-05-18
- node-exporter deployed — 2026-05-18
- RAM confirmed 16GB DDR3 (4x4GB) — upgrade to 32GB pending parts — 2026-05-18
#### Migrated from todo (completed)
- Migrate eld to Ubuntu 26.04 ✅
- Deploy Restic — automated backups from TrueNAS (Tier 1) ✅
- Deploy node-exporter to non-Docker hosts (plow-rpm, pihole-book-deb, restic-deb) ✅
- Write portainer_sync.py scheduled task ✅
- Fix TLS registration API issue in portainer_sync.py ✅

## June 2026
### 2026-06-01 — Plex Media / Live From Daryl's House
#### TV Archive Drive Workflow (restic-deb)
- Update backup date: `~/scripts/update_backup_date.sh LABEL`
- Update stats + docs: `~/scripts/cru_stats.sh && ~/scripts/backup_drives_update.sh`
- Relabel: umount → `ntfslabel --force` → remount via `cru_mount.sh`
- Fix table mismatches on git-ansible via `sed` in `~/material/mkdocs_dev_material/docs/backup_drives.md`
- TV_H-L drive label: `h-l`
#### Live From Daryl's House — Plex Rebuild
- All 41 segmented episode directories (FLV/MOV) converted to single MKV files — Season 01
- Single-file non-MKV episodes (FLV/MOV/MP4/TS) remuxed to MKV — Season 01
- Season 04 (2023 YouTube episodes E85-E91) downloaded, segmented, and concatted
- Season 02 and Season 03 folders created and populated
- Missing Season 01 episodes (E03-E74, E83-E84) downloaded from official YouTube channel
- All episodes forced to H.264 via yt-dlp format filter
- `all2mkv.sh` — batch FLV/MOV/MP4 concat script (restic-deb: `~/scripts/`)
- `lfdh_missing.sh` — YouTube download + concat script with skip-check (mediastack-deb: `~/mediastack/scripts/`)
- CRU TV_H-L drive synced via `rsync --delete` — 57GB

## 2026-06-19 — Physical Rebuild, Aslan Recovery & Storage Audit
### Physical / Workstation
- Workstation area torn down and rewired — 2026-06-19
- Cables consolidated and cleaned up — 2026-06-19
- Aslan and maturin repositioned at desk — 2026-06-19
- Rakdos rack (3D printed red Pi rack) deployed on desk — 2026-06-19
- pi2-deb (192.168.1.121, RPi Model B, DietPi, MQTT broker) confirmed up in Rakdos rack — 2026-06-19
### Proxmox / Fleet
- Maturin web UI login resolved — 2026-06-19
- Shardik down (non-critical, left for later) — 2026-06-19
- Ping sweep confirmed 20 hosts up — 2026-06-19
### Aslan — Storage & VM Audit
- Full storage audit of aslan completed — 2026-06-19
- sdb (12TB WD WD120EMAZ) has 141 ATA UNC errors at LBA 0x003a5970, 12 reallocated sectors, 22 offline uncorrectable — 2026-06-19
- Decision: docker-deb scsi1 (2TB YouTube downloads) left on sdb as canary — expendable data — 2026-06-19
- Long SMART test queued on sdb — check results 2026-06-20 — 2026-06-19
- nvme_store on aslan is NOT a real mount — just a folder on pve-root (ORICO SSD). Samsung 980 Pro NVMe is on maturin, not aslan — 2026-06-19
- kasm-2404-deb (VM 111) local-lvm disk was at 99.99% full — moved scsi0 to hdd3tb, thinpool freed from 2% to 0.17% — 2026-06-19
### Aslan VM Layout (current)
- 102/104/105 swarm01-03 — stopped, SDA_store
- 107 docker-deb — running, boot: nvme_store (pve-root/ORICO), data: hdd12tb (2TB canary)
- 108 alma-rpm, 109 rocky-rpm — running, SDA_store
- 111 kasm-2404-deb — stopped, hdd3tb
- 115 pbs — running, SDA_store

## Swept 2026-06-28
- [x] Fix onboard NIC (alc0) — confirmed dead (AR8161, alc driver, hours spent). Install Intel X540-T2 PCIe NIC instead (Sunday Project #7)
- [x] Upgrade CPU: Ryzen 7 2700X — ✅ COMPLETE 2026-06
- [x] Upgrade RAM to 64GB DDR4 — ✅ COMPLETE 2026-06
- [x] Shardik hardware upgrade (CPU 2700X, RAM to 64GB) — complete 2026-06
- [x] Router/AP rewire — complete
- [x] Beryl AP setup — GL-MT3000 configured in AP mode, 192.168.1.10, extending Greyhawk WiFi (2026-06-15)
- [x] idee-deb → aslan Proxmox hypervisor — complete 2026-06-16
- [x] restic-deb → blaine-pve — complete 2026-06-22. Blaine joined cluster, onboarded via onboard2.yml. restic-deb rebuilt as VM on blaine.
- [x] Pi rack installed — 6 Pis mounted and running 2026-06-28. Batocera off-rack (powers on for gaming only).
- [x] TrueNAS boot-pool mirror complete — da0 (SanDisk) + da1 (Kingston), bootloader written 2026-06-28, scrub clean.

## 2026-07-05 — Telegram Alerting + Monitoring Wins
- Telegram bot (OerthBot) fully deployed and verified — notify_telegram.py + /etc/oerthbot/config.json (mode 600), admin of OerthChannel
- weekly_patch.yml Telegram integration — per-host reboot/failure alerts + run-complete ping, live-tested against git-ansible-deb
- Kuma → Telegram wired on monitor-deb and backup-dietpi-deb (apply to all monitors)
- cru_stats.sh / backup_drives_update.sh path mismatch — fixed, Alex signed off, Sam shipped
- STL rsync throughput — ~400kB/s → 25MB/s (~60x), no longer a viability crisis
- VPN rationalization decided: Tailscale only, WireGuard + ZeroTier to be decommissioned
- blank-dietpi-deb renamed docs-dietpi-deb
- garuda confirmed as pve3's hostname

## 2026-07-11/12 — Power Outage Recovery & Plex Library Reorg
### Power Outage
- Ping sweep confirmed all hosts survived except blaine (192.168.1.11) — 2026-07-11
- Plex container recovered — exited (255) mid-task from abrupt power loss, no corruption, clean `docker start` — 2026-07-11
- Blaine traced to VT-x disabled in BIOS (same signature as shardik's earlier CMOS/BIOS reset) — physically re-enabled, confirmed via `/proc/cpuinfo` — 2026-07-12
- restic-deb (VM 100 on blaine) was stopped after the BIOS fix — restarted, confirmed running — 2026-07-12
### Plex Library Reorg (mediastack-deb)
- All Plex libraries consolidated from scattered root folders (Movies, TV, Music420, AudioBooksPlex, Training, Photos) into `Plex_Libraries` on the TrueNAS `plex` share — 2026-07-11
- docker-compose.yml updated: Plex, Sonarr, Radarr, Lidarr, Audiobookshelf volume mounts repointed to `Plex_Libraries` subfolders — 2026-07-11
- Music/Audiobooks required nested subfolder correction (`Music/Music_Plex`, `Audiobooks/AudioBooksPlex`) — parent folders had mixed non-Plex content — 2026-07-11
- Downloads folder moved to `Plex_Libraries/downloads`, compose updated across 7 containers (sabnzbd, qBittorrent, Sonarr, Radarr, Lidarr, Mylar, Unpackerr) — 2026-07-12
- Comics moved to `READING_0726/Comics` — Mylar and Komga repointed — 2026-07-12
- ROMs moved to `EMULATION/ROMs` (with `bios` subfolder) — RomM repointed — 2026-07-12
### TrueNAS Root Share Cleanup (freenas-bsd)
- Old empty post-reorg folders removed from `/mnt/plex` root — 2026-07-12
- `TRYAGAIN/plex/PLEX` — empty ZFS dataset since 2022, confirmed no snapshots, destroyed — 2026-07-12
- Root folder count reduced from ~17 to 12 — 2026-07-12
### Jellyfin (tools-deb, native install — separate from Docker stack)
- Library root `.mblink` files (Movies, TV, AudioBooksPlex) still referenced pre-reorg paths — updated to `Plex_Libraries` equivalents — 2026-07-12
- Discovered CIFS mount to the `plex` share was inactive on this host (outage casualty, plain `_netdev` fstab entry with no systemd automount fallback) — remounted via `mount -a` — 2026-07-12
- Full library rescan triggered via API after mount fix — 2026-07-12
### rclone (homelasb scripts, mediastack-deb / amontillado)
- mz4250 source folder renamed on Google Drive side (monthly naming) — updated script to "July 2026" — 2026-07-12
- Destination paths repointed into STL folder structure (mz4250, mz4250 remixes, BRITE, HeroQuest → STL/SOURCE_MATERIAL/HeroQuest) — 2026-07-12
- Throttled concurrency (`--transfers=4 --checkers=4 --tpslimit=8`) after hitting Google Drive shared quota (`rateLimitExceeded`) — 2026-07-12
- Script hardened with `cd /d %~dp0` to always run from its own folder — 2026-07-12
### Homepage / Ollama (monitor-deb, babar)
- babar (192.168.1.12, 5th Proxmox wheel node, added 2026-07-08) was missing from Homepage dashboard entirely — added Proxmox node entry — 2026-07-12
- Ollama (LXC 102 on babar) confirmed healthy but bound to `127.0.0.1` only — added systemd override for `OLLAMA_HOST=0.0.0.0:11434`, now reachable at 192.168.1.169:11434 — added to Homepage as new AI section — 2026-07-12
