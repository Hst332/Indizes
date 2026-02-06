import pandas as pd


def summarize_backtest(results):

    df = pd.DataFrame(results)

    # Sicherheitskonvertierung
    df["future_return"] = pd.to_numeric(df["future_return"], errors="coerce")

    rets = df["future_return"].dropna()

    total_trades = len(rets)

    if total_trades == 0:
        return {
            "trades": 0,
            "winrate": 0,
            "avg_return": 0
        }

    winrate = round((rets.gt(0).sum() / total_trades) * 100, 2)
    avg_return = round(rets.mean() * 100, 2)

    return {
        "trades": total_trades,
        "winrate": winrate,
        "avg_return": avg_return
    }


def save_backtest_csv(results, asset_name):
    import pandas as pd

    df = pd.DataFrame(results)

    if df.empty:
        df = pd.DataFrame(
            columns=["date", "signal", "price", "future_return"]
        )

    filename = f"backtest_{asset_name}.csv"
    df.to_csv(filename, index=False)

    print(f"Saved {filename} ({len(df)} rows)")
