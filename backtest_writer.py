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
        if not rets:
            continue

        wins = sum(1 for r in rets if r > 0)

        summary[signal] = {
            "count": len(rets),
            "avg_return": round(sum(rets) / len(rets), 2),
            "win_rate": round(wins / len(rets) * 100, 2),
        }

    return summary
