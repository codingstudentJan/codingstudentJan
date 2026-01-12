#!/usr/bin/env python3
import json
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "assets" / "visitors.json"
SVG  = ROOT / "assets" / "visitors.svg"

def make_svg(count: int) -> str:
    # Minimal, gut lesbar als GitHub-Avatar / Badge
    # 140x28 passt gut in READMEs
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="140" height="28" role="img" aria-label="visitors: {count}">
  <rect width="140" height="28" rx="6" fill="#0b0e14"/>
  <text x="12" y="18" fill="#9aa4b2" font-family="ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Arial" font-size="12">visitors</text>
  <text x="132" y="18" fill="#00ff9c" text-anchor="end" font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, monospace" font-size="12">{count}</text>
</svg>
"""

def main():
    DATA.parent.mkdir(parents=True, exist_ok=True)

    if DATA.exists():
        obj = json.loads(DATA.read_text(encoding="utf-8"))
    else:
        obj = {"count": 0, "updated_at": None}

    obj["count"] = int(obj.get("count", 0)) + 1
    obj["updated_at"] = datetime.now(timezone.utc).isoformat()

    DATA.write_text(json.dumps(obj, indent=2), encoding="utf-8")
    SVG.write_text(make_svg(obj["count"]), encoding="utf-8")

if __name__ == "__main__":
    main()
