from backtest_runner import run_backtest
from backtest_writer import summarize_backtest
from backtest_writer import summarize_backtest, save_backtest_csv

ASSETS = {
    "^GDAXI": {"ticker": "^GDAXI", "period": "5y", "interval": "1d"},
}
all_results = {}

for asset, cfg in ASSETS.items():
    print(f"Running backtest for {asset}")
    results = run_backtest(asset, cfg)

    save_backtest_csv(results, f"backtest_{asset}.csv")

    summary = summarize_backtest(results)
    all_results[asset] = summary
    print(summary)

