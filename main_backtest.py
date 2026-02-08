from backtest_runner import run_backtest
from backtest_writer import summarize_backtest, save_backtest_csv
from asset_config import ASSETS

all_results = {}   # <---- FEHLTE

for asset, cfg in ASSETS.items():
    print(f"Running backtest for {cfg['ticker']}")

    results = run_backtest(asset, cfg)

    # CSV VOR dem Summary erzeugen
    save_backtest_csv(results, filename=f"backtest_{asset}.csv")

    summary = summarize_backtest(results)
    all_results[asset] = summary

print(all_results)
