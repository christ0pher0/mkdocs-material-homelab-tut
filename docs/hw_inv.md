# Hardware Inventory
_Last updated: 2026-05-15_
_Physical hosts only — VMs/containers documented in network_context.md_
_Ordered by utility — least capable first, most capable last_
!!! tip "Adding Photos"
    Save host photos to `docs/images/hw/` and name them to match the image references below (e.g. `proxmox-deb.jpg`).
---
## Ewaste / Recycled
| Photo | System | Reason |
|-------|--------|--------|
| ![sys2](images/hw/waiting-02-ewaste.jpg){ width=100 } | MSI H61M-P23 (B3) — LGA1155 | Broken CPU cooler, won't POST — recycled |
---
## lee-deb — Dell Inspiron 3647
| | |
|--|--|
| ![lee](images/hw/lee-deb.jpg){ width=300 } | **Role:** Immich photo server — memorial machine<br>**Make:** Dell Inspiron 3647 (Small Form Factor)<br>**Chipset:** Intel H81 (Haswell, 2013)<br>**CPU:** Unknown — up to i7-4790 (4th gen)<br>**RAM:** Unknown — max 16GB DDR3<br>**Storage:** Samsung 870 EVO 1TB SSD (pending install)<br>**OS:** Ubuntu Server 26.04 LTS (pending install)<br>**IP:** Not yet assigned<br>**PSU:** 220W — low-profile GPU only<br>**Name:** lee — personal/memorial<br>**Best uses:** Immich photo server, lightweight Linux utility box, PiHole<br>**Easy upgrades:** SSD already planned. RAM cheap if needed.<br>**Notes:** Sentimental machine — belongs to family. Original HDD preserved as-is. |
---
## eld-win (192.168.1.101)
| | |
|--|--|
| ![eld](images/hw/eld.jpg){ width=300 } | **Role:** Restic backup server — pending Ubuntu 26.04 migration<br>**Motherboard:** Gigabyte Z77-DS3H (Intel Z77, LGA1155)<br>**CPU:** Intel Core i5-2500K @ 3.30GHz (Sandy Bridge 2011)<br>**RAM:** 16GB DDR3 1600MHz (4x 4GB matched kit)<br>**RAM max:** 32GB DDR3 (4x 8GB) — DDR3 is cheap, easy upgrade<br>**BIOS:** AMI 2012-08-20<br>**OS:** Windows 10 (EOL) → Ubuntu 26.04 (pending)<br>**Form factor:** Thermaltake white full tower — 2x CRU hot-swap bays, USB 3.0 front panel<br>**Storage:** Disk 0: 238GB SSD (C: OS, 38% free) + Disk 1: 2.79TB HDD (D: Patreon O-Z, 10% free ⚠️) + DVD drive<br>**Best uses:** Restic backup server, manual CRU drive rotation, offsite cold storage<br>**Easy upgrades:** Upgrade RAM to 32GB DDR3 before Ubuntu migration. Add drives to CRU bays.<br>**Backup role:** Tier 1 — Restic automated. Tier 2 — 2x CRU bays rotating drives. Tier 3 — offsite cold storage. |
---
## truenas (192.168.1.5) — NAS Primary Storage
| | |
|--|--|
| ![freenas](images/hw/freenas.jpg){ width=300 } | **Role:** NAS — primary storage<br>**Motherboard:** Gigabyte Z77-DS3H (Intel Z77, LGA1155) — ⚠️ pending replacement with temerant hardware<br>**CPU:** Intel Core i5-3570K @ 3.40GHz (4 cores) — Ivy Bridge 2012 — ⚠️ pending replacement<br>**RAM:** 24GB DDR3 1600MHz (mixed kit) — ⚠️ pending replacement with 32GB DDR4<br>**BIOS:** AMI F9 (2012-09-19)<br>**OS:** TrueNAS CORE 13.0-U6.8 — migrated 2026-04-27<br>**Hostname:** freenas-bsd<br>**NIC:** onboard alc0 non-functional — running on USB NIC (ue0) at 192.168.1.5<br>**Form factor:** Beige full tower ATX (~1999) — 5x CRU hot-swap bays, 1x CRU bay available, 2x internal mounts available<br>**RAM max:** 32GB DDR3 — pending upgrade to 32GB DDR4 via temerant hardware swap<br>**Best uses:** NAS — irreplaceable 45TB RAIDZ1 pool.<br>**History:** Case bought 1999. TRYAGAIN pool survived a motherboard failure — imported in 30 minutes after emergency mobo swap. No data loss. Migrated from FreeNAS 11.3 to TrueNAS 13.0 on 2026-04-27.<br><br>**⭐ Planned Hardware Rebuild — temerant components:**<br>- Gigabyte AB350-Gaming (AMD B350, AM4)<br>- Ryzen 5 1600X (6c/12t)<br>- 32GB DDR4<br>- GTX 1080 Ti (Plex hardware transcoding)<br>- 500GB SSD for TrueNAS OS boot (replace USB drives)<br>- LSI 9207-8i or 9211-8i HBA (~$20-40 eBay) + 2x SFF-8087 breakout cables<br>- Future: up to 8 drives total — 1x CRU hot-swap + 2x internal mounts available |
### Storage
| Pool | Drives | Size each | Raw Total | Layout | Status | Used | Free |
|------|--------|-----------|-----------|--------|--------|------|------|
| TRYAGAIN | 5x (ada0-ada4) | 18.19TiB | 90TB raw / 70TB usable (RAIDZ1) | RAIDZ1 — 1 drive parity | HEALTHY | 45TB used (65%) | 24.6TiB |
| freenas-boot | 2x USB | ~14GB | ~28GB | Mirror — degraded | DEGRADED | — | — |
### TRYAGAIN Datasets
| Dataset | Type | Used | Notes |
|---------|------|------|-------|
| plex | dataset | 44.45TiB | Main media — CIFS mounted on mediastack-deb |
| jails | dataset | 1.15TiB | Weltgeist + Alea Iacta Est — decommissioned, pending deletion |
| iocage | dataset | 91.74GiB | Jail manager — pending deletion |
| QUANTUM-g52439 | zvol | 25.61GiB | VM or iSCSI target |
### ZFS Health
- Last scrub: 2026-04-06 — 0 errors
- Read/Write/Checksum errors: 0 on all drives
- One drive failure tolerance (RAIDZ1)
- ⚠️ ada4 — bad sectors alert from February 2026, needs investigation
- ⚠️ Boot pool degraded — second USB drive needs replacement
---
## Raspberry Pis
| Photo | Hostname | IP | Model | CPU | RAM | Storage | Best Use | Status |
|-------|----------|----|-------|-----|-----|---------|----------|--------|
| ![pi3](images/hw/pi3-deb.jpg){ width=100 } | pi3-deb | 192.168.1.124 | RPi Model B Rev 2 (BCM2835) Rev 000e — 256MB — clear RetroPie case | ARM 1-core | 239MB | 15GB SD | RetroPie/Buster — legacy, Python 3.7, cannot Ansible manage. Keep as NES/SNES/GB only. | Online |
| ![pi1](images/hw/pi1-deb.jpg){ width=100 } | pi1-deb | 192.168.1.120 | RPi Model B Rev 2 (BCM2835) Rev 000f — 512MB — blue-green case | ARM 1-core | 427MB | 3.8GB SD (91% full ⚠️) | Raspbian Bookworm — onboarded ✅ — Secondary PiHole or MQTT broker. Needs larger SD card. | Online |
| ![pi2](images/hw/pi2-deb.jpg){ width=100 } | pi2-deb | 192.168.1.121 | RPi Model B Rev 2 (BCM2835) Rev 000f — 512MB — bare board | ARM 1-core | 475MB | 7.2GB SD | DietPi — onboarded ✅ — MQTT broker for HA IoT | Online |
| ![pi4](images/hw/pi4-deb.jpg){ width=100 } | pi4-deb | 192.168.1.126 | RPi 2 Model B Rev 1.1 (BCM2836) — 1GB — official white case | ARM 4-core | 762MB | 29GB SD | DietPi v10.2.3 — onboarded ✅ — Zigbee coordinator + MQTT broker | Online |
| ![octopi](images/hw/octopi-deb.jpg){ width=100 } | octopi-deb | 192.168.1.122 | RPi 4 Model B Rev 1.1 (BCM2711) — CanaKit clear case | ARMv7 4-core | 3.7GB | 29GB SD | OctoPrint — controls Creality Ender 3 V2 | Online |
| ![ha](images/hw/ha-net.jpg){ width=100 } | ha-net | 192.168.1.125 | RPi 4 Model B Rev 1.4 — CanaKit black case | ARM 4-core | 3.7GB | 28.6GB | Home Assistant OS 17.2 / Core 2026.4.2 | Online |
| ![batocera](images/hw/batocera.jpg){ width=100 } | batocera-deb | 192.168.1.123 | RPi 5 Model B Rev 1.0 | ARM 4-core | 3.9GB | 111GB SD | Best retro gaming — PS2, GameCube, Dreamcast, some Switch (Batocera) | Online |
| ![argos](images/hw/argos-deb.jpg){ width=100 } | argos-deb | 192.168.1.127 | RPi 4 Model B Rev 1.1 — 1GB — ewaste find! | ARM 4-core | 870MB | 32GB PNY | Fully kitted IoT field station — touchscreen, camera, LTE, LoRa | Online |
---
## argos-deb (192.168.1.127)
| | |
|--|--|
| ![argos](images/hw/argos-deb.jpg){ width=300 } | **Role:** IoT field station — TBD<br>**Model:** Raspberry Pi 4 Model B Rev 1.1 (BCM2711)<br>**RAM:** 1GB (870MB available)<br>**Storage:** 32GB PNY microSD (Bookworm 64-bit)<br>**OS:** Raspberry Pi OS Bookworm 64-bit — onboarded ✅<br>**IP:** 192.168.1.127<br>**Origin:** Ewaste find — someone's serious IoT project<br>**Display:** Official Raspberry Pi 7" touchscreen ✅ working<br>**Camera:** Raspberry Pi Camera V2.1 — untested on Bookworm<br>**Cellular:** Sixfab mPCI-E Base Shield V2 + Quectel EC25-A 4G LTE — needs SIM card<br>**Radio:** Adafruit RFM9x LoRa — long range RF, GPIO connected<br>**Best uses:** Mobile homelab node (Tailscale+LTE), LoRa gateway, security camera, HA kiosk display, field sensor station<br>**Easy upgrades:** Add SIM card (Hologram.io), reconnect Sixfab shield, test LoRa radio |
---
## 3D Printers
| Photo | Printer | Type | Controller | Status | Notes |
|-------|---------|------|-----------|--------|-------|
| ![ender3v1](images/hw/ender3v1.jpg){ width=100 } | Creality Ender 3 V1 | FDM | None assigned | Needs Pi | Could add another OctoPrint Pi |
| ![mars3](images/hw/mars3.jpg){ width=100 } | Elegoo Mars 3 | Resin (MSLA) | None | Standalone | Chitubox slicer, no OctoPrint |
| ![dreamer](images/hw/dreamer.jpg){ width=100 } | Flashforge Dreamer | FDM dual extrusion | None | Standalone | FlashPrint software |
| ![ender3v2](images/hw/ender3v2.jpg){ width=100 } | Creality Ender 3 V2 | FDM | octopi-deb (OctoPrint) | ✅ Active | Controlled via RPi 4 |
---
## GPU Stock (undeployed)
| Photo | Item | Qty | VRAM | Notes |
|-------|------|-----|------|-------|
| ![1080](images/hw/gtx1080.jpg){ width=100 } | GTX 1080 | 4 (undeployed) | 8GB each | Pascal NVENC — 1 transcode stream, no AV1 |
| ![1080ti](images/hw/gtx1080ti.jpg){ width=100 } | GTX 1080 Ti | 4-5 total (1 in amontillado, 1 moving to truenas rebuild, 2-3 undeployed) | 11GB VRAM | Best choice for AI/Ollama node — more VRAM than 1080 |
---
## pve3 (offsite — ThinkStation)
| | |
|--|--|
| ![thinkstation](images/hw/thinkstation.jpg){ width=300 } | **Role:** Proxmox VE node 3 — offsite<br>**Make:** Lenovo ThinkStation (model unknown)<br>**CPU:** Unknown<br>**RAM:** Unknown<br>**Storage:** Unknown<br>**OS:** Proxmox VE<br>**Location:** Offsite<br>**Tailscale:** Not yet configured<br>**Best uses:** Proxmox node 3 — proper 3-node quorum, offsite DR<br>**Notes:** Needs full inventory, Tailscale, and documentation |
---
## Unknown Waiting System
| Photo | # | Notes |
|-------|---|-------|
| ![sys5](images/hw/waiting-05.jpg){ width=100 } | 5 | Unknown — not yet inventoried |
---
## urnst-deb (192.168.1.27)
| | |
|--|--|
| ![urnst](images/hw/urnst-deb.jpg){ width=300 } | **Role:** Hardware diagnostics + TBD — Proxmox node 3 or PBS candidate<br>**Motherboard:** Gigabyte AB350-Gaming-CF (AMD B350, AM4)<br>**CPU:** AMD Ryzen 5 1600X (6c/12t, 3.6GHz)<br>**RAM:** 8GB DDR4 2133 (1x DIMM, 3 slots empty)<br>**RAM max:** 16GB DDR4 (4x 4GB)<br>**GPU:** AMD Radeon HD 7450 — display only<br>**OS:** Debian 13 (Trixie) — fresh install 2026-04-13<br>**Form factor:** Thermaltake white full tower — 2x 5.25" bays, front USB<br>**IP:** 192.168.1.27<br>**Name:** Urnst — County of Urnst, Greyhawk<br>**Best uses:** Proxmox node 3, PBS backup server, general Linux server, CPU swap test bench<br>**Easy upgrades:** Add 3x 4GB DDR4 to reach 16GB max. Replace HD 7450 with GTX 1080/1080 Ti from stock.<br>**Current task:** Using as AM4 test bench to diagnose unknown system that won't boot — swap CPU from urnst to test whether fault is CPU or motherboard. |
### Storage
| Device | Type | Size | Notes |
|--------|------|------|-------|
| sda | HDD | 2.7TB | OS drive — Debian installed |
| sdb | HDD | 2.7TB | Empty |
| sdc | HDD | 2.7TB | Empty |
---
## maturin (192.168.1.7) — Proxmox node 2
| | |
|--|--|
| ![pve2](images/hw/pve2-deb.jpg){ width=300 } | **Role:** Proxmox VE node 2<br>**Make:** Dell OptiPlex 7050 (SFF)<br>**Motherboard:** Dell 0NW6H5<br>**CPU:** Intel Core i7-6700 @ 3.40GHz (4c/8t, Skylake 2015)<br>**RAM:** 16GB DDR4 2400MHz (4x 4GB SK Hynix)<br>**RAM max:** 64GB DDR4 (4x 16GB)<br>**BIOS:** Dell 1.11.0 (2018-11-01)<br>**OS:** Proxmox VE / Debian 12<br>**Storage:** 476.9GB SATA SSD — single disk (96GB root, 348.8GB Proxmox data pool)<br>**IP:** 192.168.1.7<br>**Form factor:** Small form factor desktop<br>**M.2 slot:** Empty — supports PCIe NVMe (2280) — upgrade candidate<br>**2.5" bay:** Possibly empty — check physically<br>**Best uses:** Proxmox node 2 — currently running kasm, alma-rpm, rocky-rpm, pihole<br>**Easy upgrades:** RAM to 64GB DDR4 (4x 16GB). Install 2TB NVMe in empty M.2 slot OR 2TB SSD in 2.5" bay for dedicated VM storage pool. |
---
## idee-deb (192.168.1.28)
| | |
|--|--|
| ![idee](images/hw/idee-deb.jpg){ width=300 } | **Role:** TBD — AI node or Proxmox node 3 candidate<br>**Motherboard:** Gigabyte AB350-Gaming 3-CF (AMD B350, AM4)<br>**CPU:** AMD Ryzen 5 1600X (6c/12t, 3.6GHz)<br>**RAM:** 16GB DDR4 2133 dual channel — 2x 8GB G.Skill Trident Z RGB<br>**RAM max:** 128GB DDR4<br>**Storage:** Samsung 970 EVO Plus 500GB NVMe<br>**GPU:** AMD Radeon HD 7450 (placeholder — display only)<br>**OS:** Debian 13 (Trixie) + GNOME — fresh install 2026-04-13<br>**Form factor:** Mid-tower, tempered glass side panel, full RGB<br>**IP:** 192.168.1.28<br>**Name:** Idee — Duchy of Idee, Greyhawk<br>**Best uses:** AI/Ollama node with GTX 1080 Ti passthrough, Proxmox node 3, GPU transcoding server<br>**Easy upgrades:** GTX 1080 Ti from stock (biggest single improvement — 11GB VRAM for AI/Ollama). RAM upgradeable to 128GB DDR4. |
### Storage
| Device | Type | Size | Model | Notes |
|--------|------|------|-------|-------|
| nvme0n1 | NVMe | 465.8GB | Samsung 970 EVO Plus 500GB | OS drive |
---
## temerant-win (192.168.1.105) — ⭐ Donor system for TrueNAS rebuild
| | |
|--|--|
| ![temerant](images/hw/temerant-win.jpg){ width=300 } | **Role:** Hardware donor for TrueNAS rebuild — pending data check<br>**Motherboard:** Gigabyte AB350-Gaming (AMD B350, AM4)<br>**CPU:** AMD Ryzen 5 1600X (6c/12t, 3.6GHz)<br>**RAM:** 32GB DDR4 2133 (4x 8GB G.Skill F4-2400C15 — full 4 slots)<br>**RAM max:** 64GB DDR4<br>**GPU:** NVIDIA GeForce GTX 1080 Ti (11GB VRAM) ✅ already installed<br>**OS:** Windows 10 Pro (1909 — EOL) — LaunchBox/ROM gaming<br>**Form factor:** Mid-tower, tempered glass, AIO cooler, RGB<br>**IP:** 192.168.1.105<br>**Name:** Temerant — world of Kingkiller Chronicle (Rothfuss)<br>**Planned fate:** Gut mobo + CPU + RAM + GPU + 500GB SSD → install into TrueNAS beige full tower. Temerant chassis retired.<br>**⚠️ Before gutting:** Check 2x 3TB HDDs for important data. Move to urnst-deb or eld-win if needed.<br>**Notes:** Currently used for LaunchBox ROM gaming (Z:\ROMs mapped from \\freenas\plex\ROMs). RetroAchievements configured. |
### Storage
| Device | Type | Size | Notes |
|--------|------|------|-------|
| Disk C: | SSD | 500GB | OS drive — will become TrueNAS boot drive |
| Disk D: | HDD | 3TB | Seagate ST3000DM001 — check for data ⚠️ |
| Disk E: | HDD | 3TB | Seagate ST3000DM001 — check for data ⚠️ |
---
## shardik (192.168.1.2) — Proxmox node 1
| | |
|--|--|
| ![proxmox-deb](images/hw/proxmox-deb.jpg){ width=300 } | **Role:** Proxmox VE node 1 — primary hypervisor<br>**Motherboard:** ASRock AB350M Pro4<br>**CPU:** AMD Ryzen 5 1600 (6c/12t) — upgrade candidate: Ryzen 7 2700X (~$30-50 used, drop-in)<br>**RAM:** 56GB DDR4 2667MHz — 4x DIMM: 16GB+16GB+16GB+8GB<br>**RAM max:** 64GB — replace 8GB Micron stick to max out<br>**BIOS:** AMI P10.43 (supports Ryzen 7 2700X natively)<br>**OS:** Proxmox VE / Debian 12<br>**Form factor:** Cooler Master full tower — 5x CRU hot-swap bays, LG optical<br>**IP:** 192.168.1.2<br>**ZFS:** Masked off (systemd.mask=zfs-mount.service) — ZFS recovery failed 2026-05, node rebuilt<br>**Best uses:** Primary hypervisor — runs swarm, mediastack, docker, git-ansible, monitor-deb<br>**Easy upgrades:** Ryzen 7 2700X (~$30-50 eBay) — 8c/16t, same socket, BIOS already supports it. Replace 8GB Micron with 16GB DDR4 2667 to reach 64GB. |
### Storage
| Device | Type | Size | Model | FS |
|--------|------|------|-------|----|
| nvme0n1 | NVMe | 1.02TB | Kioxia KXG60ZNV1T02 | LVM (OS) |
| sda | HDD | 6TB | Seagate ST6000DX000 | ext4 |
| sdb | HDD | 6TB | Toshiba HDWE160 | ZFS |
| sdc | HDD | 6TB | Toshiba HDWE160 | ext4 |
| sdd | HDD | 6TB | Seagate ST6000VN0001 | ZFS |
---
## amontillado-win (192.168.1.100) ⭐ Best System
| | |
|--|--|
| ![amontillado](images/hw/amontillado.jpg){ width=300 } | **Role:** Primary workstation / AI powerhouse<br>**Motherboard:** MSI PRO Z690-A WIFI (MS-7D25)<br>**CPU:** Intel i7-13700K (16 cores / 24 threads — Raptor Lake 2022)<br>**RAM:** 128GB DDR5 4000MHz — 4x 32GB: G.Skill + Crucial<br>**BIOS:** AMI A.F0 (2023-11-13)<br>**OS:** Windows 11 + Hyper-V<br>**GPU:** NVIDIA GeForce GTX 1080 Ti (11GB VRAM) + Intel UHD Graphics<br>**Form factor:** Phanteks Eclipse P400A — mesh front, tempered glass, RGB<br>**IP:** 192.168.1.100<br>**Name:** Amontillado — Poe<br>**Best uses:** Primary workstation, Hyper-V host, AI workloads, heavy compilation, anything that needs 128GB RAM<br>**Easy upgrades:** Upgrade GPU to RTX 3090/4090 for serious AI work — i7-13700K won't bottleneck it. |
### Storage
| Drive | Size | FS | Label | Free |
|-------|------|----|-------|------|
| Disk 0 | 465GB | NTFS | F: | 39% |
| Disk 1 | 2.79TB | NTFS | D: New Volume | 11% ⚠️ |
| Disk 2 | 931GB | NTFS | C: OS | 20% |

