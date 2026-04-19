Production Planning Engine

This document consolidates the complete JSON dataset, planning parameters, poolstock strategy, line mappings, outbound deliveries, cycle times, changeover matrices, and the full Python scheduling engine.

1. Parameters

{
  "batch_size_target": 500,
  "batch_size_min": 300,
  "batch_size_max": 800,

  "changeover_target_per_day": 4,
  "tpa_safety_window_minutes": 45,

  "line_opening_hours": {
    "L1": ["06:00-14:00", "14:00-22:00"],
    "L2": ["06:00-14:00", "14:00-22:00"],
    "L3": ["06:00-14:00", "14:00-22:00"],
    "L4": ["06:00-18:00"],
    "L5": ["06:00-18:00"],
    "L6": ["06:00-18:00"],
    "L7": ["06:00-18:00"]
  }
}

2. Poolstock Strategy (Hybrid)

{
  "R1":  { "strategy": "TPA_strict", "min": 0, "max": 200 },
  "R2":  { "strategy": "coverage", "min": 100, "max": 400 },
  "R3":  { "strategy": "opportunistic", "min": 0, "max": 300 },
  "R4":  { "strategy": "batch_driven", "min": 0, "max": 500 },
  "R5":  { "strategy": "coverage", "min": 150, "max": 500 },
  "R6":  { "strategy": "opportunistic", "min": 0, "max": 300 },
  "R7":  { "strategy": "batch_driven", "min": 0, "max": 600 },
  "R8":  { "strategy": "coverage", "min": 100, "max": 400 },

  "R9":  { "strategy": "TPA_strict", "min": 0, "max": 100 },
  "R10": { "strategy": "coverage", "min": 50, "max": 200 },
  "R11": { "strategy": "opportunistic", "min": 0, "max": 200 },
  "R12": { "strategy": "batch_driven", "min": 0, "max": 400 },
  "R13": { "strategy": "coverage", "min": 100, "max": 300 },
  "R14": { "strategy": "opportunistic", "min": 0, "max": 200 }
}

3. Families, Lines, and Reference Mapping

{
  "family1": {
    "lines": ["L1", "L2", "L3"],
    "references": {
      "R1": ["L1", "L2"],
      "R2": ["L1", "L3"],
      "R3": ["L2", "L3"],
      "R4": ["L1", "L2"],
      "R5": ["L2", "L3"],
      "R6": ["L1", "L3"],
      "R7": ["L1", "L2"],
      "R8": ["L2", "L3"]
    }
  },
  "family2": {
    "lines": ["L4", "L5", "L6", "L7"],
    "references": {
      "R9": ["L4"],
      "R10": ["L5"],
      "R11": ["L6"],
      "R12": ["L7"],
      "R13": ["L4"],
      "R14": ["L6"]
    }
  }
}

4. Outbound Deliveries (Next 2 Days)

[
  {
    "delivery_id": "D001",
    "product": "R1",
    "quantity": 420,
    "planned_picking_time": "2026-04-20T08:00:00",
    "truck_departure": "2026-04-20T09:00:00"
  },
  {
    "delivery_id": "D002",
    "product": "R5",
    "quantity": 600,
    "planned_picking_time": "2026-04-20T14:00:00",
    "truck_departure": "2026-04-20T15:00:00"
  },
  {
    "delivery_id": "D003",
    "product": "R10",
    "quantity": 300,
    "planned_picking_time": "2026-04-21T07:30:00",
    "truck_departure": "2026-04-21T08:00:00"
  },
  {
    "delivery_id": "D004",
    "product": "R12",
    "quantity": 500,
    "planned_picking_time": "2026-04-21T16:00:00",
    "truck_departure": "2026-04-21T17:00:00"
  }
]

5. Initial Stock & Poolstock

{
  "R1": { "finished_goods": 120, "poolstock": 80 },
  "R2": { "finished_goods": 50, "poolstock": 200 },
  "R3": { "finished_goods": 0, "poolstock": 150 },
  "R4": { "finished_goods": 300, "poolstock": 0 },
  "R5": { "finished_goods": 100, "poolstock": 100 },
  "R6": { "finished_goods": 40, "poolstock": 60 },
  "R7": { "finished_goods": 0, "poolstock": 300 },
  "R8": { "finished_goods": 200, "poolstock": 50 },

  "R9": { "finished_goods": 80, "poolstock": 20 },
  "R10": { "finished_goods": 150, "poolstock": 0 },
  "R11": { "finished_goods": 60, "poolstock": 40 },
  "R12": { "finished_goods": 0, "poolstock": 100 },
  "R13": { "finished_goods": 200, "poolstock": 0 },
  "R14": { "finished_goods": 30, "poolstock": 70 }
}

6. Cycle Times (Seconds per Unit)

{
  "R1": 4.5, "R2": 5.0, "R3": 4.0, "R4": 6.0,
  "R5": 4.2, "R6": 5.5, "R7": 3.8, "R8": 4.7,
  "R9": 6.5, "R10": 7.0, "R11": 5.8, "R12": 6.2,
  "R13": 7.5, "R14": 5.9
}

7. Changeover Matrix (Minutes)

Family 1

{
  "R1": { "R1": 0, "R2": 20, "R3": 25, "R4": 15, "R5": 30, "R6": 20, "R7": 10, "R8": 25 },
  "R2": { "R1": 20, "R2": 0, "R3": 30, "R4": 25, "R5": 35, "R6": 15, "R7": 20, "R8": 30 },
  "R3": { "R1": 25, "R2": 30, "R3": 0, "R4": 20, "R5": 10, "R6": 30, "R7": 25, "R8": 15 },
  "R4": { "R1": 15, "R2": 25, "R3": 20, "R4": 0, "R5": 30, "R6": 25, "R7": 20, "R8": 30 },
  "R5": { "R1": 30, "R2": 35, "R3": 10, "R4": 30, "R5": 0, "R6": 35, "R7": 30, "R8": 20 },
  "R6": { "R1": 20, "R2": 15, "R3": 30, "R4": 25, "R5": 35, "R6": 0, "R7": 15, "R8": 25 },
  "R7": { "R1": 10, "R2": 20, "R3": 25, "R4": 20, "R5": 30, "R6": 15, "R7": 0, "R8": 20 },
  "R8": { "R1": 25, "R2": 30, "R3": 15, "R4": 30, "R5": 20, "R6": 25, "R7": 20, "R8": 0 }
}

Family 2

{
  "R9":  { "R9": 0, "R10": 40, "R11": 45, "R12": 50, "R13": 35, "R14": 45 },
  "R10": { "R9": 40, "R10": 0, "R11": 50, "R12": 55, "R13": 45, "R14": 50 },
  "R11": { "R9": 45, "R10": 50, "R11": 0, "R12": 40, "R13": 50, "R14": 10 },
  "R12": { "R9": 50, "R10": 55, "R11": 40, "R12": 0, "R13": 55, "R14": 45 },
  "R13": { "R9": 35, "R10": 45, "R11": 50, "R12": 55, "R13": 0, "R14": 50 },
  "R14": { "R9": 45, "R10": 50, "R11": 10, "R12": 45, "R13": 50, "R14": 0 }
}

8. Python Planning Algorithm

import json
from datetime import datetime, timedelta

with open("factory_data.json") as f:
    data = json.load(f)

params = data["parameters"]
families = data["families"]
deliveries = data["outbound_deliveries"]
stock = data["initial_stock"]
cycle = data["cycle_times_seconds"]
changeover = data["changeover_matrix_minutes"]
pool = data["poolstock_strategy"]

def parse_time(t):
    return datetime.fromisoformat(t)

def production_duration(product, qty):
    return timedelta(seconds=qty * cycle[product])

def changeover_time(p1, p2):
    fam = "family1" if p1 in families["family1"]["references"] else "family2"
    return timedelta(minutes=changeover[fam][p1][p2])

def latest_finish(delivery):
    pick = parse_time(delivery["planned_picking_time"])
    return pick - timedelta(minutes=params["tpa_safety_window_minutes"])

mandatory_batches = []

for d in deliveries:
    prod = d["product"]
    qty = d["quantity"]
    lpft = latest_finish(d)

    available = stock[prod]["finished_goods"] + stock[prod]["poolstock"]

    if available >= qty:
        mandatory_batches.append({
            "delivery": d["delivery_id"],
            "product": prod,
            "qty": 0,
            "status": "covered_by_stock"
        })
        continue

    needed = qty - available

    target = params["batch_size_target"]
    if needed < params["batch_size_min"]:
        needed = target

    mandatory_batches.append({
        "delivery": d["delivery_id"],
        "product": prod,
        "qty": needed,
        "lpft": lpft,
        "status": "production_required"
    })

production_plan = []

for batch in mandatory_batches:
    if batch["status"] != "production_required":
        continue

    prod = batch["product"]
    qty = batch["qty"]
    lpft = batch["lpft"]

    eligible_lines = []
    for fam in families.values():
        if prod in fam["references"]:
            eligible_lines = fam["references"][prod]

    line = eligible_lines[0]

    duration = production_duration(prod, qty)
    start = lpft - duration

    production_plan.append({
        "line": line,
        "product": prod,
        "qty": qty,
        "start": start.isoformat(),
        "end": lpft.isoformat(),
        "reason": "TPA_delivery"
    })

for prod, rules in pool.items():
    current_ps = stock[prod]["poolstock"]
    min_ps = rules["min"]

    if current_ps < min_ps:
        qty = params["batch_size_target"]

        eligible_lines = []
        for fam in families.values():
            if prod in fam["references"]:
                eligible_lines = fam["references"][prod]

        line = eligible_lines[0]

        production_plan.append({
            "line": line,
            "product": prod,
            "qty": qty,
            "start": "AUTO",
            "end": "AUTO",
            "reason": "poolstock_replenishment"
        })

print("=== PRODUCTION PLAN ===")
for p in production_plan:
    print(p)

print("=== MANDATORY BATCHES ===")
for m in mandatory_batches:
    print(m)

End of Document