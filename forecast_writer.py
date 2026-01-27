from pathlib import Path
from datetime import date
import json

def write_forecasts(forecasts):
    print(">>> TXT WRITER IS RUNNING <<<")

    today = date.today().isoformat()

    base = Path("forecasts")
    daily = base / "daily"
    history = base / "history"
    txt = base / "txt"

    daily.mkdir(parents=True, exist_ok=True)
    history.mkdir(parents=True, exist_ok=True)
    txt.mkdir(parents=True, exist_ok=True)

    with open(daily / f"{today}.json", "w") as f:
        json.dump(forecasts, f, indent=2)

    hist_file = history / "all_forecasts.json"
    history_data = []

    if hist_file.exists():
        with open(hist_file) as f:
            history_data = json.load(f)

    history_data.append({
        "date": today,
        "forecasts": forecasts
    })

    with open(hist_file, "w") as f:
        json.dump(history_data, f, indent=2)

    with open(txt / f"{today}.txt", "w") as f:
        f.write(f"Index Forecasts – {today}\n")
        f.write("=" * 40 + "\n\n")
        for item in forecasts:
            f.write(
                f"{item['asset']}: "
                f"{item['signal']} "
                f"(Confidence: {item['confidence']:.2f}, "
                f"Regime: {item['regime']})\n"
            )
