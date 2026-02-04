from data_loader import load_market_data
from model_core import run_model
from decision_engine import generate_signal
from regime_adjustment import adjust_for_regime


def forecast_asset(asset_name, asset_cfg, df_override=None):
    """
    asset_name : str   (z.B. "^GDAXI")
    asset_cfg  : dict  (z.B. {"ticker": "^GDAXI", "period": "5y", "interval": "1d"})
    df_override: DataFrame | None  (für Backtests)
    """

    # --- Daten laden (Live oder Backtest) ---
    if df_override is not None:
        df = df_override.copy()
    else:
        df = load_market_data(asset_cfg["ticker"], asset_cfg)

    # --- Sicherheitscheck ---
    if len(df) < 2:
        raise ValueError(f"Not enough data for {asset_name}")

    # --- Modell & Entscheidungslogik ---
    model_output = run_model(df)
    regime = adjust_for_regime(df)
    decision = generate_signal(model_output, regime)

    # --- Preise ---
    latest_close = df["close"].iloc[-1].item()
    prev_close = df["close"].iloc[-2].item()

    daily_return = (latest_close / prev_close) - 1

    # --- Ergebnis ---
    return {
        "asset": asset_name,
        "signal": decision["signal"],
        "confidence": decision["confidence"],
        "regime": regime,
        "prev_close": round(prev_close, 2),
        "close": round(latest_close, 2),
        "daily_return": round(daily_return * 100, 2),
        "score": round(model_output.get("score", 0.0), 4),
    }
