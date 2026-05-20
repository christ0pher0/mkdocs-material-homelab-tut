# Hardware Upgrade Radar
_Last updated: 2026-05-20_
_Physical hosts only — grouped by board family, least to most capable within each group_

---

## RAM Upgrades

### Intel LGA1155 — Gigabyte Z77-DS3H

| Host | Current RAM | Type | Max RAM | Headroom | Notes |
|------|------------|------|---------|----------|-------|
| restic-deb | 16GB (4×4GB) | DDR3-1600 | 32GB | +16GB | Easy upgrade — DDR3 kits are cheap |
| truenas | 24GB (mixed) | DDR3-1600 | 32GB now → 32GB DDR4 post-rebuild | +8GB now | 32GB DDR4 arriving via temerant rebuild |

### AMD AM4 — Gigabyte AB350 Family

| Host | Board | Current RAM | Type | Max RAM | Headroom | Notes |
|------|-------|------------|------|---------|----------|-------|
| urnst-deb | AB350-Gaming-CF | 8GB (1×8GB) | DDR4-2133 | 16GB | +8GB (3 slots empty) | Test bench — 3 slots sitting empty |
| temerant-win | AB350-Gaming | 32GB (4×8GB) | DDR4-2133 | 64GB | +32GB | Active system — check drives before any changes |
| idee-deb | AB350-Gaming 3-CF | 16GB (2×8GB) | DDR4-2133 | 128GB | +112GB | AI node candidate — GPU upgrade matters more first |
| shardik | AB350M Pro4 | 56GB (16+16+16+8GB) | DDR4-2667 | 64GB | +8GB (replace 8GB Micron) | Mixed kit — instability risk; one stick swap fixes both |

### Other Physical Hosts

| Host | Board | Current RAM | Type | Max RAM | Headroom | Notes |
|------|-------|------------|------|---------|----------|-------|
| lee-deb | Dell Inspiron 3647 (H81) | Unknown | DDR3 | 16GB | Unknown | Pending setup |
| maturin | Dell OptiPlex 7050 SFF | 32GB (4×8GB, mixed Micron+Samsung) | DDR4-2133 | 64GB | +32GB (swap to 4×16GB) | Proxmox node — memory-pressured at 25GB used |
| amontillado-win | MSI PRO Z690-A WIFI | 128GB (4×32GB) | DDR5-4000 | 128GB | None | Maxed out |

### RAM Priority Flags

!!! danger "High — maturin"
    32GB installed (4×8GB mixed Micron+Samsung) but already at 25GB used with swap touched — memory-pressured now. mediastack-deb alone is allocated 16GB. Swap all four sticks to a matched 4×16GB DDR4-2133 kit (~$40-60 used) to reach the 64GB max.

!!! warning "Medium — shardik"
    Running a mixed kit (16+16+16+8GB) — the lone 8GB Micron is the odd one out and the likely contributor to the recent instability. Replace it with a matching 16GB DDR4-2667 stick (~$20-25) to hit 64GB max and eliminate the mismatch. If shardik gets rebuilt Sunday this is the time to do it.

!!! tip "Low — restic-deb"
    Backup server works fine at 16GB. DDR3-1600 4×8GB kits are extremely cheap (~$15-20). Not urgent but an easy win if a kit turns up.

!!! tip "Low — urnst-deb"
    Three DDR4 slots empty. 8GB is adequate for the current test bench role. If promoted to Proxmox node 3, add 3×4GB DDR4 to reach 16GB max — slots are right there.

!!! tip "Low — idee-deb"
    AI node candidate but GPU comes first. Once a GTX 1080 Ti is installed, RAM becomes the next lever. The board supports up to 128GB DDR4 which is unusually high for a B350 platform.

!!! info "Skip — truenas"
    32GB DDR4 arriving as part of the temerant hardware donor rebuild. No action needed before that.

!!! info "Skip — amontillado"
    128GB DDR5 — already maxed. No upgrade path on this platform.

---

## BIOS Updates

### Intel LGA1155 — Gigabyte Z77-DS3H

| Host | Current BIOS | Latest BIOS | Up to Date? | Notes |
|------|-------------|-------------|-------------|-------|
| restic-deb | F8 (2012-08-20) | F11 | No | 3 versions behind |
| truenas | F9 (2012-09-19) | F11 | No | 2 versions behind |

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
| maturin | Dell OptiPlex 7050 SFF | 1.11.0 (2018) | 1.27.0 (Sep 2023) | No | 16 versions behind |
| amontillado-win | MSI PRO Z690-A WIFI | A.F0 (Nov 2023) | 7D25vAN (Apr 2026) | No | **Critical** — i7-13700K degradation microcode + GOP/ME updates |

### BIOS Priority Flags

!!! danger "Critical — amontillado-win"
    Running BIOS A.F0 from November 2023 on an i7-13700K. Latest MSI BIOS (7D25vAN, Apr 2026) includes microcode updates addressing the 13th gen Intel processor voltage and degradation issue, plus GOP update and ME firmware 16.1.40.2765. Without the updated microcode, the CPU may be running elevated voltages during idle and accelerating wear. Flash from Windows via MSI Center or USB boot.

    **Download:** [MSI PRO Z690-A WIFI support page](https://www.msi.com/Motherboard/PRO-Z690-A/support)

!!! warning "High — maturin"
    Dell OptiPlex 7050 SFF on BIOS 1.11.0 from 2018 — 16 versions behind current (1.27.0). Straightforward Dell USB flash (F12 at boot → BIOS Flash Update). Includes multiple security advisories.

    **Download:** [Dell OptiPlex 7050 BIOS support page](https://www.dell.com/support/product-details/en-us/product/optiplex-7050-sff/drivers)

!!! warning "Medium — Gigabyte AB350 family (urnst-deb / temerant-win / idee-deb)"
    All three boards are running first-gen AGESA and likely well behind on BIOS. The AB350-Gaming and AB350-Gaming 3 have a required update path — must go through F31 → F40 (with EC FW Update Tool) → latest. Skipping bridge versions will fail. Check current versions first, then plan accordingly.

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
    Both Z77-DS3H boards are on old Sandy Bridge-era BIOS (F8 and F9 respectively), latest is F11. Systems are stable and the CPUs are fully supported — no new hardware to unlock. Flash via USB Q-Flash if convenient, but not urgent.

!!! info "Current — shardik"
    Already on P10.43 — latest available as of September 2025. No action needed.

