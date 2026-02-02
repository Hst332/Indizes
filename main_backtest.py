from backtest_runner import run_backtest
from backtest_writer import summarize_backtest

ASSETS = {
    "^GDAXI": {"period": "5y", "interval": "1d"},
    "^ATX":   {"period": "5y", "interval": "1d"},
    "^DJI":   {"period": "5y", "interval": "1d"},
}

all_results = {}

for asset, cfg in ASSETS.items():
    print(f"Running backtest for {asset}")
    results = run_backtest(asset, cfg)
    summary = summarize_backtest(results)
    all_results[asset] = summary
    print(summary)
