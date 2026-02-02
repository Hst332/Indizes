def summarize_backtest(results):
    stats = {
        "BUY": [],
        "SELL": [],
        "HOLD": []
    }

    for r in results:
        stats[r["signal"]].append(r["future_return"])

    summary = {}
    for signal, rets in stats.items():
        if rets:
            summary[signal] = {
                "count": len(rets),
                "avg_return": round(sum(rets) / len(rets), 2),
                "win_rate": round(
                    sum(1 for r in rets if r > 0) / len(rets) * 100, 2
                )
            }

    return summary
