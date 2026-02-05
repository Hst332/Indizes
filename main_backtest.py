from backtest_engine import run_backtest
from backtest_writer import summarize_backtest, save_backtest_csv
from assets_config import ASSETS



all_results = {}

for asset, cfg in ASSETS.items():

    results_df = run_backtest(asset, cfg)

    save_backtest_csv(results_df, asset)

    summary = summarize_backtest(results_df)

    all_results[asset] = summary


print("\n=== BACKTEST SUMMARIES ===")
for asset, s in all_results.items():
    print(asset, s)
