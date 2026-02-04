def summarize_backtest(results):
    stats = {
        "BUY": [],
        "SELL": [],
        "HOLD": []
    }

    for r in results:
        signal = r["signal"]
        future_ret = float(r["future_return"])
        stats[signal].append(future_ret)

    summary = {}

    for signal, rets in stats.items():
        if len(rets) == 0:
            continue

        wins = sum(1 for x in rets if x > 0)

        summary[signal] = {
            "count": len(rets),
            "avg_return": round(sum(rets) / len(rets), 2),
            "win_rate": round(wins / len(rets) * 100, 2),
        }

    return summary
