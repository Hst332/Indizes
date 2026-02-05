import pandas as pd


def summarize_backtest(results):
    """
    results: Liste von Dicts mit mindestens:
        - signal
        - future_return
    """

    if not results:
        return {}

    df = pd.DataFrame(results)

    # Future returns als Series
    rets = df["future_return"]

    total_trades = len(rets)
    win_rate = (rets > 0).sum() / total_trades * 100 if total_trades > 0 else 0

    avg_return = rets.mean()
    median_return = rets.median()
    max_return = rets.max()
    min_return = rets.min()

    summary = {
        "total_trades": int(total_trades),
        "win_rate": round(win_rate, 2),
        "avg_return": round(float(avg_return), 4),
        "median_return": round(float(median_return), 4),
        "max_return": round(float(max_return), 4),
        "min_return": round(float(min_return), 4),
    }

    return summary


def save_backtest_csv(results, filepath="backtest_results.csv"):
    """
    Speichert die einzelnen Trades als CSV.
    """
    if not results:
        print("No backtest results to save.")
        return

    df = pd.DataFrame(results)
    df.to_csv(filepath, index=False)
    print(f"Backtest results saved to {filepath}")
