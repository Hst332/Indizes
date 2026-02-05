from backtest_engine import run_backtest
from backtest_writer import summarize_backtest, save_backtest_csv

ASSETS = {
    "DAX": {"ticker": "^GDAXI"},
    # weitere Assets...
}

if __name__ == "__main__":
    all_results = {}   # <- wichtig!

    for asset, cfg in ASSETS.items():
        print(f"Running backtest for {cfg['ticker']}")

        results = run_backtest(asset, cfg)

        summary = summarize_backtest(results)
        all_results[asset] = summary

        save_backtest_csv(results, f"{asset}_backtest.csv")

    print("Backtest summaries:")
    print(all_results)
