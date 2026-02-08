from data_loader import load_market_data
from model_core import run_model
from decision_engine import generate_signal
from regime_adjustment import adjust_for_regime


def forecast_asset(asset_name, asset_cfg, df_override=None):
    """
    df_override wird vom Backtest übergeben.
    Live-System lädt Daten normal.
    """

    # Backtest → vorhandenes Slice nutzen
    if df_override is not None:
        df = df_override
    else:
        df = load_market_data(asset_cfg["ticker"])

    model_output = run_model(df)
    regime = adjust_for_regime(df)
    decision = generate_signal(model_output, regime)

    latest_close = float(df["close"].iloc[-1])
    prev_close = float(df["close"].iloc[-2])

    daily_return = (latest_close / prev_close) - 1

    return {
        "asset": asset_name,
        "signal": decision["signal"],
        "prev_close": round(prev_close, 2),
        "confidence": decision["confidence"],
        "regime": regime,
        "close": round(latest_close, 2),
        "daily_return": round(daily_return * 100, 2),
        "score": round(model_output.get("score", 0.0), 4),
    }
