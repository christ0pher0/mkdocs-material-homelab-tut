# DIGIDIOT — Scavenge / Shop List
_Hardware to acquire. Check dc_salvage.md before buying anything._
_Last updated: 2026-07-01_

---

## Priority 1 — Blocking Projects

| Item | Purpose | Source | Est. Cost | Status |
|---|---|---|---|---|
| LSI 9211-8i or IBM M1015 IT mode HBA | TrueNAS rebuild — SATA passthrough | eBay | $15-35 | 🔴 Blocking TrueNAS rebuild |
| 2x SFF-8087 to SATA breakout cables | TrueNAS HBA cabling | eBay | $5-10 each | 🔴 Blocking TrueNAS rebuild |
| Dell managed switch (802.1Q VLAN) | VLAN project | DC1 salvage (Cisco SG200-50 in hand) | $0 | 🟡 Retrieve from DC1 |

---

## Priority 2 — RAM Upgrades

⚠️ **Consumer DDR4 UDIMM non-ECC only.** Server RDIMM/ECC from DC1 will NOT work in AM4 boards.

| Item | For | Qty | Source | Est. Cost | Status |
|---|---|---|---|---|---|
| 16GB DDR4-2666/3200 UDIMM non-ECC | shardik (replace 3x8GB → 64GB) | 3 | DC1 Lambda workstations / eBay | $20-25/ea | 🟡 Check DC salvage first |
| 16GB DDR4-2400+ UDIMM non-ECC | aslan (replace 2x8GB → 64GB) | 2 | DC1 Lambda workstations / eBay | $20-25/ea | 🟡 Check DC salvage first |
| **RAM swap (no purchase)** | maturin 2x16GB SK Hynix → aslan | — | Internal shuffle | $0 | 🟡 Pending Sunday downtime |

---

## Priority 3 — Networking

| Item | Purpose | Source | Est. Cost | Status |
|---|---|---|---|---|
| Cisco SG200-50 (48-port) | VLAN switch | DC1 salvage — in hand | $0 | 🟡 Retrieve |
| Dell N4032F x2 (32-port 10GbE SFP+) | Cluster networking upgrade | DC1 — authorization pending | $0 if authorized | 🟡 Awaiting auth |
| Hologram.io SIM | argos-deb LTE field station | hologram.io | ~$10/mo | 🔴 Purchase when argos online |

---

## Priority 4 — Storage

| Item | Purpose | Source | Est. Cost | Status |
|---|---|---|---|---|
| Dell JBOD (4TB SAS drives) | TrueNAS pool expansion | DC1 — on the fence | $0 if authorized | 🟡 Confirm chassis/bay count first |
| Dell SAS 12G HBA (external SFF-8644) | Pairs with JBOD | DC1 — on the fence | $0 if authorized | 🟡 Value depends on JBOD |
| 3TB+ HDDs (no drives under 3TB policy) | CRU archive expansion | eBay / DC salvage | ~$40-60 | 🟡 As needed |

---

## Priority 5 — Infrastructure

| Item | Purpose | Source | Est. Cost | Status |
|---|---|---|---|---|
| Dell PowerEdge R730 | Additional compute / parts | DC1 — authorized | $0 | 🟡 Get CPU/RAM specs on pickup |
| CoolerMaster tower (Quadro M4000 + 2TB NVMe + Corsair AIO) | GPU workstation or parts | DC1 — authorized | $0 | 🟡 Take whole system |
| 12U half rack | Rack enclosure | DC1 — authorized | $0 | 🟡 Retrieve |
| 1U Supermicro x2 (10G onboard) | Additional compute | DC1 — authorized | $0 | 🟡 Grab both |
| Advidia cameras (A-46-FW, B-5360) + PoE domes | Frigate NVR | DC1 — authorized | $0 | 🟡 Retrieve |
| Environmental monitor (Watchdog) | Taylor — rack monitoring | DC1 — authorized | $0 | 🟡 Retrieve |

---

## Authorization Pending — DC1

| Item | Notes |
|---|---|
| Dell N4032F x2 | 32-port 10GbE SFP+ L3 — transforms cluster networking |
| Lambda GPU workstations x4 (1 possible) | GPU model unknown — check on visit |
| Dell Precision 7920 | High-end workstation |

---

## Remaining DCs — Hold Until Surveyed

DC2, DC3, DC4 not yet walked. Hold on borderline items until complete.

---

## Purchased / In Hand

| Item | Location | Notes |
|---|---|---|
| 4x 8-port PoE switches | In hand | From DC1 |
| Cisco SG200-50 | In hand | VLAN switch — retrieve from DC1 storage |
| APC 12U half rack | In hand | Awaiting rack build |
| Netgate SG-1100 | In hand | pfSense router for VLAN project |
