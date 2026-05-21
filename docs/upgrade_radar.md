# Hardware Upgrade Radar
_Last updated: 2026-05-20_
_Physical hosts only — grouped by board family, least to most capable within each group_

---

## RAM Upgrades

### Intel LGA1155 — Gigabyte Z77-DS3H

| Host | Current RAM | Type | Max RAM | Headroom | Notes |
|------|------------|------|---------|----------|-------|
| restic-deb | 16GB (4×4GB) | DDR3-1600 | 32GB | +16GB | Free upgrade — sticks in reserve |
| truenas | 24GB (2×4GB Hynix + 2×8GB Samsung, mixed) | DDR3-1600 | 32GB | +8GB | Free upgrade — sticks in reserve |

### AMD AM4 — Gigabyte AB350 Family

| Host | Board | Current RAM | Type | Max RAM | Headroom | Notes |
|------|-------|------------|------|---------|----------|-------|
| urnst-deb | AB350-Gaming-CF | 8GB (1×8GB) | DDR4-2133 | 16GB | +8GB (3 slots empty) | Pending stick identification |
| temerant-win | AB350-Gaming | 32GB (4×8GB G.Skill) | DDR4-2133 | 64GB | +32GB | Moving to TrueNAS rebuild |
| idee-deb | AB350-Gaming 3-CF | 16GB (2×8GB G.Skill) | DDR4-2133 | 128GB | +16GB (2 slots empty) | Free upgrade — 2× Samsung 8GB DDR4-2133 from reserve |
| shardik | AB350M Pro4 | 64GB (4×16GB mixed kit) | DDR4-2133 | 64GB | None — maxed | Clocked down for stability — matched pair swap planned |

### Other Physical Hosts

| Host | Board | Current RAM | Type | Max RAM | Headroom | Notes |
|------|-------|------------|------|---------|----------|-------|
| lee-deb | Dell Inspiron 3647 (H81) | Unknown | DDR3 | 16GB | Unknown | Pending setup |
| maturin | Dell OptiPlex 7050 SFF | 32GB (4×8GB, mixed Micron+Samsung) | DDR4-2133 | 64GB | +32GB (swap to 4×16GB) | Memory-pressured — 25GB used |
| amontillado-win | MSI PRO Z690-A WIFI | 128GB (4×32GB) | DDR5-4000 | 128GB | None | Maxed out |

### RAM Priority Flags

!!! danger "High — maturin"
    32GB installed (4×8GB mixed Micron+Samsung) but already at 25GB used with swap touched — memory-pressured now. mediastack-deb alone is allocated 16GB. Swap all four sticks to a matched 4×16GB DDR4-2133 kit (~$40-60 used) to reach the 64GB max.

!!! warning "Medium — shardik"
    64GB installed but a mixed kit of 4 different sticks clocked down to 2133 for stability. Plan: swap to 2× PNY XLR8 16GB DDR4-3200 matched pair (1 in shardik, 1 in reserve) = 32GB running at full speed. Revisit after pulling unknown sticks and physically identifying them — may change the plan. Do during Sunday rebuild if it happens. If PNY pair doesn't resolve instability, fall back to 4× 8GB DDR4-2133 (2× Samsung + 2× Micron from reserve).

!!! tip "Low — truenas"
    Free upgrade available from reserve. Pull 2× Hynix 4GB sticks, replace with 2× Crucial Ballistix 8GB DDR3-1600 + 2× Crucial UDIMM 8GB DDR3-1600 = 32GB. Do before the temerant hardware rebuild. After rebuild, move the 2× Samsung 8GB pulled from truenas to restic-deb.

!!! tip "Low — restic-deb"
    Free upgrade available from reserve. After truenas swap, install 2× Samsung 8GB DDR3-1600 (pulled from truenas) + 2× Timetec 8GB DDR3-1333 = 32GB. Backup server — 16GB is fine for now, no urgency.

!!! tip "Low — idee-deb"
    Free upgrade from reserve — install 2× Samsung 8GB DDR4-2133 in 2 empty slots = 32GB total. GPU upgrade (GTX 1080 Ti from stock) matters more first. Do both at the same time.

!!! tip "Low — urnst-deb"
    Test bench — 8GB adequate for current role. Identify existing stick with dmidecode first, then match from reserve. Max is only 16GB so one stick needed.

!!! info "Skip — amontillado"
    128GB DDR5 — already maxed. No upgrade path on this platform.

!!! info "Skip — temerant-win"
    RAM moving to TrueNAS rebuild. No action needed here.

---

## BIOS Updates

### Intel LGA1155 — Gigabyte Z77-DS3H

| Host | Current BIOS | Latest BIOS | Up to Date? | Notes |
|------|-------------|-------------|-------------|-------|
| restic-deb | F8 (2012-08-20) | F11 | No | 3 versions behind |
| truenas | F9 (2012-09-19) | F11 | No | 2 versions behind — moot after temerant rebuild |

### AMD AM4 — Gigabyte AB350 Family

| Host | Board | Current BIOS | Latest BIOS | Up to Date? | Notes |
|------|-------|-------------|-------------|-------------|-------|
| urnst-deb | AB350-Gaming-CF | TBD — offline | F50d | Unknown | Run dmidecode when online |
| temerant-win | AB350-Gaming | TBD — Windows | F50d | Unknown | Run `wmic bios get smbiosbiosversion` |
| idee-deb | AB350-Gaming 3-CF | TBD — offline | F52 | Unknown | Run dmidecode when online |
| shardik | AB350M Pro4 | P10.43 | P10.43 Beta (Sep 2025) | ✅ Current | No action needed |

### Other Physical Hosts

| Host | Board | Current BIOS | Latest BIOS | Up to Date? | Notes |
|------|-------|-------------|-------------|-------------|-------|
| lee-deb | Dell Inspiron 3647 (H81) | Unknown | Check Dell support | Unknown | Pending setup |
| maturin | Dell OptiPlex 7050 SFF | 1.27.0 (Nov 2023) | 1.27.0 (Nov 2023) | ✅ Current | Flashed 2026-05-20 via USB |
| amontillado-win | MSI PRO Z690-A WIFI | 7D25vAN (Apr 2026) | 7D25vAN (Apr 2026) | ✅ Current | Flashed 2026-05-20 via MSI Center |

### BIOS Priority Flags

!!! success "Done — amontillado-win"
    Flashed to 7D25vAN (Apr 2026) on 2026-05-20. Includes i7-13700K degradation microcode fix, GOP update, and ME firmware 16.1.40.2765.

!!! success "Done — maturin"
    Flashed to 1.27.0 (Nov 2023) on 2026-05-20 via USB. 16 versions of security updates applied.

!!! warning "Medium — Gigabyte AB350 family (urnst-deb / temerant-win / idee-deb)"
    All three boards are likely well behind on BIOS. Required update path — must go through F31 → F40 (with EC FW Update Tool) → latest. Skipping bridge versions will fail. Check current versions first.

    - AB350-Gaming (temerant-win): latest **F50d**
    - AB350-Gaming 3-CF (idee-deb): latest **F52**
    - AB350-Gaming-CF (urnst-deb): latest **F50d**

    To check current version on Linux:
    ```bash
    sudo dmidecode -t 0 | grep -iE "version|release date"
    ```
    On Windows (temerant-win):
    ```cmd
    wmic bios get smbiosbiosversion
    ```

!!! tip "Low — restic-deb / truenas"
    Both Z77-DS3H boards on Sandy Bridge-era BIOS (F8/F9), latest is F11. Stable, no new hardware to unlock. Flash via USB Q-Flash if convenient. truenas is moot after temerant rebuild.

!!! info "Current — shardik"
    Already on P10.43 — latest available as of September 2025. No action needed.

