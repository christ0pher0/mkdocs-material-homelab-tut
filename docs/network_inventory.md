# DIGIDIOT Network Inventory
_Last updated: 2026-08-24 — Generated from arp-scan + nmap -sV + masscan -p1-65535 + docker ps + qm/pct list + Hyper-V Manager_
_2026-08-24 amendments below are from live SSH/docker checks during a Homepage config session, not a fresh full scan — see inline notes._
_2026-08-25: Open Questions list merged with a follow-up action-item pass — added Immich and Firefly III (both real, undocumented), and layered "first step" commands onto 9 existing items (digidiot.com, urnst-deb, duplicate Pi entries, `collect_running_services.yml`, homepage-ts, pve-exporter, Docker log rotation, backup-dietpi-deb SD card, plaintext credentials) rather than duplicating them as new entries._

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
| 192.168.1.5 | freenas-bsd | Onboard alc0 (AR8161) — working as of 2026-07-03 | TrueNAS CORE — TRYAGAIN pool |
| 192.168.1.7 | maturin | Dell OptiPlex 7050 SFF, i7-6700, 32GB DDR4 | Proxmox node 2 |
| 192.168.1.9 | aslan | Gigabyte AB350-Gaming 3-CF, Ryzen 5 1600X, 32GB DDR4 | Proxmox node 3, GTX 1080 Ti (vfio) |
| 192.168.1.10 | beryl-ap | GL-MT3000 Beryl AX (GL Technologies) | WiFi AP, OpenWrt, AP mode |
| 192.168.1.11 | blaine | Gigabyte mobo, i5-2500K, 30GB RAM | Proxmox node 4 |
| 192.168.1.21 | immich-deb | Hardware/host type unconfirmed (found via 2026-08-24 docker_inv.yml run, not documented before that) | Immich — self-hosted photo/video management |
| 192.168.1.100 | amontillado | MSI, Windows 11 | Primary workstation + Hyper-V host |
| 192.168.1.129 | unnamed — no hostname resolves, no DHCP reservation confirmed, **IP may shift** | Dell OptiPlex 3040 | Batocera retro gaming mini-PC — 2nd Batocera system, separate from batocera-pi5-deb in the Pi rack. Dropbear SSH (:22) confirmed via nmap 2026-08-24; :80/:443 filtered, no web UI reachable. Found by process of elimination (unnamed host in a live nmap sweep) — worth a DHCP reservation once a hostname is picked, so it stops needing rediscovery. |

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

## immich-deb (192.168.1.21) — Docker Containers
_Found via 2026-08-24 docker_inv.yml run — not in any doc before that. Host type (bare metal/VM) unconfirmed._

| Container | Image | Port | Purpose |
|-----------|-------|------|---------|
| immich_server | ghcr.io/immich-app/immich-server:release | :2283 | Immich web/API |
| immich_postgres | ghcr.io/immich-app/postgres:14-vectorchord0.4.3-pgvectors0.2.0 | internal | Immich backend |
| immich_machine_learning | ghcr.io/immich-app/immich-machine-learning:release-cuda | internal | Immich ML (face/object detection) — CUDA build, implies GPU passthrough |
| immich_redis | valkey/valkey:9 | internal | Immich backend |

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
| firefly_iii_core | fireflyiii/core:latest | :8091 | Personal finance / budgeting — confirmed by Chris 2026-08-24 |
| firefly_iii_cron | alpine | internal | Firefly III scheduled tasks |
| firefly_iii_db | mariadb:lts | internal | Firefly III backend |
| scrutiny | (unlabeled image) | :8082 | S.M.A.R.T. disk health monitoring — found 2026-08-24 |
| scrutiny-influxdb | (unlabeled image) | :8087 | Scrutiny backend |
| convertx | c4illin/convertx | :3005 | File conversion tool — found 2026-08-24 |
| open-webui | (unlabeled image) | :3000 | LLM chat UI — likely frontend for Ollama on babar (192.168.1.20:11434) — found 2026-08-24 |

**2026-08-24:** this host was running 7 more containers (Firefly III x3, Scrutiny x2, ConvertX, open-webui) than any doc had recorded, all "Up 30 hours" at discovery — worth periodically diffing live `docker ps` against this table instead of assuming it's current.

---

## Hyper-V (amontillado — 192.168.1.100)
_Naming theme: Poe — "The Cask of Amontillado" characters_
_AD Domain: DIGIDIOT.local (controller: DIGIDIOTSERVER)_

| VM Name | IP | State | RAM | vCPUs | OS | Role |
|---------|----|-------|-----|-------|----|------|
| Fortunato-11 | — | Off | — | 2 | Windows 11 | Work VM — offline |
| Luchesi-240 | 192.168.1.103 | Running | 2.8GB | 12 | Windows 10 | LabVIEW + FlexLM license manager |
| RheL9-172 | 192.168.1.53 | Running | 6.2GB | 12 | RHEL 9 | plow-rpm — Snipe-IT asset mgmt only as of 2026-08-24 (`docker ps -a` showed just `snipe-it-app-1` + `snipe-it-db-1`). The `nginx1`/`site2-nginx-1` containers and Portainer agent from the June scan are gone — removed at some point, not replaced. |
| Server 2016 | 192.168.1.217 | Running | 3.2GB | 12 | Windows Server 2016 | DIGIDIOTSERVER — Active Directory DC, DIGIDIOT.local |
| Ubuntu Server 2024.4 | 192.168.1.35 | Running | 1.4GB | 12 | Ubuntu 24.04 | 2404HV-deb — SSH + node-exporter |

---

## Raspberry Pi Fleet

_Pi rack fully documented 2026-06-30. 6-slot 3D printed red/black tower, desk location. Z-680 control pod on top._

### Racked (3D Printed Pi Rack)

| Slot | IP | Hostname | Hardware | OS | Services |
|------|----|----------|----------|----|---------|
| S1 | 192.168.1.125 | tools-deb (OS-reported hostname; "ha-net" is only a resolvable SSH alias/DNS name — same mismatch pattern as freenas-bsd/truenas-bsd) | RPi 4 | Home Assistant OS / DietPi (alt SD) | HA, Jellyfin :8096, Zabbix agent :10050. **Vaultwarden confirmed NOT running here** (checked 2026-08-24: no `vaultwarden` systemd unit, no matching docker container) — remove any assumption of a 3rd Vaultwarden instance. HA/Jellyfin still-running status not re-verified this pass. |
| S2 | 192.168.1.121 | blank-dietpi-deb | RPi 2B | DietPi | SSH — role TBD |
| S3 | 192.168.1.126 | backup-dietpi-deb | RPi 2B | DietPi | Gitea mirror :3000, Vaultwarden backup :8888, xrdp :3389 |
| S4 | 192.168.1.124 | retropi | RPi Model B | RetroPie | SSH, Samba — EOL, kept for patching only ⚠️ |
| S5 | 192.168.1.123 | batocera-deb (Zabbix has it registered as `batocera-pi5-deb` — naming mismatch, same pattern as ha-net/tools-deb) | RPi 5 | Batocera | Retro gaming — 52Pi case. **Confirmed 2026-08-24: usually powered off** — Zabbix's recurring "ICMP ping unavailable" High-severity alert for this host is expected, not a fault. See also the separate Batocera mini-PC (Dell OptiPlex 3040, 192.168.1.129) in Physical Infrastructure above. |
| S6 | 192.168.1.120 | pihole-pi-deb | RPi Model B | Raspbian | Pi-hole DNS :53, web :80/:443 — SD card ⚠️ |

### Not Racked

| IP | Hostname | Hardware | OS | Services |
|----|----------|----------|----|---------|
| 192.168.1.122 | octopi-pi4-deb | RPi 4 | OctoPrint OS | OctoPrint :80/:443, node-exporter :9100 — attached to Ender 3 V2 |
| 192.168.1.127 | argos-pi4-deb | RPi 4 | RPi OS Bookworm | Offline — IoT field station (touchscreen, LTE, LoRa, camera) |
| 192.168.1.128 | argos-pi4-wifi-deb | RPi 4 | — | Offline — TBD |

---

## TrueNAS (freenas-bsd — 192.168.1.5)
_Active NIC = onboard alc0 (AR8161), static 192.168.1.5/24 — as of 2026-07-03. USB NIC retired. Watching for stability (alc driver history is rougher than Intel). X540-T2 PCIe card installed same session, suspected DOA (no link either port), pending bench test elsewhere._

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

- [ ] **Immich** — real, undocumented. First step: `grep -A 15 "## immich-deb" /home/cos/material/mkdocs_dev_material/docs/docker_inv.md` on git-ansible — the fresh scan already captured its IP, containers, and ports; that's enough to write it into this doc and Homepage without more digging.
- [ ] **Firefly III** — real, but its host is unknown; didn't show up under an obvious name in the 2026-08-24 scan. First step: `grep -ri firefly /home/cos/material/mkdocs_dev_material/docs/docker_inv.md /home/cos/material/mkdocs_dev_material/docs/network_inventory.md` on git-ansible — if empty, it's either under a container name that doesn't say "firefly," or on a host `docker_inv.yml` couldn't reach; may just need someone to say which box it's on.
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
- [x] **docker_inv.md staleness** — fixed 2026-08-24: root cause was a missing `--vault-password-file` flag on the cron line (added 2026-08-24, alongside `--vault-password-file` on the same job in root's crontab), not a removed automation. Playbook now runs clean.
- [ ] **homepage-ts (monitor-deb :3003)** — separate config from the main Homepage (:3002). Still undecided whether it should mirror the 5 services just added to the main dashboard (Manyfold, Pi-hole (Book), Prometheus, Overseerr, Tube Archivist) or stay a deliberately trimmed subset. First step: `cat /home/cos/monitoring/homepage-ts/config/services.yaml` on monitor-deb to see its current scope.
- [ ] **`collect_running_services.yml`** (2:35am cron, feeds `software_inventory.md`) — same class of missing-vault-flag bug `docker_inv.yml` had is plausible, hasn't been checked. First step: `tail -50 /var/log/software_inventory.log` on git-ansible.
- [ ] **digidiot.com** — domain registered 2026-08-24. This is a decision point before it's a technical task: public-facing access to specific services (Firefly III, Immich, etc. via reverse proxy + real Let's Encrypt certs instead of Tailscale certs)? Just claiming the name/email? Replacing the internal `DIGIDIOT.local` AD naming? First step is stating the intent — the DNS/reverse-proxy work downstream depends entirely on which one.
- [ ] **urnst-deb (192.168.1.27)** — appears in `inventory_auto` but unreachable ("No route to host") and undocumented anywhere else. Real decommissioned host, or stale inventory entry with nothing behind it? First step: check the router's DHCP lease list at router-net (192.168.1.1) LuCI UI for that IP/MAC — tells us whether it's ever actually been on the network.
- [ ] **Possible duplicate Pi inventory entries** — `pi1-deb`/`pihole-pi1-deb`, `pi2-deb`/`blank-dietpi-deb`, `pi4-deb`/`backup-dietpi-deb` all appeared as separate entries in the same 2026-08-24 `docker_inv.yml` run — looks like the same physical Pis listed twice under different names in `inventory_auto`, inflating every ansible run. First step: `grep -E "192\.168\.1\.(120|121|124|126)" ~/ansible_dev/inventory_auto` on git-ansible to confirm whether the same IPs are genuinely listed twice.
- [ ] **pve-exporter (monitor-deb)** — logged 4.4GB and was the direct cause of the disk hitting 100% full on 2026-08-24. Log was truncated as a workaround; root cause not yet identified. First step: `docker logs pve-exporter --tail 50` on monitor-deb — almost certainly the same Shardik-unreachable errors Homepage was also logging.
- [ ] **Docker log rotation on monitor-deb** — no `max-size`/`max-file` configured, which is what let pve-exporter's log grow unbounded; nothing prevents a recurrence. First step: `cat /etc/docker/daemon.json 2>/dev/null` on monitor-deb before deciding what to add (needs a daemon restart to take effect — plan for a maintenance window, not mid-incident).
- [ ] **backup-dietpi-deb SD card health** — 2026-08-24 Vaultwarden outage traced to root-owned db files after a hard hang; resolved via chown, but whether the underlying hang was SD card wear is unconfirmed. First step: `sudo smartctl -a /dev/mmcblk0 2>&1 | head -20` on that Pi (may not support SMART on SD, in which case just watch for recurrence).
- [ ] **Plaintext credentials in Homepage's services.yaml** — Proxmox root token, Grafana password, several API keys in cleartext. First step: whenever convenient, rotate the Proxmox `home_page` token first since it's full API access, not just a dashboard widget key.
- [ ] **Batocera mini-PC (192.168.1.129) has no hostname or DHCP reservation** — currently identified only by MAC/IP. Worth reserving its IP once a hostname is picked, so it doesn't need rediscovering if the lease changes
- [ ] **Zabbix's High-severity alert for batocera-pi5-deb** — confirmed benign (host is normally powered off), but the alert itself is still configured as High severity for what's expected/routine behavior. Worth adjusting the trigger severity or adding a maintenance window so it stops registering as a real problem

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
| :8082 | Scrutiny | 192.168.1.34 (same port # as qBittorrent, different host — no actual conflict) |
| :8087 | Scrutiny InfluxDB | 192.168.1.34 |
| :8088 | Caddy (Vaultwarden) | 192.168.1.34 |
| :8090 | Tube Archivist | 192.168.1.34 |
| :8091 | Firefly III | 192.168.1.34 |
| :8443/:8444 | Caddy HTTPS | 192.168.1.34 |
| :8888 | Vaultwarden backup | 192.168.1.126 |
| :2283 | Immich | 192.168.1.21 |
| :3000 | open-webui | 192.168.1.34 (same port # as Grafana on .29, different host) |
| :3005 | ConvertX | 192.168.1.34 |
| :9000/:9443 | Portainer | 192.168.1.34 |
| :9100 | node-exporter | multiple hosts |
| :9999 | webhook.py | 192.168.1.3 |
| :27000 | FlexLM | 192.168.1.103 |
