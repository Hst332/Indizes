import pandas as pd
import numpy as np


def summarize_backtest(results_df):

    if len(results_df) == 0:
        return {"error": "no trades"}

    rets = results_df["strategy_return"].astype(float)

    total_trades = len(rets)
    wins = (rets > 0).sum()
    losses = (rets < 0).sum()

    win_rate = wins / total_trades * 100

    equity_curve = (1 + rets).cumprod()

    max_drawdown = (
        (equity_curve / equity_curve.cummax()) - 1
    ).min()

    sharpe = (
        rets.mean() / (rets.std() + 1e-9)
    ) * np.sqrt(252)

    return {
        "total_trades": int(total_trades),
        "win_rate": round(win_rate, 2),
        "avg_return": round(rets.mean(), 4),
        "median_return": round(rets.median(), 4),
        "max_return": round(rets.max(), 4),
        "min_return": round(rets.min(), 4),
        "sharpe": round(sharpe, 2),
        "max_drawdown": round(float(max_drawdown), 4),
    }


def save_backtest_csv(results_df, asset_name):
    filename = f"{asset_name}_backtest.csv"
    results_df.to_csv(filename, index=False)
    print(f"Backtest results saved to {filename}")
