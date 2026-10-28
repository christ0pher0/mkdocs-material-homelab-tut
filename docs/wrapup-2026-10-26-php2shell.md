# Session Wrap-Up — 2026-10-26

**Focus:** PHP2Shell remediation, monitor-deb disk expansion, Pi-hole cleanup, inventory fix

---

## PHP2Shell (CVE-2026-109618 / CVE-2026-109619)

Two critical pre-auth RCE flaws in PHP 5.4–8.5, patched upstream 2026-10-21.
Fixed versions: **8.5.12, 8.4.27, 8.3.36, 8.2.35**. Distros backport without bumping the version number.

| Host | PHP source | Before | Action | Result |
|---|---|---|---|---|
| pi4-deb | Debian package (lighttpd + php-fpm) | 8.4.24 | `dpkg` lock cleared by itself; `apt upgrade` | ✅ 8.4.27, kernel 6.18.50 |
| backup-dietpi-deb | Debian package (lighttpd + php-fpm) | 8.4.24 | `dpkg --configure -a`, `apt upgrade`, reboot | ✅ 8.4.27, kernel 6.18.50 |
| pi2-deb, blank-dietpi-deb | Debian package | 8.4.27 | none | ✅ already patched |
| git-ansible-deb | Ubuntu package (Apache mod_php) | 8.3.6-0ubuntu0.24.04.13 | `a2dismod php8.3` (nothing used it) | ✅ already patched + PHP removed from Apache |
| alma-rpm | RHEL backport | 8.0.30 | changelog verified | ✅ lists both CVEs |
| monitor-deb (zabbix-web container) | Alpine image | 8.5.5 | pinned to `alpine-7.4-latest`, pulled, recreated | ✅ 8.5.12 |
| docker-deb (Firefly III) | `fireflyiii/core:latest` | 8.5.7 | DB dump, pulled, recreated `app` | ✅ 8.5.12 |
| plow-rpm (Snipe-IT) | `snipe/snipe-it:latest` (Ubuntu) | 8.3.6 | DB dump, pulled, recreated `app` | ✅ 8.3.6-0ubuntu0.24.04.13 |
| pihole-pi1-deb | — | none installed | none | ✅ not exposed |

### Lessons

- **Ubuntu:** `php -v` stays at 8.3.6 after patching. Check the package version instead: the fixed build is `8.3.6-0ubuntu0.24.04.13`.

  ```bash
  dpkg -l 'php8.3*' | awk '/^ii/ {print $2, $3}'
  ```

- **Build dates mislead:** distro security builds are compiled during the embargo, so a build date before 2026-10-21 does not mean unpatched.
- **Containers carry their own PHP.** Host package updates do not touch them; only a new image plus recreating the container does.
- **`docker compose pull` alone does nothing** to a running container. `docker compose up -d <service>` is required.
- **PHP-FPM-only images** (e.g., Zabbix web) have no `php` binary. Find the FPM binary with:

  ```bash
  docker exec <container> sh -c 'ls /usr/sbin /usr/bin | grep -i php'
  ```

- **Ansible `raw` module** works on hosts with a full disk; normal modules fail because they need temp space.

---

## monitor-deb (VM 101 on maturin) — disk full

- Root LV was **100% full (30G)**. The cause was Docker: about 11G in `/var/lib/containerd` plus 7.5G in `/var/lib/docker`.
- `docker image prune -a` freed 2.9G, bringing it to 96%.
- PBS backup taken first: `vzdump 101 --storage pbs`.
- Grew the disk online: `qm resize 101 scsi0 +20G` on maturin, then inside the VM: rescan, `growpart /dev/sda 3`, `pvresize /dev/sda3`, `lvextend -r -l +100%FREE`.
- **Result: 50G, 57% used, 21G free.** No downtime.

### Zabbix version pinning

- `docker-compose.yml` backed up to `docker-compose.yml.bak-2026-10-26`.
- `zabbix-server` and `zabbix-web` images changed from `:latest` to `:alpine-7.4-latest`, to prevent an accidental major upgrade (which would mean a one-way DB migration).
- Zabbix went from 7.4.10 to **7.4.16**.

---

## pihole-pi1-deb (192.168.1.120) — SD card full

- 4 GB card (3.3G root) at 100%.
- `apt clean` freed about 400 MB.
- `apt autoremove --purge` finished a stalled kernel install (6.12.109) and purged old kernels.
- Added `127.0.1.1 pihole-pi-deb` to `/etc/hosts`, which fixes the `sudo: unable to resolve host` warning.
- Rebooted. **Now on kernel 6.12.109+rpt-rpi-v6, 88% used, 395 MB free.**
- The real hostname is `pihole-pi-deb` (it does not match the inventory name).

---

## Inventory cleanup (git-ansible)

- `pi1-deb` and `pihole-pi1-deb` were the **same machine** (.120).
- `/etc/hosts` backed up to `/etc/hosts.bak-2026-10-26`, and the `pi1-deb` line removed.
- Regenerated `inventory_auto`: 42 hosts. Only `pihole-pi1-deb` remains, matching the hardcoded entry in `generate_inventory.py` line 91.

---

## Follow-ups

- [ ] Recreate Firefly III `cron` container on the patched image (`docker compose up -d cron` on docker-deb) and verify
- [ ] Log in to Firefly III and Zabbix web UI to confirm both work after the update
- [ ] Replace pihole-pi1-deb's 4 GB SD card with 16 GB+; kernel updates will keep filling it
- [ ] Decide whether to rename the inventory entry to match the real hostname `pihole-pi-deb`
- [ ] Remove stale inventory hosts still listed but gone or offline (babar, shardik, urnst-deb, etc.)
- [ ] Restrict `nvme_store`, `nvme128`, `nvme512`, `SDA_store`, `hdd3tb`, `hdd12tb`, and `tank-storage` to the nodes that actually have those disks (they resolve to root disks on maturin and aslan)
- [ ] Consider pinning other `:latest` images in monitor-deb's compose file
- [ ] Optional: stop or disable Apache on git-ansible if nothing uses it

### Notes

- plow-rpm SSH host key changed. Expected: the cloud-init changes from 2026-10-21 regenerated its keys.
- Ansible vault "Decryption failed" errors on 2026-10-26 were transient; only one vault file exists (`group_vars/all/tailscale.yml`).
