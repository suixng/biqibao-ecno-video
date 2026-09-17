#!/usr/bin/env python3
"""Validate basic semantic and layout declarations in an asset manifest."""

import json
import sys
from pathlib import Path


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(1)


def main() -> None:
    if len(sys.argv) != 2:
        fail("usage: validate_asset_manifest.py <asset-manifest.json>")
    path = Path(sys.argv[1])
    data = json.loads(path.read_text(encoding="utf-8"))
    assets = {asset["id"]: asset for asset in data.get("assets", [])}
    if len(assets) != len(data.get("assets", [])):
        fail("asset ids must be unique")

    role_uses: dict[str, list[str]] = {}
    for unit in data.get("units", []):
        groups = unit.get("groups", [])
        count = len(groups)
        if count > 3:
            fail(f"unit {unit['id']} has {count} information groups; split or merge it")
        expected = {1: {"center"}, 2: {"left", "right"}, 3: {"left", "center", "right"}}.get(count, set())
        actual = {group.get("slot") for group in groups}
        if actual != expected:
            fail(f"unit {unit['id']} slots {sorted(actual)} must be {sorted(expected)}")
        for group in groups:
            for asset_id in group.get("asset_ids", []):
                if asset_id not in assets:
                    fail(f"unit {unit['id']} references missing asset {asset_id}")
                asset = assets[asset_id]
                if unit["id"] not in asset.get("allowed_units", []):
                    fail(f"asset {asset_id} is not allowed in unit {unit['id']}")
                if asset.get("kind") == "role":
                    role_uses.setdefault(asset_id, []).append(unit["id"])

    reused = {asset_id: units for asset_id, units in role_uses.items() if len(set(units)) > 1}
    if reused:
        detail = ", ".join(f"{asset_id}: {sorted(set(units))}" for asset_id, units in reused.items())
        fail(f"role poses may not be reused across semantic units: {detail}")
    print("Manifest declaration checks passed.")


if __name__ == "__main__":
    main()
