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
| # | Label | Model | Capacity | Serial | Interface | Notes |
|---|-------|-------|----------|--------|-----------|-------|
| 1 | 4TB KICKSTARTER | WD/HGST HC310 HUS726T4ALE6L4 | 4TB | V6KAG1VR | SATA 6Gb/s | Dec 2019 |
| 2 | 3D / 4TB | WD Green WD40EZRX | 4TB | TBD | SATA 6Gb/s | Apr 2015 — update serial when installed |
| 3 | PATREON #-B | Toshiba DT01ACA300 | 3TB | Y5FM2SEGS | SATA 6Gb/s | Patreon archive #-B — Nov 2015 |
| 4 | PATREON C-D | Toshiba DT01ACA300 | 3TB | Y5GMAEAGS | SATA 6Gb/s | Patreon archive C-D — Nov 2015 |
| 5 | PATREON E-K | Seagate Constellation ES.2 SED ST3000051NS | 3TB | Z2928YTG | SATA 6Gb/s | Patreon archive E-K — enterprise SED, May 2012 |
| 6 | PATREON L-O | Seagate Barracuda ST3000DM001 | 3TB | W1F0BALQ | SATA 6Gb/s | Patreon archive L-O |
| 7 | PATREON O-Z | WD WD30EZRS | 3TB | WD-WMAWZ0009936 | SATA 6Gb/s | Currently in restic-deb bay |
| 8 | TROVE 24-08 | Seagate Enterprise NAS ST6000VN0001 | 6TB | Z401Z7A5 | SATA 6Gb/s | DOM 05/2015 |
| 9 | 6 TB SEAGATE 7200 | Seagate Enterprise NAS ST6000VN0001 | 6TB | Z40Z2HT9 | SATA 6Gb/s | DOM 05/2015 |

### Reserve / Surplus Drives
| # | Label | Model | Capacity | Serial | Interface | Notes |
|---|-------|-------|----------|--------|-----------|-------|
| 1 | Hitachi bare | Hitachi 0F12450 | 3TB | THG3LSNA | SATA 6Gb/s | Dec 2010 — run SMART before trusting |
| 2 | 3TB (unlabeled) | Seagate Constellation ES.2 SED ST3000051NS | 3TB | TBD | SATA 6Gb/s | Enterprise SED — update serial when installed |
| 3 | (unlabeled) | Seagate Constellation ES.2 SED ST3000051NS | 3TB | Z292K11M | SATA 6Gb/s | DOM 05/2012 — enterprise SED |
| 4 | (unlabeled) | Seagate Constellation ES.3 | 3TB | Z1Y38A01 | SATA 6Gb/s | DOM 01/2015 |
| 5 | 2WD CLASS EE | WD Caviar Green WD20EARX | 2TB | WCAZAF839739 | SATA 6Gb/s | Aug 2012 — check for data before use |
| 6 | GOODWIM CENTOS | Seagate Barracuda ST500DM002 | 500GB | TBD | SATA 6Gb/s | Check for data before use |

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
