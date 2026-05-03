# Host Software Inventory
_Last updated: 2026-04-15 10:27 PM EDT_
_Auto-generated — do not edit manually_

---

## 2404HV-deb

| Property | Value |
|----------|-------|
| **IP** | 192.168.1.35 |
| **OS** | Ubuntu 24.04 |
| **Virt** | VirtualPC |
| **RAM** | Total: 717Mi / Used: 553Mi / Free: 134Mi |
| **Disk (/)** | Total: 61G / Used: 5.4G / Free: 53G / Use: 10% |
| **Uptime** | up 1 week, 5 days, 18 hours, 22 minutes |

**Services:** ssh, fail2ban, chrony

---

## alma-rpm

| Property | Value |
|----------|-------|
| **IP** | 192.168.1.52 |
| **OS** | AlmaLinux 9.7 |
| **Virt** | kvm |
| **RAM** | Total: 1.7Gi / Used: 396Mi / Free: 1.2Gi |
| **Disk (/)** | Total: 29G / Used: 3.0G / Free: 26G / Use: 11% |
| **Uptime** | up 20 hours, 17 minutes |

**Services:** sshd, fail2ban, chronyd, httpd

---

## apache-deb

| Property | Value |
|----------|-------|
| **IP** | 192.168.1.32 |
| **OS** | Ubuntu 22.04 |
| **Virt** | lxc |
| **RAM** | Total: 4.0Gi / Used: 253Mi / Free: 3.4Gi |
| **Disk (/)** | Total: 16G / Used: 4.1G / Free: 11G / Use: 28% |
| **Uptime** | up 20 hours, 18 minutes |

**Services:** ssh, chrony, docker, apache2

**Containers (running):** portainer_agent, cadvisor

---

## docker-deb

| Property | Value |
|----------|-------|
| **IP** | 192.168.1.34 |
| **OS** | Ubuntu 24.04 |
| **Virt** | kvm |
| **RAM** | Total: 1.9Gi / Used: 650Mi / Free: 104Mi |
| **Disk (/)** | Total: 31G / Used: 9.4G / Free: 20G / Use: 33% |
| **Uptime** | up 20 hours, 17 minutes |

**Services:** ssh, fail2ban, docker

**Containers (running):** caddy, vaultwarden, traefik, nginx, portainer

---

## git-ansible-deb

| Property | Value |
|----------|-------|
| **IP** | 192.168.1.3 |
| **OS** | Ubuntu 24.04 |
| **Virt** | kvm |
| **RAM** | Total: 3.8Gi / Used: 1.5Gi / Free: 349Mi |
| **Disk (/)** | Total: 63G / Used: 22G / Free: 39G / Use: 36% |
| **Uptime** | up 20 hours, 17 minutes |

**Services:** ssh, fail2ban, docker, apache2

**Containers (running):** gitea, portainer_agent

---

## grafana-docker-deb

| Property | Value |
|----------|-------|
| **IP** | 192.168.1.21 |
| **OS** | Ubuntu 24.04 |
| **Virt** | lxc |
| **RAM** | Total: 4.0Gi / Used: 561Mi / Free: 2.7Gi |
| **Disk (/)** | Total: 503G / Used: 11G / Free: 468G / Use: 3% |
| **Uptime** | up 20 hours, 18 minutes |

**Services:** ssh, chrony, docker

**Containers (running):** portainer_agent, pve-exporter, cadvisor, prometheus, grafana, portainer

---

## kasm-2404-deb

| Property | Value |
|----------|-------|
| **IP** | 192.168.1.26 |
| **OS** | Ubuntu 24.04 |
| **Virt** | kvm |
| **RAM** | Total: 3.8Gi / Used: 1.7Gi / Free: 234Mi |
| **Disk (/)** | Total: 30G / Used: 16G / Free: 15G / Use: 53% |
| **Uptime** | up 20 hours, 16 minutes |

**Services:** ssh, fail2ban, chrony, docker

**Containers (running):** kasm_proxy, kasm_rdp_https_gateway, kasm_share, kasm_rdp_gateway, kasm_agent, kasm_api, kasm_guac, kasm_manager, kasm_redis, kasm_db, portainer_agent, cadvisor

---

## mediastack-deb

| Property | Value |
|----------|-------|
| **IP** | 192.168.1.36 |
| **OS** | Ubuntu 24.04 |
| **Virt** | kvm |
| **RAM** | Total: 3.8Gi / Used: 2.2Gi / Free: 294Mi |
| **Disk (/)** | Total: 159G / Used: 29G / Free: 124G / Use: 19% |
| **Uptime** | up 20 hours, 16 minutes |

**Services:** ssh, fail2ban, docker

**Containers (running):** portainer_agent, romm, seerr, komga, mylar, lidarr, radarr, sabnzbd, sonarr, vpn, mariadb, prowlarr, audiobookshelf

---

## octopi-deb

| Property | Value |
|----------|-------|
| **IP** | 192.168.1.122 |
| **OS** | Debian 12 |
| **Virt** | NA |
| **RAM** | Total: 3.7Gi / Used: 339Mi / Free: 2.9Gi |
| **Disk (/)** | Total: 29G / Used: 3.9G / Free: 24G / Use: 15% |
| **Uptime** | up 1 week, 1 day, 13 hours, 39 minutes |

**Services:** ssh, fail2ban, chrony

---

## pihole-book-deb

| Property | Value |
|----------|-------|
| **IP** | 192.168.1.33 |
| **OS** | Debian 12.13 |
| **Virt** | lxc |
| **RAM** | Total: 512Mi / Used: 66Mi / Free: 337Mi |
| **Disk (/)** | Total: 7.8G / Used: 1.7G / Free: 5.8G / Use: 22% |
| **Uptime** | up 20 hours, 16 minutes |

**Services:** ssh

---

## plow-rpm

| Property | Value |
|----------|-------|
| **IP** | 192.168.1.53 |
| **OS** | RedHat 9.6 |
| **Virt** | VirtualPC |
| **RAM** | Total: 5.7Gi / Used: 2.0Gi / Free: 809Mi |
| **Disk (/)** | Total: 70G / Used: 16G / Free: 55G / Use: 22% |
| **Uptime** | up 1 week, 1 day, 16 hours, 49 minutes |

**Services:** sshd, fail2ban, chronyd, docker

**Containers (running):** portainer_agent, snipe-it-app-1, snipe-it-db-1, audiobookshelf-app-1, site2-nginx-1, nginx1

---

## rocky-rpm

| Property | Value |
|----------|-------|
| **IP** | 192.168.1.51 |
| **OS** | Rocky 9.7 |
| **Virt** | kvm |
| **RAM** | Total: 1.7Gi / Used: 706Mi / Free: 634Mi |
| **Disk (/)** | Total: 29G / Used: 6.7G / Free: 23G / Use: 23% |
| **Uptime** | up 20 hours, 17 minutes |

**Services:** sshd, fail2ban, chronyd, httpd

---

## snipeit-deb

| Property | Value |
|----------|-------|
| **IP** | 192.168.1.20 |
| **OS** | Debian 18.0-bookworm-amd64 |
| **Virt** | lxc |
| **RAM** | Total: 2.0Gi / Used: 334Mi / Free: 1.0Gi |
| **Disk (/)** | Total: 7.8G / Used: 2.8G / Free: 4.7G / Use: 38% |
| **Uptime** | up 2 days, 12 hours, 59 minutes |

**Services:** ssh, fail2ban, docker, apache2

**Containers (running):** portainer_agent, cadvisor

---

## swarm01-deb

| Property | Value |
|----------|-------|
| **IP** | 192.168.1.22 |
| **OS** | Ubuntu 24.04 |
| **Virt** | kvm |
| **RAM** | Total: 1.9Gi / Used: 671Mi / Free: 350Mi |
| **Disk (/)** | Total: 31G / Used: 12G / Free: 18G / Use: 41% |
| **Uptime** | up 20 hours, 18 minutes |

**Services:** ssh, fail2ban, chrony, docker, apache2

**Containers (running):** portainer_agent
**Containers (stopped):** cadvisor

---

## swarm02-deb

| Property | Value |
|----------|-------|
| **IP** | 192.168.1.23 |
| **OS** | Ubuntu 24.04 |
| **Virt** | kvm |
| **RAM** | Total: 1.9Gi / Used: 755Mi / Free: 148Mi |
| **Disk (/)** | Total: 31G / Used: 8.7G / Free: 21G / Use: 31% |
| **Uptime** | up 20 hours, 17 minutes |

**Services:** ssh, fail2ban, chrony, docker, apache2

**Containers (running):** portainer_agent, cadvisor

---

## swarm03-deb

| Property | Value |
|----------|-------|
| **IP** | 192.168.1.24 |
| **OS** | Ubuntu 24.04 |
| **Virt** | kvm |
| **RAM** | Total: 1.9Gi / Used: 744Mi / Free: 88Mi |
| **Disk (/)** | Total: 31G / Used: 8.3G / Free: 21G / Use: 29% |
| **Uptime** | up 20 hours, 17 minutes |

**Services:** ssh, fail2ban, chrony, docker, apache2

**Containers (running):** portainer_agent, cadvisor

---

## ubuntu-ansible-deb

| Property | Value |
|----------|-------|
| **IP** | 192.168.1.25 |
| **OS** | Ubuntu 24.04 |
| **Virt** | kvm |
| **RAM** | Total: 3.8Gi / Used: 555Mi / Free: 2.9Gi |
| **Disk (/)** | Total: 30G / Used: 3.7G / Free: 27G / Use: 13% |
| **Uptime** | up 20 hours, 19 minutes |

**Services:** ssh, fail2ban, chrony, docker

**Containers (running):** portainer_agent, cadvisor

---
