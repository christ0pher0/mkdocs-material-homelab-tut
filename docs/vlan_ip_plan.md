# DIGIDIOT VLAN & Static IP Plan
_Designed: 2026-06-28 — Pending implementation (Sunday Project 8)_
_Status: APPROVED by Chris — awaiting Dell switch model confirmation_

---

## Design Principles

- Last octets preserved from current 192.168.1.x scheme to minimize migration pain
- All statics locked by MAC reservation in pfSense DHCP
- pfSense SG-1100: WAN = ONT, LAN = Dell switch trunk
- Dell managed switch: 802.1Q tagged VLANs, one trunk port to SG-1100

---

## VLAN 10 — Servers · 192.168.10.0/24

Gateway: 192.168.10.1 (pfSense)
DHCP pool: 192.168.10.200–250 (dynamic VMs)

| IP | Hostname | Role |
|----|----------|------|
| 192.168.10.1 | pfSense | Gateway |
| 192.168.10.2 | shardik | Proxmox node 1 |
| 192.168.10.3 | git-ansible-deb | Ansible, MkDocs, Gitea |
| 192.168.10.4 | pbs | Proxmox Backup Server |
| 192.168.10.5 | freenas-bsd | TrueNAS CORE |
| 192.168.10.7 | maturin | Proxmox node 2 |
| 192.168.10.9 | aslan | Proxmox node 3 |
| 192.168.10.11 | blaine | Proxmox node 4 |
| 192.168.10.20 | rocky-rpm | Role TBD |
| 192.168.10.29 | monitor-deb | Grafana, Uptime Kuma, Zabbix server |
| 192.168.10.33 | pihole-book-deb | Pi-hole (LXC on aslan) |
| 192.168.10.34 | docker-deb | Vaultwarden, Tube Archivist, Manyfold, Traefik, Caddy |
| 192.168.10.36 | mediastack-deb | Plex, *arr suite, SABnzbd, Jellyfin, WireGuard |
| 192.168.10.40 | restic-deb | Restic backup agent, Samba (CRU drives) |
| 192.168.10.52 | alma-rpm | Apache, role TBD |
| 192.168.10.120 | pihole-pi1-deb | Pi-hole primary DNS |
| 192.168.10.121 | blank-dietpi1-deb | Role TBD |
| 192.168.10.122 | octopi-pi4-deb | OctoPrint |
| 192.168.10.124 | retropi-pi1-deb | RetroPie |
| 192.168.10.125 | ha-pi4 / tools-deb | Home Assistant / Jellyfin |
| 192.168.10.126 | backup-dietpi-deb | Gitea mirror, Vaultwarden backup |

**Firewall rules (VLAN 10):**
- Intra-VLAN: allow all
- → VLAN 20: allow (servers reach trusted)
- → VLAN 30: block by default
- → VLAN 99: block
- → WAN: allow
- Zabbix agents (.all) → monitor-deb (.29): allow :10050/:10051
- pihole (.120, .33) → all VLANs: allow :53 (DNS)

---

## VLAN 20 — Trusted · 192.168.20.0/24

Gateway: 192.168.20.1 (pfSense)
DHCP pool: 192.168.20.150–199 (laptops, temp devices)

| IP | Hostname | Role |
|----|----------|------|
| 192.168.20.1 | pfSense | Gateway |
| 192.168.20.100 | amontillado | Primary workstation (Windows 11) |
| 192.168.20.35 | 2404HV-deb | Ubuntu 24.04 Hyper-V VM |
| 192.168.20.53 | plow-rpm | Snipe-IT asset management (RHEL 9 Hyper-V VM) |
| 192.168.20.103 | Luchesi | LabVIEW + FlexLM (Windows 10 Hyper-V VM) |
| 192.168.20.217 | DIGIDIOTSERVER | Active Directory DC, DIGIDIOT.local (Server 2016 Hyper-V VM) |

**Notes:**
- Hyper-V VMs bridge through amontillado's NIC — amontillado switch port must be trunk OR second NIC added for server VLAN separation. ⚠️ Riley to resolve before cutover.
- Fortunato-11 (work VM, off) — add when online

**Firewall rules (VLAN 20):**
- → VLAN 10: allow (full server access)
- → VLAN 30: allow (control IoT devices from trusted)
- → VLAN 99: allow (admin access to switch/pfSense)
- → WAN: allow
- VLAN 30 blocked from reaching back into VLAN 20

---

## VLAN 30 — IoT · 192.168.30.0/24

Gateway: 192.168.30.1 (pfSense)
DHCP pool: 192.168.30.50–139 (WiFi IoT clients)

| IP | Hostname | Role |
|----|----------|------|
| 192.168.30.1 | pfSense | Gateway |
| 192.168.30.140 | tv1 | LG TV #1 |
| 192.168.30.145 | echo1 | Amazon Echo / Fire TV |
| 192.168.30.167 | tv2 | LG TV #2 (probable) |
| DHCP | LG TV #3 | Likely on guest WiFi currently — confirm |
| DHCP | WiFi clients | Phones, tablets, general WiFi |

**Firewall rules (VLAN 30):**
- → WAN: allow (internet access)
- → VLAN 10: block (no homelab access)
- → VLAN 20: block
- → VLAN 99: block
- Exception: → 192.168.10.36 :32400 allow (Plex from TVs/Fire TV)
- Flint 2 + Beryl WiFi clients default to this VLAN

---

## VLAN 99 — Management · 192.168.99.0/24

Gateway: 192.168.99.1 (pfSense)
No DHCP — static only

| IP | Device | Access |
|----|--------|--------|
| 192.168.99.1 | pfSense web UI | amontillado only |
| 192.168.99.2 | Dell switch web UI | amontillado only |

**Firewall rules (VLAN 99):**
- All VLANs blocked inbound except VLAN 20 (amontillado)
- No outbound to WAN

---

## Migration Checklist (Phase 3)

After cutover, every reference to 192.168.1.x must be updated:

- [ ] pfSense DHCP reservations — set by MAC before cutover
- [ ] Ansible inventory_auto — all IPs
- [ ] corosync.conf — cluster ring addresses (Proxmox nodes)
- [ ] /etc/hosts on each host
- [ ] fstab NFS/CIFS mounts (mediastack-deb → TrueNAS, amontillado → restic-deb)
- [ ] Uptime Kuma monitor URLs
- [ ] Homepage dashboard
- [ ] Zabbix agent configs (Server= line in zabbix_agentd.conf)
- [ ] MkDocs hosts.md, network_inventory.md, vlan_ip_plan.md
- [ ] CLAUDE.md server reference table
- [ ] memory/project_lab_state.md

---

## Open Decisions

- [ ] **Hyper-V VLAN handling** — amontillado on VLAN 20, but Hyper-V VMs need server VLAN access. Options: (a) trunk port for amontillado + separate vSwitch per VLAN, (b) second NIC on amontillado for VLAN 10. Riley to decide.
- [ ] **Dell switch model** — Chris to confirm model this week. Must support 802.1Q. 10G switch possible.
- [ ] **Flint 2 AP mode** — configure before cutover day. Guest WiFi SSID → VLAN 30, main SSID → VLAN 20.
- [ ] **Beryl AP mode** — already in AP mode, needs SSID → VLAN mapping configured.
- [ ] **pihole DNS across VLANs** — pfSense DNS relay points to pihole-pi1-deb (192.168.10.120). All VLANs use pfSense as DNS → pfSense forwards to pihole. No inter-VLAN DNS holes needed.
