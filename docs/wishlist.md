# Hardware Wishlist & Ewaste Hunt
_Last updated: 2026-05-24_

Ordered by priority. "Buy" = needs purchasing. "Hunt" = ewaste/opportunistic find.

---

## 🔴 Critical — Buy Now

| Item | Est. Cost | Use Case | Notes |
|---|---|---|---|
| LSI 9211-8i or HP H220 9205-8i HBA | ~$19-40 | TrueNAS rebuild — SAS drive support | HP H220 seen at $19.49 (China, free ship). Already in IT mode. Order early — China shipping 2-4 weeks. |
| 2x SFF-8087 to SATA breakout cables | ~$5-10 each | TrueNAS HBA → data drives | Required with HBA above. |
| ~~20TB CMR drive (ada4 replacement)~~ | ~~$399.99~~ | ~~TRYAGAIN pool resilver~~ | **ORDERED 2026-05-24** — WD Ultrastar WUH722020BLE6L4, easttechdeals eBay |

---

## 🟡 Medium Priority — Buy or Hunt

| Item | Est. Cost | Action | Use Case | Notes |
|---|---|---|---|---|
| AMD Ryzen 7 2700X | ~$30-50 | Buy/Hunt | shardik CPU upgrade | Drop-in AM4 upgrade — 8c/16t vs current 6c/12t. ASRock AB350M Pro4 BIOS P10.43 supports it natively. Best bang for buck upgrade available. |
| PNY XLR8 16GB DDR4-3200 | ~$25-35 | Buy | shardik RAM — reach 64GB | **1x already in reserve** — need 1 more matching stick to replace the lone 8GB DIMM. |
| CRU drive tray/sleeve (3rd bay) | ~$10 | Buy | restic-deb hot-swap bay 3 | Need matching tray to use 3rd CRU bay |

---

## 🟢 Ewaste Hunt — Opportunistic Only

| Item | Target Price | Use Case | Notes |
|---|---|---|---|
| Any AM4 Ryzen 5 2600/3600 | <$25 | urnst-deb or idee-deb CPU bump | Both have 1600X already — only worth it at rock-bottom price |
| DDR4-2133 8GB UDIMM sticks | <$8 each | urnst-deb RAM fill | Need 3x to reach 32GB. **Already have 2x Micron 8GB DDR4-2133 in reserve** — need 1 more matching stick |
| AMD Ryzen 3 2200G | <$25 | iGPU build only | Vega 8 iGPU useful for headless-free builds. **Not an upgrade for existing 1600X machines.** Skip at $40. |
| NVMe SSD 500GB+ | <$25 | General VM storage | Always useful — check reserve first (SK Hynix PC600 512GB and Crucial P1 500GB already in stock) |
| GTX 1080 (additional) | <$50 | GPU node expansion | Already have 4x undeployed — only buy if deploying a new node |

---

## 📦 Already In Reserve — Don't Buy

These are covered by existing hardware reserve stock:

| Need | Already Have |
|---|---|
| TrueNAS RAM upgrade | ✅ Done 2026-05-24 — Crucial Ballistix + UDIMM installed |
| restic-deb RAM upgrade | ✅ Done 2026-05-24 — Samsung 8GB (from TrueNAS) + Timetec installed |
| idee-deb RAM (2 empty slots) | ✅ 2x Samsung 8GB DDR4-2133 in reserve — free upgrade |
| urnst-deb RAM (3 empty slots) | ✅ 2x Micron 8GB DDR4-2133 in reserve — need 1 more |
| shardik second 16GB DDR4-3200 | 1x PNY XLR8 16GB in reserve — need matching second stick |
| NVMe drives | Multiple in reserve — SK Hynix PC600 512GB, Crucial P1 500GB, Orico 2TB NVMe (new in box) |
| Backup/portable storage | 2x WD My Passport 1TB in reserve |

---

## 💀 Drive Health Alerts

| Drive | Label | Serial | Status | Notes |
|---|---|---|---|---|
| WD WD30EZRS | 3TB TV K-L | WMAWZ0J24370 | ⚠️ SUSPECTED DEAD | Shows 0.0GB in BIOS — 2026-05-24. Last backed up Sep 2022. May need PhotoRec attempt. |
| OOS20000G | ada4 (TRYAGAIN) | 00013AJR | ⚠️ FAULTED | 57 read errors — replacement ordered |

---

## 📝 Notes

- **Ewaste sources:** local thrift, FB Marketplace, eBay lots, server decommissions
- **AM4 CPU compatibility:** All AB350/B350 boards need BIOS update for Ryzen 2000/3000 — verify before buying
- **HBA cables:** SFF-8087 (4-port) → SATA breakout. Need 2x cables for 8 ports total on 9211-8i
- **restic-deb backup drive strategy:** Drives are too fragmented by letter range — plan full reorganization starting from 0-9, A-B, C-D etc. to fill drives completely before moving to next
