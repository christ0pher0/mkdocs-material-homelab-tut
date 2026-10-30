# Network IP Schema

_Last updated: 2026-10-30_

## IP Range Assignments

| Range | Purpose |
|-------|---------|
| 1-19 | Infrastructure (router, proxmox, NAS, network gear) |
| 20-49 | Debian/Ubuntu servers, VMs, containers |
| 50-59 | RPM servers (Rocky, Alma, RHEL) |
| 60-69 | Other Linux, non-deb/rpm (Arch, CachyOS, etc.) |
| 70-79 | Apple (macOS, iPadOS) |
| 100-119 | Windows workstations |
| 120-139 | Raspberry Pis |
| 140-159 | TVs, media devices, Plex jails |
| 160-179 | Peripherals, printers, IoT |
| 200-249 | Mobile, Android devices |
| 250+ | Special, reserved, virtual |

## Current Assignments

### Infrastructure (1-19)
| IP | Hostname | Description |
|----|----------|-------------|
| 192.168.1.1 | router-net | GL-iNet Flint 2 |
| 192.168.1.2 | proxmox-deb | Proxmox VE host |
| 192.168.1.3 | git-ansible-deb | Ansible control node / MkDocs |
| 192.168.1.5 | freenas-bsd | FreeNAS/TrueNAS |
| 192.168.1.6 | netgate-net | Netgate/pfSense |

### Debian/Ubuntu Servers (20-49)
| IP | Hostname | Description |
|----|----------|-------------|
| 192.168.1.20 | snipeit-deb | Snipe-IT asset management |
| 192.168.1.21 | grafana-docker-deb | Grafana, Prometheus, Portainer |
| 192.168.1.22 | swarm01-deb | Docker Swarm manager |
| 192.168.1.23 | swarm02-deb | Docker Swarm worker |
| 192.168.1.24 | swarm03-deb | Docker Swarm worker |
| 192.168.1.25 | ubuntu-ansible-deb | Ubuntu Ansible host |
| 192.168.1.26 | kasm-2404-deb | Kasm Workspaces |
| 192.168.1.32 | apache-deb | Apache web server |
| 192.168.1.33 | server2204-hv-deb | Hyper-V Ubuntu 22.04 |
| 192.168.1.34 | docker-deb | Docker host |
| 192.168.1.35 | 2404HV-deb | Hyper-V Ubuntu 24.04 |

### RPM Servers (50-59)
| IP | Hostname | Description |
|----|----------|-------------|
| 192.168.1.51 | rocky-rpm | Rocky Linux |
| 192.168.1.52 | alma-rpm | AlmaLinux |
| 192.168.1.53 | plow-rpm | RHEL 9 Hyper-V VM (Snipe-IT) |

### Other Linux, non-deb/rpm (60-69)
| IP | Hostname | Description |
|----|----------|-------------|
| 192.168.1.60 | celene-arch | MacBook Pro 13" 2016, CachyOS (Wi-Fi reservation; Tailscale 100.85.67.88) |

### Apple (70-79)
| IP | Hostname | Description |
|----|----------|-------------|
| 192.168.1.70 | ket-mac | macOS (Golden Gate-capable), Wi-Fi reservation; Ansible user beygraf; formerly tahoe-mac |
| 192.168.1.71 | ipad-ios | iPad (Wi-Fi reservation; not managed by Ansible) |

### Windows Workstations (100-119)
| IP | Hostname | Description |
|----|----------|-------------|
| 192.168.1.100 | amontillado-win | Main Windows workstation |
| 192.168.1.101 | eld-win | Windows workstation |
| 192.168.1.102 | replacements-win | Windows workstation |
| 192.168.1.103 | todash-win | Windows workstation |
| 192.168.1.104 | work-win | Work laptop (COE-3T8M403) |
| 192.168.1.105 | fortunato-win | Hyper-V Windows 11 VM |

### Raspberry Pis (120-139)
| IP | Hostname | Description |
|----|----------|-------------|
| 192.168.1.120 | pi1-deb | Raspberry Pi 1 (moving from .75) |
| 192.168.1.121 | pi2-deb | Raspberry Pi 2 (moving from .124) |

### TVs / Media / Plex (140-159)
| IP | Hostname | Description |
|----|----------|-------------|
| 192.168.1.140 | tv1-net | BTV |
| 192.168.1.141 | tv2-net | TV2 |
| 192.168.1.142 | lg-tv-net | LG WebOS TV (moving from .105) |
| 192.168.1.143 | weltgeist-bsd | Plex jail (FreeBSD) |
| 192.168.1.144 | alea_iacta_est-bsd | Plex jail (FreeBSD) |
| 192.168.1.145 | firetv-droid | Amazon Fire TV (moving from .214) |

### Peripherals / IoT (160-179)
| IP | Hostname | Description |
|----|----------|-------------|
| 192.168.1.162 | dell-printer-net | Dell 2155cdn Color MFP |

### Mobile / Android (200-249)
| IP | Hostname | Description |
|----|----------|-------------|
| 192.168.1.200 | alexa-droid | Amazon Echo (moving from .172) |
| 192.168.1.201 | pixel8-droid | Google Pixel 8 (moving from .202) |
| 192.168.1.202 | fire-tablet-droid | Amazon Fire Tablet (moving from .242) |
| 192.168.1.203 | roomba-droid | iRobot Roomba (moving from .241) |

### Special / Reserved (250+)
| IP | Hostname | Description |
|----|----------|-------------|
| 192.168.1.250 | swarm-shared-deb | Docker Swarm shared/VIP address |

## Pending IP Changes

| Host | Current IP | New IP | Status |
|------|-----------|--------|--------|
| pi1-deb | 192.168.1.75 | 192.168.1.120 | Pending |
| pi2-deb | 192.168.1.124 | 192.168.1.121 | Pending |
| lg-tv-net | 192.168.1.105 | 192.168.1.142 | Pending |
| fortunato-win | 192.168.1.106 | 192.168.1.105 | Pending |
| firetv-droid | 192.168.1.214 | 192.168.1.145 | Pending |
| alexa-droid | 192.168.1.172 | 192.168.1.200 | Pending |
| pixel8-droid | 192.168.1.202 | 192.168.1.201 | Pending |
| fire-tablet-droid | 192.168.1.242 | 192.168.1.202 | Pending |
| roomba-droid | 192.168.1.241 | 192.168.1.203 | Pending |
