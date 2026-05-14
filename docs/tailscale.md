# Tailscale Network
_Last updated: 2026-05-13_
_Tailnet: taild502ad.ts.net_
_MagicDNS enabled — hosts reachable by short name within tailnet_

---

## Tailscale Hosts

| Hostname | Tailscale IP | MagicDNS FQDN | OS | LAN IP |
|----------|-------------|----------------|-----|--------|
| 2404hv-deb | 100.81.13.127 | 2404hv-deb.taild502ad.ts.net | Linux | 192.168.1.35 |
| alma-rpm | 100.125.65.58 | alma-rpm.taild502ad.ts.net | Linux | 192.168.1.52 |
| amontillado | 100.126.7.50 | amontillado.taild502ad.ts.net | Windows | 192.168.1.100 |
| coe-thinkpad-p1-gen-4i *(offline)* | 100.81.219.113 | coe-thinkpad-p1-gen-4i.taild502ad.ts.net | Linux | — |
| docker-deb | 100.121.121.10 | docker-deb.taild502ad.ts.net | Linux | 192.168.1.34 |
| git-ansible | 100.68.195.68 | git-ansible.taild502ad.ts.net | Linux | 192.168.1.3 |
| kasm-2404-deb | 100.80.14.29 | kasm-2404-deb.taild502ad.ts.net | Linux | 192.168.1.26 |
| maturin | 100.75.181.63 | maturin.taild502ad.ts.net | Linux | 192.168.1.7 |
| mediastack-deb | 100.103.127.40 | mediastack-deb.taild502ad.ts.net | Linux | 192.168.1.36 |
| monitor-deb | 100.88.140.58 | monitor-deb.taild502ad.ts.net | Linux | 192.168.1.29 |
| octopi-deb | 100.75.54.17 | octopi-deb.taild502ad.ts.net | Linux | 192.168.1.122 |
| pihole-book-deb | 100.91.156.40 | pihole-book-deb.taild502ad.ts.net | Linux | 192.168.1.33 |
| pixel-8 *(offline)* | 100.110.116.11 | pixel-8.taild502ad.ts.net | Android | — |
| plow-rpm | 100.92.197.96 | plow-rpm.taild502ad.ts.net | Linux | 192.168.1.53 |
| restic-deb | 100.74.233.29 | restic-deb.taild502ad.ts.net | Linux | 192.168.1.40 |
| rocky-rpm | 100.72.44.64 | rocky-rpm.taild502ad.ts.net | Linux | 192.168.1.51 |
| shardik | 100.107.69.29 | shardik.taild502ad.ts.net | Linux | 192.168.1.2 |
| swarm01-deb | 100.104.74.2 | swarm01-deb.taild502ad.ts.net | Linux | 192.168.1.22 |
| swarm02-deb | 100.77.65.12 | swarm02-deb.taild502ad.ts.net | Linux | 192.168.1.23 |
| swarm03-deb | 100.106.23.81 | swarm03-deb.taild502ad.ts.net | Linux | 192.168.1.24 |

---

## Notes

- MagicDNS enabled — use short hostnames within the tailnet (e.g. ssh mediastack-deb)
- FQDN format: hostname.taild502ad.ts.net
- Auth key expires: 2026-07-28 — rotate at https://login.tailscale.com/admin/settings/keys
- LAN IPs marked — are mobile/offsite devices with no fixed LAN address

---

## Services

### mediastack-deb (192.168.1.36 / mediastack-deb.taild502ad.ts.net)

| Service | Description | LAN URL | Tailscale URL |
|---------|-------------|---------|---------------|
| Plex | Media Server | http://192.168.1.36:32400/web/index.html#!/ | http://mediastack-deb.taild502ad.ts.net:32400/web/index.html#!/ |
| Sonarr | TV Show Manager | http://192.168.1.36:8989 | http://mediastack-deb.taild502ad.ts.net:8989 |
| Radarr | Movie Manager | http://192.168.1.36:7878 | http://mediastack-deb.taild502ad.ts.net:7878 |
| Lidarr | Music Manager | http://192.168.1.36:8686 | http://mediastack-deb.taild502ad.ts.net:8686 |
| Prowlarr | Indexer Manager | http://192.168.1.36:9696 | http://mediastack-deb.taild502ad.ts.net:9696 |
| Mylar | Comics Manager | http://192.168.1.36:8091 | http://mediastack-deb.taild502ad.ts.net:8091 |
| SABnzbd | Usenet Downloader | http://192.168.1.36:8090 | http://mediastack-deb.taild502ad.ts.net:8090 |
| qBittorrent | Torrent Downloader (VPN) | http://192.168.1.36:8082 | http://mediastack-deb.taild502ad.ts.net:8082 |
| Audiobookshelf | Audiobook Server | http://192.168.1.36:13378 | http://mediastack-deb.taild502ad.ts.net:13378 |
| Komga | Comics Reader | http://192.168.1.36:8085 | http://mediastack-deb.taild502ad.ts.net:8085 |
| Seerr | Movie & TV Requests | http://192.168.1.36:5055 | http://mediastack-deb.taild502ad.ts.net:5055 |
| RomM | ROM Manager | http://192.168.1.36:8998 | http://mediastack-deb.taild502ad.ts.net:8998 |

### monitor-deb (192.168.1.29 / monitor-deb.taild502ad.ts.net)

| Service | Description | LAN URL | Tailscale URL |
|---------|-------------|---------|---------------|
| Grafana | Metrics Dashboard | http://192.168.1.29:3000 | http://monitor-deb.taild502ad.ts.net:3000 |
| Prometheus | Metrics Collector | http://192.168.1.29:9090 | http://monitor-deb.taild502ad.ts.net:9090 |
| Zabbix | Network Monitor | http://192.168.1.29:8080 | http://monitor-deb.taild502ad.ts.net:8080 |
| Uptime Kuma | Uptime Monitor | http://192.168.1.29:3001 | http://monitor-deb.taild502ad.ts.net:3001 |
| Homepage | Dashboard | http://192.168.1.29:3002 | http://monitor-deb.taild502ad.ts.net:3002 |

### docker-deb (192.168.1.34 / docker-deb.taild502ad.ts.net)

| Service | Description | LAN URL | Tailscale URL |
|---------|-------------|---------|---------------|
| Portainer | Container Manager | https://192.168.1.34:9443 | https://docker-deb.taild502ad.ts.net:9443 |
| Vaultwarden | Password Manager | https://192.168.1.34:8443 | https://docker-deb.taild502ad.ts.net:8443 |
| Traefik | Reverse Proxy | http://192.168.1.34:8080 | http://docker-deb.taild502ad.ts.net:8080 |

### git-ansible-deb (192.168.1.3 / git-ansible.taild502ad.ts.net)

| Service | Description | LAN URL | Tailscale URL |
|---------|-------------|---------|---------------|
| Gitea | Git Server | http://192.168.1.3:3000 | http://git-ansible.taild502ad.ts.net:3000 |
| MkDocs | Homelab Docs | http://192.168.1.3:8000 | http://git-ansible.taild502ad.ts.net:8000 |

### plow-rpm (192.168.1.53 / plow-rpm.taild502ad.ts.net)

| Service | Description | LAN URL | Tailscale URL |
|---------|-------------|---------|---------------|
| Snipe-IT | Asset Management | http://192.168.1.53:8000 | http://plow-rpm.taild502ad.ts.net:8000 |
| Apache | Web Server | http://192.168.1.53 | http://plow-rpm.taild502ad.ts.net |

### Proxmox Nodes

| Service | Description | LAN URL | Tailscale URL |
|---------|-------------|---------|---------------|
| Proxmox (shardik) | Hypervisor Node 1 | https://192.168.1.2:8006 | https://shardik.taild502ad.ts.net:8006 |
| Proxmox (maturin) | Hypervisor Node 2 | https://192.168.1.7:8006 | https://maturin.taild502ad.ts.net:8006 |

### Other Services

| Service | Description | LAN URL | Tailscale URL |
|---------|-------------|---------|---------------|
| Kasm | Browser Isolation (kasm-2404-deb) | https://192.168.1.26 | https://kasm-2404-deb.taild502ad.ts.net |
| Pi-hole | DNS / Ad Blocking (pihole-book-deb) | http://192.168.1.33/admin | http://pihole-book-deb.taild502ad.ts.net/admin |
| OctoPrint | 3D Printer Control (octopi-deb) | http://192.168.1.122 | http://octopi-deb.taild502ad.ts.net |
