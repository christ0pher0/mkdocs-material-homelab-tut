# Hardware Reserve
_Last updated: 2026-06-29_
_Spare and undeployed hardware available for upgrades and new builds_
_Inventory in progress — updated as items are found_
---
## Graphics Cards
| Item | Qty | VRAM | Notes |
|------|-----|------|-------|
| NVIDIA GeForce GTX 1080 | 4 | 8GB | Pascal NVENC — 1 transcode stream, no AV1. Undeployed. |
| NVIDIA GeForce GTX 1080 Ti | 2-3 | 11GB | Best choice for AI/Ollama — more VRAM than 1080. 1x in amontillado, 1x earmarked for TrueNAS rebuild. |
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
| SK Hynix 4GB HMA851U6AFR6N | 4 | DDR4-2400 | Low capacity — limited use cases. Untested. |
| G.Skill Trident Z RGB 8GB F4-3200C16 | 2 | DDR4-3200 | ✅ memtest clean 2026-06-29 — known good spares |
| Crucial 8GB CT8G4DFS824A | 3 | DDR4-2400 | Untested |
| Crucial 8GB CT8G40FD8213 | 2 | DDR4-2133 | Untested |
| HyperX Fury 8GB DDR4-2666 | 1 | DDR4-2666 | Found in ASRock B450M red case 2026-06-29 — untested |
| Micron 8GB MTA16ATF1G64AZ | 1 | DDR4-2133 | Untested |
| Mushkin Essentials 8GB | 1 | DDR4-2133 | Untested |
| Samsung 8GB M378A1G43 | 1 | DDR4-2133 | Untested |
| Team Group RockSoul 8GB TED48G2400C16BK | 1 | DDR4-2400 | Untested |
| DDR4-2133 sticks (various) | ~8 | DDR4-2133 | Not yet individually catalogued — 13 total DDR4-2133 known in reserve, 5 above + ~8 uncatalogued |
_Deployed 2026-06-29: Ballistix by Micron 16GB BLS16G4D26BFST → shardik; Micron 8GB MTA8ATF1G64AZ (3x) → shardik. Total: 40GB DDR4-2666 in shardik._
_Deployed 2026-06-29: GeIL 8GB GN48GB2400C16S (2x) + ADATA XPG 8GB AX4U240038G16-BRZ (2x) → ASRock B450M Steel Legend (mystery machine / red case) — untested, 32GB total_
_Deployed 2026-06: Micron 8GB MTA16ATF1G64AZ (2x) → urnst-deb; Samsung 8GB M378A1G43DB0 (2x) → idee-deb_
_Disposed 2026-06-29: PNY XLR8 16GB 16GF2X16QFHH36 (2x) — failed memtest and stress-ng, pulled from shardik, dead_
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
| Timetec 8GB 75TT13NU2R8-8G | 2 | DDR3-1333 | Desktop — deployed to restic-deb 2026-06 |
_Deployed 2026-06: Crucial Ballistix Sport 8GB (2x) + Crucial UDIMM 8GB (2x) → truenas (now 32GB); Samsung 8GB (2x, pulled from truenas) + Timetec 8GB (2x) → restic-deb (now 32GB)_
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
!!! note "Drive Policy"
    No HDDs under 3TB in any active role. Sub-3TB drives are disposal/ewaste candidates after data check.

### Production / Rotation Drives
| # | Label | Model | Capacity | Serial | Interface | Last Backed Up | Notes |
|---|-------|-------|----------|--------|-----------|----------------|-------|
| 1 | 3D / 4TB | WD Green WD40EZRX | 4TB | TBD | SATA 6Gb/s | Aug 2022 | Diff against TrueNAS before retiring — update serial |
| 2 | 4TB KICKSTARTER | WD/HGST HC310 HUS726T4ALE6L4 | 4TB | V6KAG1VR | SATA 6Gb/s | Jan 2024 | Dec 2019 |
| 3 | STL #-B | Toshiba DT01ACA300 | 3TB | Y5FM2SEGS | SATA 6Gb/s | Jan 2024 | STL archive #-B (formerly PATREON) |
| 4 | STL C-D | Toshiba DT01ACA300 | 3TB | Y5GMAEAGS | SATA 6Gb/s | Feb 2025 | STL archive C-D (formerly PATREON) |
| 5 | STL E-H | Seagate Constellation ES.2 SED ST3000051NS | 3TB | Z2928YTG | SATA 6Gb/s | 2026-06 | STL archive E-H (formerly PATREON E-K, split) |
| 6 | STL I-K | TBD | 3TB | TBD | SATA 6Gb/s | In progress | STL archive I-K — new drive, currently being written |
| 7 | STL L-O | TBD | 3TB | TBD | SATA 6Gb/s | Pending | STL archive L-O — not yet started |
| 8 | STL O-S | WD WD30EZRS | 3TB | WD-WMAWZ0009936 | SATA 6Gb/s | May 2026 | STL archive O-S (formerly PATREON O-S) |
| 9 | TROVE 24-08 | Seagate Enterprise NAS ST6000VN0001 | 6TB | Z401Z7A5 | SATA 6Gb/s | Aug 2024 | DOM 05/2015 |
| 10 | 6 TB SEAGATE 7200 | Seagate Enterprise NAS ST6000VN0001 | 6TB | Z40Z2HT9 | SATA 6Gb/s | — | DOM 05/2015 |
| 11 | READING | Seagate Constellation ES.3 ST3000NM0033 | 3TB | Z1Y32KTB | SATA 6Gb/s | Feb 2025 | DOM 01/2015 |
| 12 | AUDIOBOOKS 3TB | WD Caviar Green WD30EZRS | 3TB | WMAW20629019 | SATA 6Gb/s | Feb 2024 | Nov 2014 |
| 13 | MUSIC+ MUSIC NOT PLEX | Toshiba DT01ACA300 | 3TB | Y5GM81UGS | SATA 6Gb/s | Feb 2024 | Nov 2015 |
| 14 | TROVE BOOKS | Toshiba DT01ACA300 | 3TB | Y5GM22NGS | SATA 6Gb/s | Feb 2024 | Nov 2015 |
| 15 | PLEX ETC | Toshiba DT01ACA300 | 3TB | Y5GM755GS | SATA 6Gb/s | Feb 2024 | Nov 2015 |
| 16 | 3TB TV SONS-T | Hitachi 0F12450 | 3TB | YHG4ZPSA | SATA 6Gb/s | 2026-06 | TV archive S — ✅ rotation complete |
| 17 | 3T TVU-Z | Hitachi 3TB | 3TB | YHG80M8A | SATA 6Gb/s | 2026-06 | TV archive U-Z — ✅ rotation complete |
| 18 | 3T HIT EVERYTHING | Seagate Enterprise NAS ST3000VN0001 | 3TB | Z4F95VN8 | SATA 6Gb/s | 2026-06 | TV archive misc — ✅ rotation complete |
| 19 | 3TB TV M-O | Seagate Barracuda ST3000DM001 | 3TB | Z1FKZ6JM | SATA 6Gb/s | 2026-06 | TV archive M-O — ✅ rotation complete |
| 20 | 3TB TV K-L | WD Caviar Green WD30EZRS | 3TB | WMAWZ0J24370 | SATA 6Gb/s | 2026-06 | TV archive K-L — ✅ rotation complete |
| 21 | 3TB TV P-SNOFALL | Seagate Constellation ES.2 SED ST3000051NS | 3TB | Z292M282 | SATA 6Gb/s | 2026-06 | TV archive P-Snowfall — ✅ rotation complete |
| 22 | 3TB SEA TV C-D | Seagate Constellation ES.2 SED ST3000051NS | 3TB | Z2926W97 | SATA 6Gb/s | 2026-06 | TV archive C-D — ✅ rotation complete |
| 23 | 3TB TV E-F GOT | WD Caviar Green WD30EZRS | 3TB | WMAWZ0028623 | SATA 6Gb/s | 2026-06 | TV archive E-F incl GOT — ✅ rotation complete |
| 24 | 3TB TV G-J | WD Caviar Green WD30EZRS | 3TB | WMAWZ036055 | SATA 6Gb/s | 2026-06 | TV archive G-J — ✅ rotation complete |
| 25 | D&D GAMING | Seagate Desktop HDD ST3000DM001 | 3TB | Z5011ZMP | SATA 6Gb/s | Feb 2024 | D&D/Gaming archive |
| 26 | MUSIC 10-21-2018 | Seagate Desktop HDD ST3000DM001 | 3TB | Z5011NMK | SATA 6Gb/s | Feb 2024 | Music archive |
| 27 | TV 0-B / 4TB WDGREEN | WD Green WD40EZRX | 4TB | HARNNY2C48 | SATA 6Gb/s | 2026-06 | TV archive 0-B — ✅ rotation complete |
| 28 | 3WD MOVIES R-Z | Seagate Desktop HDD ST3000DM001 | 3TB | Z50102NP | SATA 6Gb/s | 2026-06 | Movie archive R-Z — ✅ rotation complete |
| 29 | MOVIES H-Q | Seagate | 3TB | B31412046N | SATA 6Gb/s | 2026-06 | Movie archive H-Q — ✅ rotation complete |
| 30 | 3TBSEA MOVIES O-G | Hitachi 0F12450 | 3TB | YHG777BNA | SATA 6Gb/s | 2026-06 | Movie archive O-G — ✅ rotation complete |

### Reserve / Surplus Drives
| # | Label | Model | Capacity | Serial | Interface | Notes |
|---|-------|-------|----------|--------|-----------|-------|
| 1 | Hitachi bare | Hitachi 0F12450 | 3TB | THG3LSNA | SATA 6Gb/s | Dec 2010 — run SMART before trusting |
| 2 | 3TB (unlabeled) | Seagate Constellation ES.2 SED ST3000051NS | 3TB | TBD | SATA 6Gb/s | Enterprise SED — update serial when installed |
| 3 | (unlabeled) | Seagate Constellation ES.2 SED ST3000051NS | 3TB | Z292K11M | SATA 6Gb/s | DOM 05/2012 — enterprise SED |
| 4 | (unlabeled) | Seagate Constellation ES.3 | 3TB | Z1Y38A01 | SATA 6Gb/s | DOM 01/2015 |
| 5 | (unlabeled) | Seagate Constellation ES.2 SED ST3000051N0 | 3TB | Z2923YYH | SATA 6Gb/s | DOM 05/2012 — enterprise SED |
| 6 | (unlabeled) | Unknown | 12TB | TBD | SATA 6Gb/s | Found in reserve — run SMART before use |
| 7 | (unlabeled) | Unknown | 20TB (suspect) | TBD | SATA 6Gb/s | Found in reserve — condition unknown, run full SMART test before trusting |

### Needs Data Check Before Disposal
| # | Label | Notes |
|---|-------|-------|
| 1 | 2WD CLASS EE | WD 2TB — unknown contents, sub-3TB policy: dispose after check |
| 2 | GOODWIM CENTOS | Seagate 500GB — P2V CentOS to Proxmox VM first, then dispose |

### External HDDs
| Label | Capacity | Notes |
|-------|----------|-------|
| WD My Passport (black) | 1TB | USB 3.0 portable |
| WD My Passport (red) | 1TB | USB 3.0 portable |
