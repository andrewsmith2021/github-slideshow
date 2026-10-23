---
layout: slide
date: 2000-01-08 11:30:00
title: "VMware to VM Essentials: What Changes"
---

| VMware feature | Under VM Essentials | Status |
|---|---|---|
| **vMotion / HA** | Live migration and clustering-based HA | ✅ Covered |
| **DRS** (workload balancing) | Listed by HPE; maturity unclear | ⚠️ Confirm |
| **Fault Tolerance** | No confirmed equivalent | ❌ Likely gap |
| **NSX** (microsegmentation, distributed firewall) | Open vSwitch basic switching | ❌ Gap |
| **vSAN** | External shared storage (e.g., HPE Alletra) | ❌ Gap |
| **Aria** (ops, automation) | Morpheus Enterprise + OpsRamp | 🔄 Replaced |
| **Site Recovery Manager** | Zerto | 🔄 Replaced |
| **Tanzu** (Kubernetes) | Morpheus orchestrates standard Kubernetes | 🔄 Different |
| **vGPU, scale limits, Horizon VDI** | Confirm support; VDI is separate | ⚠️ Confirm |

<small>Few current public comparisons exist; treat as a checklist to confirm with HPE.</small>
