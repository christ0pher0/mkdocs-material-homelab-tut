# Network Context Document
_Paste this at the start of any new Claude session to provide homelab context._
_Last updated: 2026-05-17_
---
## Network Overview
- **ISP:** FIOS (fiber ONT)
- **Router/Firewall:** GL.iNet Flint 2 (192.168.1.1) — OpenWrt-based, AdGuard Home enabled
- **Secondary firewall:** Netgate (192.168.1.6) — pfSense
- **Proxmox Cluster:** "wheel" — 2-node cluster with QDevice
  - **shardik** (192.168.1.2) — AMD Ryzen 5 1600, 62GB RAM, ASRock AB350M Pro4 — primary hypervisor
  - **maturin** (192.168.1.7) — Dell OptiPlex 7050 SFF, SATA SSD — secondary hypervisor
  - **QDevice:** git-ansible-deb (192.168.1.3)
- **NAS:** TrueNAS CORE 13.0-U6.8 (192.168.1.5) — ~45TB TRYAGAIN pool, CIFS shares, USB NIC (ue0)
- **Subnet:** 192.168.1.0/24
- **DNS:** AdGuard Home on router + PiHole (192.168.1.33)
- **Monitoring:** monitor-deb (192.168.1.29) — Homepage, Zabbix, Grafana, Uptime Kuma, Prometheus, node-exporter, PVE-exporter, cAdvisor
- **Ansible control node:** git-ansible-deb (192.168.1.3)
- **Tailscale tailnet:** coshaughnessy@
- **VPN:** Surfshark WireGuard (via Gluetun on mediastack-deb)
---
## IP Schema
| Range   | Purpose                          |
|---------|----------------------------------|
| 1–19    | Infrastructure (router, Proxmox, NAS, network gear) |
| 20–49   | Debian/Ubuntu servers, VMs, LXCs |
| 50–69   | RPM servers (Rocky, Alma, RHEL)  |
| 100–119 | Windows workstations             |
| 120–139 | Raspberry Pis                    |
| 140–159 | TVs, media devices               |
| 160–179 | Peripherals, printers, IoT       |
| 200–249 | Mobile, Android devices          |
| 250+    | Special, reserved, virtual IPs   |
---
## Full Host Inventory
### Infrastructure (1–19)
| IP          | Hostname        | OS/Type              | Role                                      | Status  |
|-------------|-----------------|----------------------|-------------------------------------------|---------|
| 192.168.1.1 | router-net      | GL.iNet Flint 2      | Router, AdGuard Home, WireGuard VPN       | Online  |
| 192.168.1.2 | shardik         | Debian 12 (PVE)      | Proxmox node 1 — primary hypervisor       | Online  |
| 192.168.1.3 | git-ansible-deb | Ubuntu 24.04         | Ansible control, MkDocs, Gitea, QDevice   | Online  |
| 192.168.1.5 | freenas-bsd     | TrueNAS CORE 13.0    | NAS — ~45TB TRYAGAIN pool, CIFS shares    | Online  |
| 192.168.1.6 | netgate-net     | pfSense              | Secondary firewall/router                 | Online  |
| 192.168.1.7 | maturin         | Debian 12 (PVE)      | Proxmox node 2 — secondary hypervisor     | Online  |
### Debian/Ubuntu Servers (20–49)
| IP           | Hostname        | OS           | Virt    | Role                                          | Status  |
|--------------|-----------------|--------------|---------|-----------------------------------------------|---------|
| 192.168.1.22 | swarm01-deb     | Ubuntu 24.04 | KVM     | Docker Swarm manager (VM 102, shardik)        | Online  |
| 192.168.1.23 | swarm02-deb     | Ubuntu 24.04 | KVM     | Docker Swarm worker (VM 104, shardik)         | Online  |
| 192.168.1.24 | swarm03-deb     | Ubuntu 24.04 | KVM     | Docker Swarm worker (VM 105, shardik)         | Online  |
| 192.168.1.26 | kasm-2404-deb   | Ubuntu 24.04 | KVM     | Kasm Workspaces 1.17.0 (VM 111, maturin)     | Online  |
| 192.168.1.27 | urnst-deb       | Debian 13    | Physical| Role TBD                                      | Offline |
| 192.168.1.28 | idee-deb        | Debian       | Physical| GPU node — GTX 1080 Ti (role TBD)             | Offline |
| 192.168.1.29 | monitor-deb     | Debian 12    | KVM     | Monitoring stack (VM 110, maturin)            | Online  |
| 192.168.1.33 | pihole-book-deb | Debian 12    | LXC     | Pi-hole DNS (1 core, 512MB RAM, maturin)      | Online  |
| 192.168.1.34 | docker-deb      | Ubuntu 24.04 | KVM     | Docker host — Portainer, Vaultwarden, Traefik (VM 107, shardik) | Online |
| 192.168.1.35 | 2404HV-deb      | Ubuntu 24.04 | Hyper-V | Hyper-V Ubuntu VM (i7-13700K, 12 cores)       | Online  |
| 192.168.1.36 | mediastack-deb  | Ubuntu 24.04 | KVM     | Full media stack — 17 Docker containers (VM 113, shardik) | Online |
| 192.168.1.40 | restic-deb      | Debian       | Physical| Backup host — Restic                          | Online  |
### RPM Servers (50–69)
| IP           | Hostname  | OS            | Virt    | Role                         | Status |
|--------------|-----------|---------------|---------|------------------------------|--------|
| 192.168.1.20 | rocky-rpm | Rocky 9.7     | KVM     | Rocky Linux (VM 109, maturin)| Online |
| 192.168.1.52 | alma-rpm  | AlmaLinux 9.7 | KVM     | AlmaLinux (VM 108, maturin)  | Online |
| 192.168.1.53 | plow-rpm  | RHEL 9.6      | Hyper-V | RHEL VM (i7-13700K), Snipe-IT| Online |
### Windows Workstations (100–119)
| IP            | Hostname         | Notes                                    | Status      |
|---------------|------------------|------------------------------------------|-------------|
| 192.168.1.100 | amontillado-win  | Main Windows 11 desktop                  | Online      |
| 192.168.1.101 | eld-win          | Windows workstation — backup target      | Online      |
| 192.168.1.103 | todash-win       | Windows workstation                      | Online      |
| 192.168.1.105 | temerant-win     | Windows 11 — LaunchBox, ROM gaming       | Online      |
| 192.168.1.106 | fortunato-win    | Hyper-V Windows VM (VM 106, shardik rebuilt) | Online  |
### Raspberry Pis (120–139)
| IP            | Hostname     | Notes                                | Status      |
|---------------|--------------|--------------------------------------|-------------|
| 192.168.1.122 | octopi-deb   | OctoPrint — 3D printer control       | Online      |
| 192.168.1.123 | batocera-deb | Batocera retro gaming                | Online      |
| 192.168.1.125 | pi5-deb      | Raspberry Pi 5                       | Online      |
### TVs / Media (140–159)
| IP            | Hostname    | Notes        | Status      |
|---------------|-------------|--------------|-------------|
| 192.168.1.140 | tv1-media   | TV           | Online      |
| 192.168.1.141 | tv2-media   | TV           | Online      |
### Peripherals / IoT (160–179)
| IP            | Hostname         | Notes                  | Status      |
|---------------|------------------|------------------------|-------------|
| 192.168.1.162 | dell-printer-net | Dell 2155cdn Color MFP | Offline     |
### Mobile / Android (200–249)
| IP            | Hostname          | Notes              | Status      |
|---------------|-------------------|--------------------|-------------|
| 192.168.1.201 | pixel8-droid      | Google Pixel 8     | Mobile      |
| 192.168.1.202 | fire-tablet-droid | Amazon Fire Tablet | Online      |
| 192.168.1.203 | roomba-droid      | iRobot Roomba      | Online      |
### Special / Virtual (250+)
| IP            | Hostname         | Notes                    |
|---------------|------------------|--------------------------|
| 192.168.1.250 | swarm-shared-vip | Docker Swarm shared VIP  |
---
## Proxmox Cluster Detail
### shardik (192.168.1.2) — Node 1
**Hardware:** AMD Ryzen 5 1600 (6c/12t) | **RAM:** 62GB DDR4
**Motherboard:** ASRock AB350M Pro4 | **BIOS:** P10.43
**Note:** ZFS masked off (systemd.mask=zfs-mount.service) — ZFS recovery failed, node rebuilt

| Pool      | Type    | Notes                        |
|-----------|---------|------------------------------|
| local     | dir     | OS                           |
| local-lvm | lvmthin | VM storage                   |
| nvme_store | dir     | Samsung 980 Pro 1TB — fast VM storage (~960GB free) |
| SDA_store | dir     | Large VM storage (~4.8TB free)|
| SDB_store | dir     | Additional storage           |
| SDC_store | dir     | Additional storage           |
| SDD_store | dir     | Additional storage           |

| VMID | Name              | IP           | Status  | RAM  | Node    |
|------|-------------------|--------------|---------|------|---------|
| 101  | monitor-deb       | 192.168.1.29 | running | 4GB  | shardik |
| 102  | swarm01-manager   | 192.168.1.22 | running | 2GB  | shardik |
| 104  | swarm02-worker    | 192.168.1.23 | running | 2GB  | shardik |
| 105  | swarm03-worker    | 192.168.1.24 | running | 2GB  | shardik |
| 106  | git-ansible       | 192.168.1.3  | running | 4GB  | shardik |
| 107  | docker-deb        | 192.168.1.34 | running | 2GB  | shardik |
| 113  | mediastack-deb    | 192.168.1.36 | running | 16GB | shardik |

### maturin (192.168.1.7) — Node 2
**Hardware:** Dell OptiPlex 7050 SFF | **Storage:** 476GB SATA SSD (single disk)

| VMID | Name              | IP           | Status  | RAM  | Node   |
|------|-------------------|--------------|---------|------|--------|
| 108  | alma-rpm          | 192.168.1.52 | running | 2GB  | maturin|
| 109  | rocky-rpm         | 192.168.1.20 | running | 2GB  | maturin|
| 110  | pihole-book-deb   | 192.168.1.33 | running | 512MB| maturin|
| 111  | kasm-2404-deb     | 192.168.1.26 | running | 4GB  | maturin|
| 900  | ubuntu-24.04-template | —        | stopped | 1GB  | maturin|
---
## mediastack-deb Detail (192.168.1.36)
Proxmox VM 113 | Ubuntu 24.04 | 4 cores | 16GB RAM | shardik
Tailscale: 100.127.236.79

### Docker Containers
| Container      | Port  | Purpose                        |
|----------------|-------|--------------------------------|
| plex           | 32400 | Media server                   |
| sonarr         | 8989  | TV management                  |
| radarr         | 7878  | Movie management               |
| lidarr         | 8686  | Music management               |
| mylar          | 8091  | Comics downloader              |
| sabnzbd        | 8090  | Usenet downloader              |
| prowlarr       | 9696  | Indexer manager                |
| qbittorrent    | 8082  | Torrent client                 |
| seerr          | 5055  | Media requests                 |
| komga          | 8085  | Comics/ebooks reader           |
| audiobookshelf | 13378 | Audiobooks/podcasts            |
| romm           | 8998  | ROM manager (~300 games)       |
| kometa         | —     | Plex metadata/collections      |
| flaresolverr   | 8191  | Cloudflare bypass for Prowlarr |
| unpackerr      | —     | Archive extractor              |
| vpn (gluetun)  | —     | Surfshark WireGuard VPN        |
| mariadb        | —     | Database for RomM              |

NAS CIFS mounts at `/mnt/plex/*`: Music420, Movies, Comics, AudioBooksPlex, downloads, TV, Training, ROMs, Photos
---
## git-ansible-deb Detail (192.168.1.3)
Ubuntu 24.04 | Proxmox VM 106 on shardik | Tailscale: 100.68.195.68
Ansible core 2.20.4 | Python 3.12.3 | ansible.cfg: interpreter_python = auto_silent
Primary inventory: `~/ansible_dev/inventory_auto`
Playbooks: `~/ansible_dev/playbooks/`
Docs: `~/material/mkdocs_dev_material/` (MkDocs Material)
Gitea: port 3000
VS Code Server installed
---
## docker-deb Detail (192.168.1.34)
Ubuntu 24.04 | Proxmox VM 107 on shardik
Services: Portainer (central), Vaultwarden, Traefik, Caddy
Vaultwarden: https://docker-deb.taild502ad.ts.net:8443
Portainer agents deployed fleet-wide
---
## Tailscale Nodes
| Hostname               | Tailscale IP    | OS      | Status  |
|------------------------|-----------------|---------|---------|
| git-ansible-deb        | 100.68.195.68   | Linux   | Online  |
| mediastack-deb         | 100.127.236.79  | Linux   | Online  |
| kasm-2404-deb          | 100.80.14.29    | Linux   | Online  |
| amontillado            | 100.126.7.50    | Windows | Online  |
| pixel-8                | 100.110.116.11  | Android | Offline |
---
## Docker Swarm (.22–.24, VIP .250)
swarm01 (.22) — manager (VM 102, shardik) | swarm02 (.23) — worker (VM 104, shardik) | swarm03 (.24) — worker (VM 105, shardik)
Swarm VIP: 192.168.1.250
---
## Naming Conventions
| Type              | Convention              | Examples                              |
|-------------------|-------------------------|---------------------------------------|
| Proxmox nodes     | Dark Tower characters   | shardik, maturin                      |
| Linux servers     | Greyhawk D&D geography  | urnst-deb, idee-deb                   |
| Windows machines  | Literary references     | amontillado, eld, temerant (Kingkiller)|
| Cluster/nodes     | Dark Tower              | shardik, maturin                      |
---
## Security Status
| Issue                              | Status                              |
|------------------------------------|-------------------------------------|
| fail2ban                           | ✅ Deployed fleet-wide              |
| Dirty Frag CVE-2026-43284/43500    | ✅ Mitigated fleet-wide 2026-05-15  |
| Copy Fail CVE-2026-31431           | ✅ Patched fleet-wide 2026-05-10    |
| TrueNAS CORE EOL                   | ⚠️ Hardware rebuild planned         |
| ada4 bad sectors (TrueNAS)         | ⚠️ Investigate                      |
| pi1 SD card 91% full               | ⚠️ Replace SD card                  |
| eld D: drive 10% free              | ⚠️ Expand storage                   |
---
## Known Issues
- plow-rpm — xrdp/SELinux conflict blocking updates
- TrueNAS ue0 (USB NIC) — set to static .5 but may not survive reboots
- TrueNAS alc0 onboard NIC — broken
- Vaultwarden autofill port matching issue in browser extension
- Plex Music library fix for mobile — unresolved
---
_Last updated: 2026-05-17_

## Backup Strategy

| Source Node | VMs | Target Storage | Schedule | Retention |
|-------------|-----|----------------|----------|-----------|
| maturin | 101, 106, 107, 113 | shardik:SDC_store | 03:00 daily | 2 copies |
| shardik | 108, 109, 110, 111 | shardik:SDB_store | 02:00 daily | 2 copies |

Backup command (maturin VMs): `pvesh create /nodes/maturin/vzdump --vmid <id> --storage SDC_store --mode stop --compress zstd --tmpdir /mnt/nvme_store`


