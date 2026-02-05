from backtest_engine import run_backtest
from backtest_writer import summarize_backtest, save_backtest_csv



if __name__ == "__main__":

    all_results = {}

    for asset, cfg in ASSETS.items():

        results = run_backtest(asset, cfg)

        summary = summarize_backtest(results)

        save_backtest_csv(results, asset)

        all_results[asset] = summary

        print(asset, summary)
