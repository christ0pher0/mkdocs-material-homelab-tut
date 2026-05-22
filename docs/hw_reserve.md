# Hardware Reserve
_Last updated: 2026-05-20_
_Spare and undeployed hardware available for upgrades and new builds_
_Inventory in progress — updated as items are found_

---

## Graphics Cards

| Item | Qty | VRAM | Notes |
|------|-----|------|-------|
| NVIDIA GeForce GTX 1080 | 4 | 8GB | Pascal NVENC — 1 transcode stream, no AV1. Undeployed. |
| NVIDIA GeForce GTX 1080 Ti | 2-3 | 11GB | Best choice for AI/Ollama — more VRAM than 1080. 1x in amontillado, 1x moving to TrueNAS rebuild. |

---

## SSDs

### 1TB+
| Item | Qty | Interface | Notes |
|------|-----|-----------|-------|
| Samsung 860 EVO 1TB | 6 | SATA 2.5" | Best in reserve — lee-deb, restic-deb CRU bays, maturin 2.5" bay |
| Crucial MX200 1TB | 1 | SATA 2.5" | Solid mid-range — good for any SATA slot |
| Samsung PM9A3 1.92TB | 1 | NVMe PCIe Gen4 U.2 | Enterprise — needs U.2 to PCIe adapter |
| Orico Y-20M 2TB | 1 | M.2 NVMe | New in box ⭐ — best NVMe in reserve |

### 480-512GB
| Item | Qty | Interface | Notes |
|------|-----|-----------|-------|
| SK Hynix PC600 512GB | 1 | M.2 NVMe | Good NVMe — maturin, idee-deb, urnst-deb candidate |
| Crucial P1 500GB | 1 | M.2 NVMe PCIe Gen3 | Good mid-range NVMe |
| Edge SE B47 512GB | 1 | SATA 3 | Budget — OS drives, light duty |
| Edge SE B47 500GB | 3 | SATA 3 | Budget — OS drives, light duty |
| Edge SE B47 480GB | 2 | SATA 3 | Budget — OS drives, light duty |

### 256GB
| Item | Qty | Interface | Notes |
|------|-----|-----------|-------|
| Samsung PM951 256GB | 1 | M.2 NVMe | Older NVMe — still usable for OS drives |
| Intel M.2 NVMe 256GB | 1 | M.2 NVMe | OS drive candidate |
| Toshiba M.2 256GB | 1 | M.2 SATA | OS drive candidate |
| SK Hynix SC300 256GB | 1 | M.2 SATA | OS drive candidate |
| SK Hynix SH920 256GB | 2 | SATA 2.5" | Decent — OS drives |
| Edge SE B47 256GB | 3 | SATA 3 | Budget — OS drives only |

### 128GB
| Item | Qty | Interface | Notes |
|------|-----|-----------|-------|
| Intel SSD 600P 128GB | 1 | M.2 NVMe | Older NVMe — light OS use only |
| SK Hynix SC300 128GB | 1 | M.2 SATA | Light OS use |
| WD Blue 128GB | 1 | M.2 SATA | Light OS use |
| Crucial BX300 128GB | 2 | SATA 2.5" | Borderline for modern OS — Pi or embedded use |
| Transcend SSD370S 128GB | 1 | SATA 2.5" | Borderline for modern OS — Pi or embedded use |
| 128GB NVMe in mSATA caddy | 1 | mSATA caddy | Confirm form factor before use |

### 64GB and under
| Item | Qty | Interface | Notes |
|------|-----|-----------|-------|
| SanDisk 64GB | 1 | mSATA | Too small for modern OS — embedded only |

---

## External Storage

| Item | Qty | Interface | Notes |
|------|-----|-----------|-------|
| WD My Passport 1TB (black) | 1 | USB 3.0 | Portable backup / data transfer |
| WD My Passport 1TB (red) | 1 | USB 3.0 | Portable backup / data transfer |

---

## RAM — DDR5

| Item | Qty | Speed | Type | Notes |
|------|-----|-------|------|-------|
| Crucial 32GB CT32G4C40U5 | 4 | DDR5-4800 CL40 | UDIMM | Reserve for future DDR5 build — amontillado is maxed |

---

## RAM — DDR4 Desktop (UDIMM)

| Item | Qty | Speed | Notes |
|------|-----|-------|-------|
| SK Hynix 4GB HMA851U6AFR6N | 4 | DDR4-2400 | Low capacity — limited use cases |
| Micron 8GB MTA8ATF1G64AZ | 1 | DDR4-2666 | Desktop UDIMM |
| Micron 8GB MTA16ATF1G64AZ | 2 | DDR4-2133 | Desktop UDIMM — urnst-deb candidate |
| GeIL 8GB GN48GB2400C16S | 1 | DDR4-2400 | Desktop UDIMM |
| Crucial 8GB CT8G4DFS824A | 1 | DDR4-2400 | Desktop UDIMM |
| Crucial 8GB CT8G40FD8213 | 1 | DDR4-2133 | Desktop UDIMM |
| Samsung 8GB M378A1G43DB0 | 2 | DDR4-2133 | Desktop UDIMM — idee-deb upgrade (2 slots empty) |
| PNY XLR8 16GB 16GF2X16QFHH36 | 1 | DDR4-3200 | Desktop UDIMM — matches 1x in shardik, swap plan pending |

---

## RAM — DDR4 ECC Registered (Server Only)

!!! warning "Not compatible with any current fleet boards"
    These require a server/workstation board with ECC Registered support (Xeon, EPYC, Threadripper Pro). None of the current fleet qualifies.

| Item | Qty | Speed | Notes |
|------|-----|-------|-------|
| SK Hynix 8GB HMA81GR7CJR8N | 2 | DDR4-2666 | RDIMM |
| Kingston 8GB KVR21R15S4/8 | 1 | DDR4-2133 | RDIMM |
| SK Hynix 16GB HMA82GR7DJR8N | 2 | DDR4-2933 | RDIMM |
| Kingston 32GB KSM26RD4/32MRR | 1 | DDR4-2666 | RDIMM — valuable for future Xeon build |

---

## RAM — DDR4 SO-DIMM (Laptop)

| Item | Qty | Speed | Notes |
|------|-----|-------|-------|
| SK Hynix 8GB HMA81GS6AFR8N | 1 | DDR4-2400 | Laptop only |
| Crucial 16GB CT16G4SFRA32A | 2 | DDR4-3200 | Laptop only |

---

## RAM — DDR3 Desktop (UDIMM)

| Item | Qty | Speed | Notes |
|------|-----|-------|-------|
| Crucial Ballistix Sport 8GB BLS8G3D1609DS1S00 | 2 | DDR3-1600 | Desktop — truenas upgrade candidate |
| Crucial 8GB CT1024548A1608 | 2 | DDR3-1600 | Desktop UDIMM — truenas upgrade candidate |
| Timetec 8GB 75TT13NU2R8-8G | 2 | DDR3-1333 | Desktop — restic-deb candidate |

### DDR3 Upgrade Plan
| Step | Action | Result |
|------|--------|--------|
| 1 | truenas: pull 2× Hynix 4GB, insert 2× Crucial Ballistix + 2× Crucial UDIMM | truenas → 32GB DDR3-1600 |
| 2 | truenas rebuild: pull 2× Samsung 8GB (currently in truenas) | Samsung sticks freed |
| 3 | restic-deb: insert 2× Samsung 8GB + 2× Timetec 8GB | restic-deb → 32GB |

---

## RAM — DDR3 ECC Registered (Server Only)

!!! warning "Not compatible with any current fleet boards"

| Item | Qty | Speed | Notes |
|------|-----|-------|-------|
| Samsung 4GB M393B5273DH0 | 2 | DDR3L-1333 | RDIMM |
| Hynix 8GB HMT31GR7CFR4A | 2 | DDR3L-1333 | RDIMM |
| Micron 8GB MT36JSF1G72PZ | 2 | DDR3-1600 | RDIMM |
| Crucial 8GB CT102472BB160B | 1 | DDR3-1600 | RDIMM |
| SK Hynix 16GB HMT42GR7BFR4A | 1 | DDR3L-1600 | RDIMM — largest single stick |

---

## Development Boards

| Item | Qty | Notes |
|------|-----|-------|
| Avnet ZUBoard 1CG | 2 | Xilinx/AMD Zynq UltraScale+ FPGA — not homelab hardware, worth keeping for ML/FPGA work |

---

## Ewaste / Misc

| Item | Notes |
|------|-------|
| Dell SanDisk CompactFlash (Version 4.1.4) | Dell server BIOS flash card — no matching hardware, ewaste |
| 2× mSATA caddies (empty) | Spare hardware caddies |

---

## Hard Drives (3.5" HDD)

### Production Drives
| # | Label | Model | Capacity | Serial | Interface | Last Backed Up | Notes |
|---|-------|-------|----------|--------|-----------|----------------|-------|
| 1 | 3D / 4TB | WD Green WD40EZRX | 4TB | TBD | SATA 6Gb/s | Aug 2022 | Update serial when installed |
| 2 | 4TB KICKSTARTER | WD/HGST HC310 HUS726T4ALE6L4 | 4TB | V6KAG1VR | SATA 6Gb/s | Jan 2024 | Dec 2019 |
| 3 | PATREON #-B | Toshiba DT01ACA300 | 3TB | Y5FM2SEGS | SATA 6Gb/s | Jan 2024 | Patreon archive #-B — Nov 2015 |
| 4 | PATREON C-D | Toshiba DT01ACA300 | 3TB | Y5GMAEAGS | SATA 6Gb/s | Feb 2025 | Patreon archive C-D — Nov 2015 |
| 5 | PATREON E-K | Seagate Constellation ES.2 SED ST3000051NS | 3TB | Z2928YTG | SATA 6Gb/s | Feb 2025 | Patreon archive E-K — enterprise SED |
| 6 | PATREON L-O | Seagate Barracuda ST3000DM001 | 3TB | W1F0BALQ | SATA 6Gb/s | Feb 2025 | Patreon archive L-O |
| 7 | PATREON O-Z | WD WD30EZRS | 3TB | WD-WMAWZ0009936 | SATA 6Gb/s | — | Currently in restic-deb bay |
| 8 | TROVE 24-08 | Seagate Enterprise NAS ST6000VN0001 | 6TB | Z401Z7A5 | SATA 6Gb/s | Aug 2024 | DOM 05/2015 |
| 9 | 6 TB SEAGATE 7200 | Seagate Enterprise NAS ST6000VN0001 | 6TB | Z40Z2HT9 | SATA 6Gb/s | — | DOM 05/2015 |
| 10 | READING | Seagate Constellation ES.3 ST3000NM0033 | 3TB | Z1Y32KTB | SATA 6Gb/s | Feb 2025 | DOM 01/2015 |
| 11 | AUDIOBOOKS 3TB | WD Caviar Green WD30EZRS | 3TB | WMAW20629019 | SATA 6Gb/s | Feb 2024 | Nov 2014 |
| 12 | MUSIC+ MUSIC NOT PLEX | Toshiba DT01ACA300 | 3TB | Y5GM81UGS | SATA 6Gb/s | Feb 2024 | Nov 2015 |
| 13 | TROVE BOOKS | Toshiba DT01ACA300 | 3TB | Y5GM22NGS | SATA 6Gb/s | Feb 2024 | Nov 2015 |
| 14 | PLEX ETC | Toshiba DT01ACA300 | 3TB | Y5GM755GS | SATA 6Gb/s | Feb 2024 | Nov 2015 |
| 15 | 3TB TV SONS-T | Hitachi 0F12450 | 3TB | YHG4ZPSA | SATA 6Gb/s | Jan 2024 | TV archive S |
| 16 | 3T TVU-Z | Hitachi 3TB | 3TB | YHG80M8A | SATA 6Gb/s | Jan 2024 | TV archive U-Z |
| 17 | 3T HIT EVERTHING | Seagate Enterprise NAS ST3000VN0001 | 3TB | Z4F95VN8 | SATA 6Gb/s | Feb 2024 | TV archive misc |
| 18 | 3TB TV M-O | Seagate Barracuda ST3000DM001 | 3TB | Z1FKZ6JM | SATA 6Gb/s | Jan 2024 | TV archive M-O |
| 19 | 3TB TV K-L | WD Caviar Green WD30EZRS | 3TB | WMAWZ0J24370 | SATA 6Gb/s | Sep 2022 | TV archive K-L |
| 20 | 3TB TV P-SNOFALL | Seagate Constellation ES.2 SED ST3000051NS | 3TB | Z292M282 | SATA 6Gb/s | Jan 2024 | TV archive P-Snowfall |
| 21 | 3TB SEA TV C-D | Seagate Constellation ES.2 SED ST3000051NS | 3TB | Z2926W97 | SATA 6Gb/s | Jan 2024 | TV archive C-D |
| 22 | 3TB TV E-F GOT | WD Caviar Green WD30EZRS | 3TB | WMAWZ0028623 | SATA 6Gb/s | Jan 2024 | TV archive E-F incl GOT |
| 23 | 3TB TV G-J | WD Caviar Green WD30EZRS | 3TB | WMAWZ036055 | SATA 6Gb/s | Sep 2022 | TV archive G-J |
| 24 | D&D GAMING | Seagate Desktop HDD ST3000DM001 | 3TB | Z5011ZMP | SATA 6Gb/s | Feb 2024 | D&D/Gaming archive |
| 25 | MUSIC 10-21-2018 | Seagate Desktop HDD ST3000DM001 | 3TB | Z5011NMK | SATA 6Gb/s | Feb 2024 | Music archive — date on label is old backup date |
| 26 | TV 0-B / 4TB WDGREEN | WD Green WD40EZRX | 4TB | HARNNY2C48 | SATA 6Gb/s | Jan 2024 | TV archive 0-B |
| 27 | 3WD MOVIES R-Z | Seagate Desktop HDD ST3000DM001 | 3TB | Z50102NP | SATA 6Gb/s | Jan 2024 | Movie archive R-Z |
| 28 | MOVIES H-Q | Seagate | 3TB | B31412046N | SATA 6Gb/s | Jan 2024 | Movie archive H-Q |
| 29 | 3TBSEA MOVIES O-G | Hitachi 0F12450 | 3TB | YHG777BNA | SATA 6Gb/s | Jan 2024 | Movie archive O-G |

### Reserve / Surplus Drives
| # | Label | Model | Capacity | Serial | Interface | Notes |
|---|-------|-------|----------|--------|-----------|-------|
| 1 | Hitachi bare | Hitachi 0F12450 | 3TB | THG3LSNA | SATA 6Gb/s | Dec 2010 — run SMART before trusting |
| 2 | 3TB (unlabeled) | Seagate Constellation ES.2 SED ST3000051NS | 3TB | TBD | SATA 6Gb/s | Enterprise SED — update serial when installed |
| 3 | (unlabeled) | Seagate Constellation ES.2 SED ST3000051NS | 3TB | Z292K11M | SATA 6Gb/s | DOM 05/2012 — enterprise SED |
| 4 | (unlabeled) | Seagate Constellation ES.3 | 3TB | Z1Y38A01 | SATA 6Gb/s | DOM 01/2015 |
| 5 | (unlabeled) | Seagate Constellation ES.2 SED ST3000051N0 | 3TB | Z2923YYH | SATA 6Gb/s | DOM 05/2012 — enterprise SED |
| 6 | *** 2WD CLASS EE | WD Caviar Green WD20EARX | 2TB | WCAZAF839739 | SATA 6Gb/s | *** dispose — check for data first |
| 7 | *** GOODWIM CENTOS | Seagate Barracuda ST500DM002 | 500GB | TBD | SATA 6Gb/s | *** dispose after P2V — convert CentOS install to Proxmox VM first |

### Needs Data Check Before Use
| # | Label | Notes |
|---|-------|-------|
| 1 | 2WD CLASS EE | WD 2TB — unknown contents |
| 2 | GOODWIM CENTOS | Seagate 500GB — unknown contents |

### External HDDs
| Label | Capacity | Notes |
|-------|----------|-------|
| WD My Passport (black) | 1TB | USB 3.0 portable |
| WD My Passport (red) | 1TB | USB 3.0 portable |
