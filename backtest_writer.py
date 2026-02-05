import pandas as pd


def summarize_backtest(results):

    df = pd.DataFrame(results)

    rets = df["future_return"]

    total_trades = len(rets)

    winrate = round((rets > 0).sum() / total_trades * 100, 2)

    avg_return = round(rets.mean() * 100, 2)

    return {
        "trades": total_trades,
        "winrate": winrate,
        "avg_return": avg_return
    }


def save_backtest_csv(results, asset_name):

    df = pd.DataFrame(results)
    filename = f"backtest_{asset_name}.csv"
    df.to_csv(filename, index=False)
