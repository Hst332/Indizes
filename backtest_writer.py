import pandas as pd


def save_backtest_csv(results, filename="backtest_results.csv"):
    rows = []

    for r in results:
        val = r.get("future_return", 0)

        if isinstance(val, pd.Series):
            val = float(val.iloc[0])
        else:
            val = float(val)

        rows.append({
            "date": r.get("date"),
            "signal": r.get("signal"),
            "future_return": val,
            "regime": r.get("regime"),
            "confidence": r.get("confidence"),
        })

    df = pd.DataFrame(rows)
    df.to_csv(filename, index=False)


def summarize_backtest(results):
    rets = []

    for r in results:
        val = r.get("future_return", 0)

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
