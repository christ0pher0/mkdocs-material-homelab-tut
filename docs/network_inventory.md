# DIGIDIOT Network Inventory
_Last updated: 2026-06-28 — Generated from arp-scan + nmap -sV + masscan -p1-65535 + docker ps + qm/pct list + Hyper-V Manager_

---

## Network: 192.168.1.0/24
**30 hosts active** at time of scan.

---

## Physical Infrastructure

| IP | Hostname | Hardware | Role |
|----|----------|----------|------|
| 192.168.1.1 | router-net | GL-MT6000 Flint 2 (GL Technologies) | Router, OpenWrt, LuCI on :80/:8080 |
| 192.168.1.2 | shardik | ASRock AB350M Pro4, Ryzen 7 2700X, 64GB DDR4 | Proxmox node 1 — back online 2026-06-28 |
| 192.168.1.3 | git-ansible-deb | VM on maturin (see below) | Ansible control node, MkDocs, Gitea webhook |
| 192.168.1.5 | freenas-bsd | Realtek USB NIC (onboard dead) | TrueNAS CORE — TRYAGAIN pool |
| 192.168.1.7 | maturin | Dell OptiPlex 7050 SFF, i7-6700, 32GB DDR4 | Proxmox node 2 |
| 192.168.1.9 | aslan | Gigabyte AB350-Gaming 3-CF, Ryzen 5 1600X, 32GB DDR4 | Proxmox node 3, GTX 1080 Ti (vfio) |
| 192.168.1.10 | beryl-ap | GL-MT3000 Beryl AX (GL Technologies) | WiFi AP, OpenWrt, AP mode |
| 192.168.1.11 | blaine | Gigabyte mobo, i5-2500K, 30GB RAM | Proxmox node 4 |
| 192.168.1.100 | amontillado | MSI, Windows 11 | Primary workstation + Hyper-V host |

---

## Proxmox Cluster: wheel

### maturin (192.168.1.7) — VMs

| VMID | Name | IP | Status | RAM | Disk | Services |
|------|------|----|--------|-----|------|---------|
| 101 | monitor-deb | 192.168.1.29 | running | 4GB | 32GB | Grafana :3000, Uptime Kuma :3001, Homepage :3003, nginx :8080, cAdvisor :8081, Portainer agent :9001, node-exporter :9100, **Zabbix Server :10051**, Zabbix agent :10050, unknown :9221 |
| 106 | git-ansible-deb | 192.168.1.3 | running | 4GB | 64GB | SSH, Apache :80, MkDocs/WSGIServer :8000, webhook.py :9999, xrdp :3389 |
| 113 | mediastack-deb | 192.168.1.36 | running | 16GB | 150GB | Plex :32400 (host net), Sonarr :8989, Radarr :7878, Lidarr :8686, Mylar :8091, Komga :8085, Seerr :5055, SABnzbd :8090, qBittorrent :8082/:6881, Prowlarr :9696, FlareSolverr :8191, Audiobookshelf :13378, RomM :8998, Kometa, Unpackerr, WireGuard VPN :51820, node-exporter :9100, cAdvisor :8081, Portainer agent :9001 |
| 900 | ubuntu-24.04-template | — | stopped | 1GB | 32GB | Template only |

### aslan (192.168.1.9) — VMs

| VMID | Name | IP | Status | RAM | Disk | Services |
|------|------|----|--------|-----|------|---------|
| 102 | swarm01-manager | — | stopped | 2GB | 64GB | Docker Swarm manager (pending migration) |
| 104 | swarm02-worker | — | stopped | 2GB | 64GB | Docker Swarm worker |
| 105 | swarm03-worker | — | stopped | 2GB | 64GB | Docker Swarm worker |
| 107 | docker-deb | 192.168.1.34 | running | 8GB | 64GB | See Docker containers below |
| 108 | alma-rpm | 192.168.1.52 | running | 2GB | 32GB | SSH, Apache httpd :80, node-exporter :9100 |
| 109 | rocky-rpm | 192.168.1.20 | running | 2GB | 32GB | SSH only |
| 111 | kasm-2404-deb | — | stopped | 4GB | 32GB | KASM Workspaces (disk move pending) |
| 115 | pbs | 192.168.1.4 | running | 4GB | 32GB | Proxmox Backup Server UI :8007 (SSL) |

### aslan (192.168.1.9) — LXC

| VMID | Name | IP | Status | Services |
|------|------|----|--------|---------|
| 110 | pihole-book-deb | 192.168.1.33 | running | Pi-hole DNS :53, web UI :80/:443, node-exporter :9100 |

### blaine (192.168.1.11) — VMs

| VMID | Name | IP | Status | RAM | Disk | Services |
|------|------|----|--------|-----|------|---------|
| 100 | restic | 192.168.1.40 | running | 8GB | 64GB | SSH, Samba :139/:445, xrdp :3389 |

### shardik (192.168.1.2) — VMs

_No VMs currently deployed. Back online 2026-06-28. 1-month uptime target: 2026-07-28._

---

## docker-deb (192.168.1.34) — Docker Containers

| Container | Image | Port | Purpose |
|-----------|-------|------|---------|
| tubearchivist | bbilly1/tubearchivist | :8090 | YouTube archiver — 15 curated channels |
| archivist-es | elasticsearch:8.18.0 | internal | Tube Archivist backend |
| archivist-redis | redis/redis-stack-server | internal | Tube Archivist backend |
| manyfold-manyfold-1 | manyfold3d/manyfold | :3214 | 3D model manager |
| manyfold-db-1 | postgres:16 | internal | Manyfold backend |
| manyfold-redis-1 | redis:7-alpine | internal | Manyfold backend |
| node-exporter | prom/node-exporter | :9100 | Prometheus metrics |
| cadvisor | gcr.io/cadvisor/cadvisor | :8081 | Container metrics |
| portainer_agent | portainer/agent | :9001 | Portainer agent |
| caddy | caddy | :8088/:8444/:8443 | Reverse proxy |
| traefik | traefik | :80/:443/:8080 | Reverse proxy ⚠️ dual proxy — resolve with Riley |
| vaultwarden | vaultwarden/server | internal | Password manager (behind Caddy) |
| portainer | portainer/portainer-ce | :9443 | Container management UI |

---

## Hyper-V (amontillado — 192.168.1.100)
_Naming theme: Poe — "The Cask of Amontillado" characters_
_AD Domain: DIGIDIOT.local (controller: DIGIDIOTSERVER)_

| VM Name | IP | State | RAM | vCPUs | OS | Role |
|---------|----|-------|-----|-------|----|------|
| Fortunato-11 | — | Off | — | 2 | Windows 11 | Work VM — offline |
| Luchesi-240 | 192.168.1.103 | Running | 2.8GB | 12 | Windows 10 | LabVIEW + FlexLM license manager |
| RheL9-172 | 192.168.1.53 | Running | 6.2GB | 12 | RHEL 9 | plow-rpm — Snipe-IT asset mgmt, nginx, Portainer agent |
| Server 2016 | 192.168.1.217 | Running | 3.2GB | 12 | Windows Server 2016 | DIGIDIOTSERVER — Active Directory DC, DIGIDIOT.local |
| Ubuntu Server 2024.4 | 192.168.1.35 | Running | 1.4GB | 12 | Ubuntu 24.04 | 2404HV-deb — SSH + node-exporter |

---

## Raspberry Pi Fleet

_Pi rack fully documented 2026-06-30. 6-slot 3D printed red/black tower, desk location. Z-680 control pod on top._

### Racked (3D Printed Pi Rack)

| Slot | IP | Hostname | Hardware | OS | Services |
|------|----|----------|----------|----|---------|
| S1 | 192.168.1.125 | ha-net | RPi 4 | Home Assistant OS / DietPi (alt SD) | HA, Jellyfin :8096, Vaultwarden, Zabbix agent :10050 |
| S2 | 192.168.1.121 | blank-dietpi-deb | RPi 2B | DietPi | SSH — role TBD |
| S3 | 192.168.1.126 | backup-dietpi-deb | RPi 2B | DietPi | Gitea mirror :3000, Vaultwarden backup :8888, xrdp :3389 |
| S4 | 192.168.1.124 | retropi | RPi Model B | RetroPie | SSH, Samba — EOL, kept for patching only ⚠️ |
| S5 | 192.168.1.123 | batocera-deb | RPi 5 | Batocera | Retro gaming — 52Pi case |
| S6 | 192.168.1.120 | pihole-pi-deb | RPi Model B | Raspbian | Pi-hole DNS :53, web :80/:443 — SD card ⚠️ |

### Not Racked

| IP | Hostname | Hardware | OS | Services |
|----|----------|----------|----|---------|
| 192.168.1.122 | octopi-pi4-deb | RPi 4 | OctoPrint OS | OctoPrint :80/:443, node-exporter :9100 — attached to Ender 3 V2 |
| 192.168.1.127 | argos-pi4-deb | RPi 4 | RPi OS Bookworm | Offline — IoT field station (touchscreen, LTE, LoRa, camera) |
| 192.168.1.128 | argos-pi4-wifi-deb | RPi 4 | — | Offline — TBD |

---

## TrueNAS (freenas-bsd — 192.168.1.5)
_⚠️ Active NIC = USB (Realtek) — fragile, PCIe swap pending_

| Service | Port | Notes |
|---------|------|-------|
| SSH | :22 | OpenSSH 8.8 HPN-SSH |
| TrueNAS Web UI | :80/:443 | nginx |
| SMB/Samba | :139/:445 | Windows file sharing, smbd |
| NFS | :2049 | + rpcbind :111, mountd, statd, lockd |
| rsync | :873 | protocol v32 |
| WSDD | :5357 | Windows Service Discovery |
| collectd | internal | metrics collection |
| avahi | internal | mDNS/Bonjour |
| NTP | internal | ntpd |

_No iocage jails running._

---

## Consumer / IoT Devices

| IP | MAC Vendor | Device | Services |
|----|------------|--------|---------|
| 192.168.1.140 | LG Electronics | tv1-media — LG WebOS TV | UPnP/DLNA :1057/:1077/:1102, AirTunes/AirPlay :7000, WebOS HTTP :3000/:3001 |
| 192.168.1.145 | Amazon | Echo/Fire device | All ports filtered |
| 192.168.1.167 | Unknown | **Likely second LG TV** — ports 3000, 3001, 7000, 36866 match .140 (LG WebOS) exactly. Also ports 1114, 1128, 1132, 1226, 1385, 1792, 18181 | Identify — confirm LG device ⚠️ |
| 192.168.1.218 | Locally administered MAC | Unknown — high ephemeral ports only (32793, 51692, 64660). Likely VPN tunnel interface | Riley to investigate ⚠️ |

---

## Open Questions / Action Items

- [ ] **Dual reverse proxy** — Caddy + Traefik both running on docker-deb. Riley + Casey to determine which is authoritative
- [ ] **DIGIDIOT.local AD domain** — document what's joined, whether still in use, whether DIGIDIOTSERVER needs to stay running
- [ ] **192.168.1.167** — likely second LG TV based on port pattern. Confirm
- [ ] **192.168.1.218** — locally administered MAC, ephemeral ports only. Riley to identify (VPN tunnel?)
- [ ] **ZeroTier on amontillado (:9993)** — undocumented VPN overlay. What network/peers?
- [ ] **Zabbix server on monitor-deb (:10051)** — 11 agents deployed across the lab. Is Grafana pulling from Zabbix? Document monitoring topology
- [ ] **monitor-deb :9221** — unknown service. Identify
- [ ] **Fortunato-11** — work VM, off. Document role
- [ ] **alma-rpm (192.168.1.52)** — Apache :80, role undocumented
- [ ] **rocky-rpm (192.168.1.20)** — SSH only, role undocumented
- [ ] **2404HV-deb (192.168.1.35)** — Ubuntu 24.04 Hyper-V, role undocumented
- [ ] **Netgate (192.168.1.6)** — not responding to scans. Offline?
- [ ] **Portainer agents on mediastack-deb and plow-rpm** — registered in Portainer on docker-deb?
- [ ] **FlareSolverr + Prowlarr** — mark as complete on todo.md (both running)
- [ ] **pihole-pi1-deb SD card** — 91% full ⚠️

---

## Port Quick Reference

| Port | Service | Host |
|------|---------|------|
| :80/:443 | TrueNAS UI | 192.168.1.5 |
| :3000 | Gitea mirror | 192.168.1.126 |
| :3000 | Grafana | 192.168.1.29 |
| :3001 | Uptime Kuma | 192.168.1.29 |
| :3003 | Homepage | 192.168.1.29 |
| :3214 | Manyfold | 192.168.1.34 |
| :8000 | MkDocs | 192.168.1.3 |
| :8007 | PBS UI | 192.168.1.4 |
| :8081 | cAdvisor | 192.168.1.34 |
| :8082 | qBittorrent | 192.168.1.36 |
| :8088 | Caddy (Vaultwarden) | 192.168.1.34 |
| :8090 | Tube Archivist | 192.168.1.34 |
| :8443/:8444 | Caddy HTTPS | 192.168.1.34 |
| :8888 | Vaultwarden backup | 192.168.1.126 |
| :9000/:9443 | Portainer | 192.168.1.34 |
| :9100 | node-exporter | multiple hosts |
| :9999 | webhook.py | 192.168.1.3 |
| :27000 | FlexLM | 192.168.1.103 |
