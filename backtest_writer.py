import pandas as pd

def summarize_backtest(results):
    rets = []

    for r in results:
        val = r["future_return"]
        if isinstance(val, pd.Series):
            val = float(val.iloc[0])
        else:
            val = float(val)

        rets.append(val)

    if len(rets) == 0:
        return {}

    summary = {
        "trades": len(rets),
        "win_rate": round(sum(1 for r in rets if r > 0) / len(rets) * 100, 2),
        "avg_return": round(sum(rets) / len(rets), 4),
        "total_return": round(sum(rets), 4),
    }

    return summary
