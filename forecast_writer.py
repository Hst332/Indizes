import json
from datetime import date
from pathlib import Path

def write_forecasts(forecasts):
    today = date.today().isoformat()

    daily_path = Path(f"forecasts/daily/{today}.json")
    history_path = Path("forecasts/history/all_forecasts.json")

    daily_path.parent.mkdir(parents=True, exist_ok=True)
    history_path.parent.mkdir(parents=True, exist_ok=True)

    daily_path.write_text(json.dumps(forecasts, indent=2))

    if history_path.exists():
        history = json.loads(history_path.read_text())
    else:
        history = []

    history.append({"date": today, "forecasts": forecasts})
    history_path.write_text(json.dumps(history, indent=2))
