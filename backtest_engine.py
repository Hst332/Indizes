from forecast_asset import forecast_asset


def run_backtest(asset_name, asset_cfg):
    """
    Führt Backtest für ein Asset aus.
    Gibt Liste von Trade-Resultaten zurück.
    """

    results = []

    # Forecast ausführen
    forecast = forecast_asset(asset_name, asset_cfg)

    # Zukunftsrendite simulieren (Placeholder – später echte Logik)
    future_return = forecast["daily_return"] / 100.0

    results.append({
        "asset": asset_name,
        "signal": forecast["signal"],
        "confidence": forecast["confidence"],
        "regime": forecast["regime"],
        "close": forecast["close"],
        "future_return": future_return,
        "score": forecast["score"],
    })

    return results
