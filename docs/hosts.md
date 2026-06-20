# Hosts
_Last updated: 2026-06-20_
_Live hosts from network scan + known offline hosts from router DHCP/hosts file_
_Router: GL-MT6000 (Flint 2) running OpenWrt — 192.168.1.1_

---

## Live Hosts (Last Scan: 2026-06-10, updated 2026-06-20)
| # | Hostname | IP Address | MAC Address | OS | Status | Notes |
|---|----------|------------|------------|----|--------|-------|
| 1 | router-net | 192.168.1.1 | 94:83:C4:AA:EE:FF | OpenWrt (GL-MT6000 Flint 2) | Online | Main router |
| 2 | shardik | 192.168.1.2 | 70:85:C2:72:C0:AB | Proxmox VE / Debian 12 | Online | ⚠️ PSU suspected — PVE node 1. CPU+RAM upgraded 2026-06. |
| 3 | git-ansible | 192.168.1.3 | — | Linux (Debian) | Online | Docs, Gitea, Ansible, qdevice — physical host |
| 4 | pbs-deb | 192.168.1.4 | BC:24:11:55:0B:AC | Debian/Ubuntu Linux | Online | Proxmox Backup Server VM (aslan) — migrated from shardik 2026-06-16 |
| 5 | freenas-bsd | 192.168.1.5 | 00:E0:4C:68:1C:1E | TrueNAS CORE 13.0-U6.8 | Online | NAS — TRYAGAIN pool HEALTHY. ⚠️ USB NIC, boot-pool DEGRADED |
| 6 | netgate-net | 192.168.1.6 | F0:AD:4E:1B:E7:62 | Network Device | Online | Netgate (pfSense/OPNsense) — topology vs Flint2 TBD |
| 7 | maturin | 192.168.1.7 | D8:9E:F3:0C:62:CC | Proxmox VE / Debian 12 | Online | PVE node 2 — Dell OptiPlex 7050 SFF |
| 8 | aslan | 192.168.1.9 | — | Proxmox VE 9.2.3 | Online | PVE node 3 — Gigabyte AB350, Ryzen 5 1600X, 32GB DDR4, GTX 1080 Ti (vfio). Was idee-deb — repurposed 2026-06-16 |
| 9 | urnst-deb | 192.168.1.27 | — | Debian 13 (Trixie) | Online | AM4 test bench / Proxmox node candidate |
| 10 | rocky-rpm | 192.168.1.20 | BC:24:11:0B:36:71 | RHEL/Rocky Linux | Online | VM on aslan (migrated from shardik 2026-06-16) |
| 11 | kasm-2404-deb | 192.168.1.26 | BC:24:11:D7:B3:48 | Debian/Ubuntu Linux | Online | Kasm Workspaces 1.17.0 VM (aslan) — disk on SDA_store, move to NVMe pending |
| 12 | monitor-deb | 192.168.1.29 | BC:24:11:A7:F3:4F | Debian/Ubuntu Linux | Online | Monitoring stack VM (maturin) |
| 13 | pihole-book-deb | 192.168.1.33 | BC:24:11:E8:54:9D | Debian/Ubuntu Linux | Online | PiHole LXC (aslan) — migrated from shardik 2026-06-16 |
| 14 | docker-deb | 192.168.1.34 | BC:24:11:E3:70:53 | Debian/Ubuntu Linux | Online | ⚠️ Reboot pending — Vaultwarden, Traefik, Portainer VM (maturin) |
| 15 | 2404HV-deb | 192.168.1.35 | 00:15:5D:00:B3:1E | Debian/Ubuntu Linux | Online | Hyper-V VM (amontillado) |
| 16 | mediastack-deb | 192.168.1.36 | BC:24:11:63:F7:0D | Debian/Ubuntu Linux | Online | Full media stack VM (maturin) |
| 17 | restic-deb | 192.168.1.40 | 90:2B:34:5E:B0:A2 | Ubuntu 26.04 LTS | Online | ⚠️ Planned repurpose → blaine-pve (Proxmox). Scripts backed up Gitea 4ad5a94. |
| 18 | alma-rpm | 192.168.1.52 | BC:24:11:E5:47:A1 | AlmaLinux | Online | VM on aslan (migrated from shardik 2026-06-16) |
| 19 | plow-rpm | 192.168.1.53 | 00:15:5D:00:B3:03 | RHEL/Rocky/Alma Linux | Online | Hyper-V VM (amontillado) — Snipe-IT, nginx |
| 20 | amontillado-win | 192.168.1.100 | 04:7C:16:C1:44:8E | Windows 11 + Hyper-V | Online | ⭐ Best system — primary workstation + Hyper-V host |
| 21 | todash-win | 192.168.1.103 | 00:15:5D:00:B3:08 | Windows | Online | Hyper-V VM (amontillado) |
| 22 | fortunato-win | 192.168.1.106 | 00:15:5D:00:B3:1A | Windows | Online | Hyper-V VM (amontillado) — Poe |
| 23 | octopi-deb | 192.168.1.122 | DC:A6:32:5E:04:08 | Debian/Ubuntu Linux | Online | RPi 4 — OctoPrint (Ender 3 V2) |
| 24 | ha-net | 192.168.1.125 | E4:5F:01:65:56:EE | Home Assistant OS 17.2 | Online | RPi 4 — Home Assistant |
| 25 | tv1-media | 192.168.1.140 | A8:23:FE:13:A9:D1 | Media Device | Online | — |
| 26 | tv2-media | 192.168.1.141 | 22:57:5A:A7:04:87 | Media Device | Online | — |
| 27 | pixel8-droid | 192.168.1.201 | EE:FC:9C:95:22:1B | Android | Online | Pixel 8 |
| 28 | alexa-droid | 192.168.1.202 | B0:FC:0D:51:8F:78 | Android | Online | Fire tablet |
| 29 | unknown-WS2016 | 192.168.1.217 | 00:15:5D:00:B3:20 | Windows Server 2016 | Online | Hyper-V VM — temporary NIC teaming test (amontillado) |

---

## Known Offline Hosts
_Not currently active — known from router hosts file and prior inventory_

| Hostname | IP | OS | Notes |
|----------|----|----|-------|
| swarm01-deb | 192.168.1.22 | Debian | Swarm manager VM (shardik) — stopped, migration to aslan pending |
| swarm02-deb | 192.168.1.23 | Debian | Swarm worker VM (aslan) — stopped |
| swarm03-deb | 192.168.1.24 | Debian | Swarm worker VM (aslan) — stopped |
| eld-win | 192.168.1.101 | Windows | Offline — needs inventory |
| work-win | 192.168.1.104 | Windows | Offline — needs inventory |
| temerant-win | 192.168.1.105 | Windows 10 | Donor system for TrueNAS rebuild |
| tahoe-mac | 192.168.1.200 | macOS | Offline — not yet inventoried |
| pi1-deb | 192.168.1.120 | Raspbian | RPi Model B — ⚠️ SD 91% full |
| pi2-deb | 192.168.1.121 | — | RPi Model B Rev 2 (512MB) — role TBD |
| pi3-deb | 192.168.1.124 | RetroPie | RPi Model B — legacy NES/SNES/GB |
| pi4-deb | 192.168.1.126 | DietPi | RPi 2 — Zigbee + MQTT |
| batocera-deb | 192.168.1.123 | Batocera | RPi 5 — retro gaming |
| argos-deb | 192.168.1.127 | Raspberry Pi OS | RPi 4 — IoT field station |
| pve3 | offsite | Proxmox VE | ThinkStation — PVE node 4, needs inventory + Tailscale |
| lee-deb | TBD | Ubuntu Server (pending) | Dell Inspiron 3647 — Immich, memorial machine |

---

## Network Devices & IoT
| Hostname | IP | Notes |
|----------|-----|-------|
| router-net | 192.168.1.1 | GL-MT6000 Flint 2, OpenWrt |
| beryl-ap | 192.168.1.10 | GL-MT3000 Beryl AX — AP mode, extends Greyhawk WiFi (configured 2026-06-15) |
| netgate-net | 192.168.1.6 | Netgate — topology vs Flint2 to be clarified |
| ha-net | 192.168.1.125 | Home Assistant (RPi 4) |
| lg-media | 192.168.1.142 | LG TV |
| firetv-media | 192.168.1.145 | Amazon Fire TV |
| dell-printer-net | 192.168.1.162 | Dell printer |
| roomba-droid | 192.168.1.203 | Roomba |
| swarm-shared-vip | 192.168.1.250 | Docker Swarm virtual IP |

---

## Local DNS Overrides (GL-MT6000)
| Hostname | Resolves To | Notes |
|----------|-------------|-------|
| vaultwarden.lan | 192.168.1.34 | docker-deb — Caddy proxies to Vaultwarden |

---

## Decommissioned (Remove from all docs)
| Hostname | IP | Reason |
|----------|-----|--------|
| snipeit-deb | 192.168.1.20 | LXC destroyed 2026-05-10 — replaced by Snipe-IT on plow-rpm |
| grafana-docker-deb | 192.168.1.21 | Decommissioned |
| ubuntu-ansible-deb | 192.168.1.25 | Decommissioned |
| apache-deb | 192.168.1.32 | Decommissioned |
| weltgeist-media | 192.168.1.143 | TrueNAS jail — decommissioned, dataset pending deletion |
| alea_iacta_est-media | 192.168.1.144 | TrueNAS jail — decommissioned, dataset pending deletion |
| replacements-win | 192.168.1.102 | Decommissioned |
| idee-deb | 192.168.1.28 | Repurposed as aslan (Proxmox node 3) — 2026-06-16 |
