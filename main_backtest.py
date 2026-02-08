from backtest_engine import run_backtest
from backtest_writer import summarize_backtest, save_backtest_csv
from asset_config import ASSETS

print("START BACKTEST")

all_results = {}

for asset, cfg in ASSETS.items():
    print(f"Running backtest for {asset}")

    results = run_backtest(asset, cfg)

    print("Results length:", len(results))

    # CSV erzwingen
    save_backtest_csv(results, filename=f"backtest_{asset}.csv")
    print("CSV WRITTEN:", f"backtest_{asset}.csv")

    summary = summarize_backtest(results)
    all_results[asset] = summary

print("FINISHED")
print(all_results)
