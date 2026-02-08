from backtest_engine import run_backtest
from backtest_writer import summarize_backtest, save_backtest_csv
from asset_config import ASSETS

all_results = {}

for asset, cfg in ASSETS.items():
    print(f"Running backtest for {asset}")

    results = run_backtest(asset, cfg)

    # CSV SOFORT schreiben
    save_backtest_csv(results, filename=f"backtest_{asset}.csv")

    summary = summarize_backtest(results)
    all_results[asset] = summary

print(all_results)
