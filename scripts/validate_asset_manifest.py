#!/usr/bin/env python3
"""校验素材清单中的基础语义和构图声明。"""

import json
import sys
from pathlib import Path


def fail(message: str) -> None:
    print(f"错误：{message}")
    raise SystemExit(1)


def main() -> None:
    if len(sys.argv) != 2:
        fail("用法：validate_asset_manifest.py <asset-manifest.json>")
    path = Path(sys.argv[1])
    data = json.loads(path.read_text(encoding="utf-8"))
    assets = {asset["id"]: asset for asset in data.get("assets", [])}
    if len(assets) != len(data.get("assets", [])):
        fail("素材 ID 必须唯一")

    role_uses: dict[str, list[str]] = {}
    for unit in data.get("units", []):
        groups = unit.get("groups", [])
        count = len(groups)
        if count > 3:
            fail(f"画面单元 {unit['id']} 有 {count} 个信息组；请拆分或合并")
        expected = {1: {"center"}, 2: {"left", "right"}, 3: {"left", "center", "right"}}.get(count, set())
        actual = {group.get("slot") for group in groups}
        if actual != expected:
            fail(f"画面单元 {unit['id']} 的槽位 {sorted(actual)} 必须为 {sorted(expected)}")
        for group in groups:
            for asset_id in group.get("asset_ids", []):
                if asset_id not in assets:
                    fail(f"画面单元 {unit['id']} 引用了不存在的素材 {asset_id}")
                asset = assets[asset_id]
                if unit["id"] not in asset.get("allowed_units", []):
                    fail(f"素材 {asset_id} 不允许出现在画面单元 {unit['id']}")
                if asset.get("kind") == "role":
                    role_uses.setdefault(asset_id, []).append(unit["id"])

    reused = {asset_id: units for asset_id, units in role_uses.items() if len(set(units)) > 1}
    if reused:
        detail = ", ".join(f"{asset_id}: {sorted(set(units))}" for asset_id, units in reused.items())
        fail(f"角色姿态不得跨语义单元复用：{detail}")
    print("素材清单声明检查通过。")


if __name__ == "__main__":
    main()
