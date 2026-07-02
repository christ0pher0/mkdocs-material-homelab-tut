# DC Decommission Salvage Tracker
_2-3 DCs going down. Last updated: 2026-07-02. DC2 survey in progress._

---

## SWITCHES

| Item | Status | Notes |
|---|---|---|
| Dell N4032F | 🔥 **Need authorization** | x2 available, 32-port 10GbE SFP+ L3, transforms Proxmox cluster |
| Dell PowerConnect 6224 | ✅ High priority | L3, VLAN-ready, 4x 10G uplinks — fallback if N4032F denied |
| Cisco SG200-50 | ✅ **Confirmed grab** | 50-port GbE managed, VLAN capable |
| HPE OfficeConnect 1820 J9980A | 👍 Nice to have | x2, fanless, VLAN support |
| Netgear 10G-SW | ❓ Investigate | Partial label — need full model |
| PoE switches (8-port, x4) | ✅ **Have them** | Camera deployment sorted. |

---

## CAMERAS

| Item | Status | Notes |
|---|---|---|
| Advidia A-46-FW | ✅ **Grab** | 1080p, H.265, IP67, IR 30m, PoE, Frigate-compatible |
| Advidia B-5360 Mini 360 Dome | ✅ **Grab** | 360° panoramic PoE |
| Loose PoE domes (~4 units) | ✅ Grab if Advidia | Confirm make first |

_Future project: Frigate VM on Proxmox (Drew)._

---

## HBAs / CONTROLLERS

| Item | Status | Notes |
|---|---|---|
| Dell SAS 12G HBA | 🤔 On the fence | External SFF-8644, IT mode. Value depends on JBOD availability. |

---

## SERVERS

| # | Item | Status | Notes |
|---|---|---|---|
| 1 | **Dell PowerEdge R730** | ✅ **Authorized** | Best server here. Dual E5-2600 v3/v4, 24 DIMMs, iDRAC. Specs TBD. |
| 2 | **Lambda GPU Workstation** | 🔥 **Auth pending** | x4 available, 1 possible. GPU unknown — investigate. Pull any 32GB DDR4 UDIMM sticks found. |
| 3 | **Dell Precision 7920** | ❓ Auth needed | Dual Xeon Scalable, massive PCIe, modern platform. |
| 4 | **CoolerMaster Tower (ASUS/Corsair AIO)** | ✅ **Take the whole thing** | M4000 8GB GDDR5 + 2TB NVMe boot drive + Corsair AIO liquid cooling. Don't just pull the GPU — grab the system. |
| 5 | **Dell PowerEdge R720** | ❓ Auth needed | Dual Xeon E5-2600 v1/v2, solid Proxmox node. |
| 6 | **Supermicro Tower (Xeon)** | ❓ Auth needed | Hot-swap bays, potential TrueNAS chassis. |
| 7 | **Environmental Monitor (Watchdog)** | ✅ Grab | DC temp/humidity. Taylor wants it. |
| 8 | **1U Supermicro (x2, "G4G +10G")** | ✅ **Grab both** | x2 units. Onboard 10G NIC is the sell. Low RAM but expandable. Dedicated service hosts or lightweight VM nodes. |
| 9 | **Lenovo ThinkStation (Xeon, x2)** | 👍 Nice to have | Confirmed Xeon. Already have one as pve3. Parts or spare node. |
| 10 | **Dell OptiPlex 7050 + 7040** | 👍 Nice to have | 6th/7th gen Core. Low power service hosts. |
| 11 | **Dell Precision T1650** | 👍 Low priority | Older workstation. Parts or light VM host. |
| 12 | **Dell PowerEdge R750** | 🔥 **Investigate** | Modern Ice Lake Xeon Scalable. Specs unknown — pull CPU/RAM/drive/PCIe details. High potential. Found 2026-07-02. |
| 13 | **Dell PowerEdge R420 (x2)** | 👍 Low priority | Sandy Bridge Xeon E5-2400, DDR3 ECC RDIMM. Older and loud. RAM not compatible with homelab nodes. |
| 14 | **Dell PowerEdge R620** | 👍 Low priority | Sandy Bridge/Ivy Bridge Xeon E5-2600, DDR3 ECC RDIMM. Same caveats as R420. |
| 15 | **Dell M1000e Blade Chassis** | ❌ Pass | 10U, 6kW+, proprietary fabric. Too power-hungry for homelab. Blades can't run without chassis. |
| — | **Dell M620/M630 Blades** | 💰 Resale | Pull service tag + model. M630 DDR4 RDIMMs + E5-2600 v3/v4 CPUs have eBay value. Check 2.5" drives in each blade. |
| — | **Dell XPS 630i (Red)** | ❤️ Sentimental | Core 2 era. Technically e-waste. Spiritually irreplaceable. |

---

## INFRASTRUCTURE

| Item | Status | Notes |
|---|---|---|
| **12U Half Rack** | ✅ **Grab** | Free enclosure for all this new hardware. No-brainer. |
| **DLI IP Power Switches (x2)** | ✅ **KEEP** | Digital Loggers network-managed PDUs. Remote power cycling, outlet monitoring, HA integration. Get model numbers. Found 2026-07-02. |

## RAM FINDS (2026-07-02)

| Item | Qty | Status | Notes |
|---|---|---|---|
| **Crucial CT32G4DFD832A** 32GB DDR4-3200 UDIMM | 2 (so far) | ✅ **Holy grail** | Exact spec for shardik/aslan 128GB grail. 2 more machines to check. |
| **Samsung M378A2K43CB1-CTD** 16GB DDR4-2666 UDIMM | 10 | ✅ **Keep** | 4→maturin (maxes at 64GB), 4→shardik (interim 64GB), 2 spare. |
| **SK Hynix HMCG88MEBRA115N** 32GB DDR5 ECC RDIMM (Supermicro) | 8 | 💰 **Sell** | No current platform. DDR5 RDIMM server-grade. eBay value. |
| **OWC OWC2933D4MP32GB** 32GB DDR4-2933 RDIMM (Mac Pro) | 2 | — | Already in pve3. RDIMM — not compatible with AM4 nodes. |

## AV / PERIPHERALS

| Item | Status | Notes |
|---|---|---|
| **Polycom conference phone** | 💰 Resale | Get model number. List on eBay/Marketplace. ~$20-80. |
| **Polycom satellite speakers** | 💰 Resale | Pairs with matching base unit. Get model, bundle if possible. |
| **Polycom EaglEye cameras** | 💰 Resale (maybe) | Proprietary snap connector — only works with Polycom codecs. Get model number first. May be worth more as a bundle with the phone. |

---

## STORAGE

| # | Item | Status | Notes |
|---|---|---|---|
| 1 | **Dell JBOD (4TB SAS drives)** | ❓ **Pursue** | Chassis/bay count TBD. Pairs with SAS 12G HBA → TrueNAS. |
| 2 | **Synology RS810RP+** | ❌ Pass | 4-bay 1U, redundant PSU. Atom D510, DSM EOL. Too old to be useful. Donate/scrap. |
| 3 | **Dell PowerVault MD1200** | ✅ **KEEP** | 12-bay 2U SAS shelf. No compute — pure disk expansion. Pairs with SAS HBA → TrueNAS. Found 2026-07-02. Retrieve with other DC hardware. |
| 4 | **Hitachi AMS2100** | ❌ Pass | Enterprise SAN, ~15x Seagate Cheetah 15K SAS drives. Proprietary FC controllers. Drives too old/small/loud. Alex to sign off before disposal. |

---

## NEEDS MORE INFO

Work through this on your next visit.

- [ ] **Dell JBOD (4TB SAS)** — chassis model? bay count? available?
- [ ] **Large orange-tab array** — make/model? drives? available?
- [ ] **Lambda GPU workstation** — GPU model? authorization status?
- [ ] **Netgear 10G-SW** — full model number? available?
- [ ] **Dell N4032F x2** — authorization status?
- [ ] **Synology RS810+** — drives installed? sizes?
- [ ] **Dell R730** — CPU model? RAM?
- [ ] **Dell Precision 7920** — authorization? specs?
- [ ] **1U Supermicro x2** — CPU? max RAM? 10G chipset? available?
- [ ] **Loose PoE cameras** — confirmed Advidia?
- [ ] **Dell SAS 12G HBA** — grab or leave?

---

## WATCH LIST — look for these in remaining rooms

- **10GbE NICs** — Intel X520/X540, Mellanox ConnectX-2/3. Riley needs these.
- **IT mode HBAs** — LSI 9211-8i, Dell H200, Dell H310. Alex needs one for TrueNAS.
- **ECC DDR4 server RAM** — especially if R730 is light on RAM.
- **NVMe or SATA SSDs** — always useful for VM boot drives.
- **DAC cables / SFP+ modules** — if N4032F is authorized, need these.
- **PoE switch** — ✅ Covered. 4x 8-port PoE switches in hand.
- **Working UPS** — Eaton is dead. Any replacement welcome.
- **GPU cards** — RTX, A-series Quadro, Tesla. Casey/ML use.
- **KVM switch** — lab management.
- **PDUs** — rack power distribution.

---

## DC STATUS

| DC | Status | Notes |
|---|---|---|
| DC 1 | ✅ **Fully inventoried** | Largest source. All rooms surveyed 2026-06-30. Authorization pending on key items. |
| DC 2 | 🔄 Coming down | Inventory unknown. Schedule walkthrough. |
| DC 3 | ❓ Possible | TBD — confirm status. |
| DC 4 | 🆕 Added | TBD — confirm status. |

_Hold on borderline items until DC 2-4 inventory complete. More hardware likely to surface._
