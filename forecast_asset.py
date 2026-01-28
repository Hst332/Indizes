from data_loader import load_market_data
from model_core import run_model
from decision_engine import generate_signal
from regime_adjustment import adjust_for_regime



def forecast_asset(asset_name, asset_cfg):
    df = load_market_data(asset_cfg["ticker"])

    model_output = run_model(df)
    regime = adjust_for_regime(df)
    decision = generate_signal(model_output, regime)

    return {
        "asset": asset_name,
        "signal": decision["signal"],
        "confidence": decision["confidence"],
        "regime": regime
    }
