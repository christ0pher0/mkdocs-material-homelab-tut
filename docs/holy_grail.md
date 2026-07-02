# DIGIDIOT Homelab — The Holy Grail
_The ideal end state. Every decision moves us toward this._
_Last updated: 2026-07-02_

---

## Compute — Proxmox Cluster "Wheel"

| Node | Role | Current RAM | Max RAM | Target Storage | Status |
|---|---|---|---|---|---|
| shardik | Primary VM host — general workloads | 32GB (4×8GB DDR4-2400) | 128GB | NVMe + ZFS RAIDZ1 tank (15.7TB) | 🟡 Uptime watch to Aug 2 |
| maturin | Secondary VM host — lightweight services | 32GB (4×8GB DDR4-2133) | 64GB | Local SSD | 🟢 Stable |
| aslan | GPU node — AI, transcoding, GPU VMs | 64GB (4×16GB DDR4-2666) | 128GB | NVMe + HDD | 🟢 RAM upgraded 2026-07-02 |
| blaine | CRU/backup node — restic + Samba | 32GB (4×8GB DDR3-1333) | 32GB (maxed, DDR3) | SSD | 🟢 Role locked |
| pve3 | Offsite DR node — cold/warm failover | Unknown | TBD | TBD | 🔴 Not yet configured |

**Target cluster state:**
- shardik: general VM workloads, mediastack, heavy lifting
- maturin: lightweight infrastructure (monitor-deb, git-ansible)
- aslan: GPU passthrough — Ollama, Tdarr, hardware transcoding
- blaine: CRU workflow only — restic-deb + Samba LXC, nothing else
- pve3: offsite DR — Proxmox HA failover over Tailscale

---

## Storage

**TrueNAS (freenas-bsd — rebuild target)**
- Hardware: temerant (Ryzen 5 1600X, 32GB DDR4) — replaces aging Z77
- Boot: SSD (replace fragile USB boot)
- HBA: LSI 9211-8i or IBM M1015 IT mode
- Pool: TRYAGAIN RAIDZ1 (~90TB raw) — healthy, keep
- NIC: Intel X540-T2 PCIe (replace dead onboard + fragile USB NIC)
- Add: Dell JBOD + SAS 12G HBA for future expansion

**CRU Archive (blaine → restic-deb)**
- 3-2-1 policy: TrueNAS (live) → CRU drives (local archive) → offsite rotation
- Rotation schedule: established and documented
- All STL categories backed up to dedicated labeled drives
- Scripts: cru_stats, backup_drives_update, cru_plexfolder_stats all patched and reliable

**Target backup policy:**
- Tier 1: TrueNAS RAIDZ1 (live)
- Tier 2: CRU drives on blaine (local archive, rotated)
- Tier 3: Offsite drive rotation (TBD schedule)
- Tier 4: PBS snapshots of all VMs on shardik

---

## Networking

**Target topology:**
- Netgate SG-1100: primary router/firewall (pfSense)
- Dell managed switch (Cisco SG200-50 or N4032F): 802.1Q VLANs
- GL-MT6000 Flint 2: AP mode only
- GL-MT3000 Beryl AX: secondary AP

**VLAN scheme:**
- VLAN 10 Servers: 192.168.10.0/24 — Proxmox, TrueNAS, VMs, Docker, Pis
- VLAN 20 Trusted: 192.168.20.0/24 — amontillado, work devices
- VLAN 30 IoT: 192.168.30.0/24 — TVs, Echo, Fire TV, WiFi clients
- VLAN 99 Mgmt: 192.168.99.0/24 — switch UI, pfSense UI

**DNS:** Unbound local resolver — no relying on ISP DNS
**VPN:** Single solution (Tailscale preferred) — ZeroTier and WireGuard decommissioned
**Auth:** Authelia in front of all exposed services

---

## Services

**Media Stack (mediastack-deb → shardik)**
- Plex + hardware transcoding (GPU on aslan long-term)
- Tdarr — automated transcoding pipeline (GPU node)
- Tautulli — analytics
- Bazarr — subtitles
- Audiobookshelf, Komga, RomM all populated

**Infrastructure**
- Vaultwarden: primary on docker-deb, backup on backup-dietpi-deb
- Traefik: cluster-wide reverse proxy in Docker Swarm
- Uptime Kuma + Zabbix: full monitoring coverage, Telegram alerts
- Homepage: live dashboard, all services wired
- PBS: VM snapshots on shardik, offsite sync to pve3

**AI / Local LLM (aslan)**
- Ollama with GTX 1080 Ti GPU passthrough
- Open WebUI
- Whisper (STT) + Piper (TTS)
- MkDocs docs as RAG knowledge base
- Sysadmin, homelab, and casual assistant personalities

**Home Automation (ha-net)**
- Phase 1: TrueNAS backup, Tailscale
- Phase 2: Zigbee, MQTT, ESPHome, Frigate (Advidia cameras)
- Phase 3: OctoPrint integration, Music Assistant
- Phase 4: argos-deb wall kiosk (touchscreen field station)

**3D Printing**
- OctoPrint on octopi-pi4-deb — Ender 3 V2
- Elegoo Mars 3 — resin
- Ender 3 V1 — spares/testing
- Flashforge Dreamer — dual extrusion
- Manyfold on blaine LXC — STL library browser

---

## Monitoring & Alerting

- Zabbix: agent on every host, server on monitor-deb
- Uptime Kuma: service uptime, TrueNAS at 30s poll
- Telegram bot: weekly patch results, SMART alerts, service down alerts
- Grafana: pulling from Zabbix for dashboards
- Alerts on: drive errors, disk >85%, service down, high temp, RAM pressure

---

## Rack

- APC 12U half rack: all servers racked cleanly
- Patch panel + PDU
- Dell managed switch in rack
- Pi rack on shelf
- maturin (OptiPlex SFF) on shelf
- TrueNAS rack-mount chassis (post rebuild)
- Full cable management

---

## Documentation (MkDocs)

- Cluster capacity page — node specs, RAM, VM placement
- Hardware target state (this page)
- Network topology diagram — live and accurate
- Runbooks for every recurring operation
- DC salvage tracker — live
- Backup policy — documented 3-2-1
- All hosts in hosts.md — accurate and current
- Vinyl collection page — live

---

## Team End State

Every specialist has clear ownership, runbooks for their domain, and no single points of failure in knowledge or execution. Chris reviews weekly. The ED keeps the backlog clean and priorities clear.

---

_This is the north star. Not everything happens at once. Every session moves the needle._
