import json
import pandas as pd

with open("forecasts/history/all_forecasts.json") as f:
    data = json.load(f)

records = []

for entry in data:
    date = entry["timestamp"]
    for fcast in entry["forecasts"]:
        records.append({
            "date": date,
            "asset": fcast["asset"],
            "signal": fcast["signal"],
            "confidence": fcast["confidence"]
        })

df = pd.DataFrame(records)
print(df.head())
