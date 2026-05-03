# Tailscale Network
_Last updated: 2026-04-29_
_Tailnet: taild502ad.ts.net_
_MagicDNS enabled — hosts reachable by short name within tailnet_

---

## Tailscale Hosts

| Hostname | Tailscale IP | MagicDNS FQDN | OS | LAN IP |
|----------|-------------|----------------|-----|--------|
| git-ansible | 100.68.195.68 | git-ansible.taild502ad.ts.net | Linux | 192.168.1.3 |
| 2404hv-deb | 100.81.13.127 | 2404hv-deb.taild502ad.ts.net | Linux | 192.168.1.34 |
| alma-rpm | 100.125.65.58 | alma-rpm.taild502ad.ts.net | Linux | 192.168.1.81 |
| amontillado | 100.126.7.50 | amontillado.taild502ad.ts.net | Windows | 192.168.1.100 |
| apache-deb | 100.72.112.113 | apache-deb.taild502ad.ts.net | Linux | 192.168.1.32 |
| coe-thinkpad-p1-gen-4i | 100.81.219.113 | coe-thinkpad-p1-gen-4i.taild502ad.ts.net | Linux | — |
| docker-deb | 100.121.121.10 | docker-deb.taild502ad.ts.net | Linux | 192.168.1.34 |
| grafana-docker-deb | 100.86.38.88 | grafana-dock.taild502ad.ts.net | Linux | 192.168.1.35 |
| kasm-2404-deb | 100.80.14.29 | kasm-2404-deb.taild502ad.ts.net | Linux | 192.168.1.37 |
| maturin | 100.75.181.63 | maturin.taild502ad.ts.net | Linux | 192.168.1.7 |
| mediastack-deb | 100.127.236.79 | mediastack-deb.taild502ad.ts.net | Linux | 192.168.1.36 |
| octopi-deb | 100.75.54.17 | octopi-deb.taild502ad.ts.net | Linux | 192.168.1.122 |
| pihole-book-deb | 100.91.156.40 | pihole-book-deb.taild502ad.ts.net | Linux | 192.168.1.33 |
| pixel-8 | 100.110.116.11 | pixel-8.taild502ad.ts.net | Android | — |
| plow-rpm | 100.92.197.96 | plow-rpm.taild502ad.ts.net | Linux | 192.168.1.82 |
| rocky-rpm | 100.72.44.64 | rocky-rpm.taild502ad.ts.net | Linux | 192.168.1.80 |
| shardik | 100.107.69.29 | shardik.taild502ad.ts.net | Linux | 192.168.1.2 |
| snipe-it | 100.113.46.16 | snipe-it.taild502ad.ts.net | Linux | 192.168.1.20 |
| swarm01-deb | 100.104.74.2 | swarm01-deb.taild502ad.ts.net | Linux | 192.168.1.41 |
| swarm02-deb | 100.77.65.12 | swarm02-deb.taild502ad.ts.net | Linux | 192.168.1.42 |
| swarm03-deb | 100.106.23.81 | swarm03-deb.taild502ad.ts.net | Linux | 192.168.1.43 |
| ubuntu-ansible-deb | 100.114.198.58 | ubuntu-ansible-deb.taild502ad.ts.net | Linux | 192.168.1.38 |

---

## Notes
- MagicDNS enabled — use short hostnames within the tailnet (e.g. `ssh mediastack-deb`)
- FQDN format: `hostname.taild502ad.ts.net`
- Auth key expires: 2026-07-28 — rotate at `https://login.tailscale.com/admin/settings/keys`
- Pixel-8 offline — last seen 8 days ago
- LAN IPs marked `—` are mobile/offsite devices with no fixed LAN address
- Some LAN IPs are estimated — verify against DHCP reservations

---

## Services

All services hosted on mediastack-deb (192.168.1.36 / 100.127.236.79)

| Service | Description | LAN URL | Tailscale URL |
|---------|-------------|---------|---------------|
| Plex | Media Server | http://192.168.1.36:32400/web | http://mediastack-deb.taild502ad.ts.net:32400/web |
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
| RoMM | ROM Manager | http://192.168.1.36:8998 | http://mediastack-deb.taild502ad.ts.net:8998 |
| Homepage | Dashboard | http://192.168.1.36:9898 | http://mediastack-deb.taild502ad.ts.net:9898 |
| Vaultwarden | Password Manager | https://192.168.1.34 | http://docker-deb.taild502ad.ts.net |
| Kasm | Browser Isolation | http://192.168.1.37 | http://kasm-2404-deb.taild502ad.ts.net |
| Grafana | Metrics Dashboard | http://192.168.1.35:3000 | http://grafana-dock.taild502ad.ts.net:3000 |
| Snipe-IT | Asset Management | http://192.168.1.20 | http://snipe-it.taild502ad.ts.net |
| MkDocs | Homelab Docs | http://192.168.1.3:8000 | http://git-ansible.taild502ad.ts.net:8000 |
| Proxmox (shardik) | Hypervisor Node 1 | https://192.168.1.2:8006 | https://shardik.taild502ad.ts.net:8006 |
| Proxmox (maturin) | Hypervisor Node 2 | https://192.168.1.7:8006 | https://maturin.taild502ad.ts.net:8006 |
| OctoPrint | 3D Printer Control | http://192.168.1.122 | http://octopi-deb.taild502ad.ts.net |
