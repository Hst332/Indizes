from data_loader import load_market_data
from forecast_asset import forecast_asset

BACKTEST_MODE = True

def make_decision(signal_strength, confidence):

    if BACKTEST_MODE:
        if signal_strength > 0:
            return "LONG"
        elif signal_strength < 0:
            return "SHORT"
        else:
            return None

    # Live-Logik (unverändert lassen!)
    if confidence > 0.6 and abs(signal_strength) > 0.5:
        return "LONG" if signal_strength > 0 else "SHORT"

    return None


def run_backtest(asset_name, asset_cfg, lookback=120):

    print(f"Running backtest for {asset_name}")

    df = load_market_data(asset_cfg["ticker"], asset_cfg)

    results = []

    # walk forward
    for i in range(lookback, len(df) - 1):

        sliced_df = df.iloc[:i].copy()

        forecast = forecast_asset(asset_name, asset_cfg, df_override=sliced_df)

        future_close = df["close"].iloc[i + 1]
        current_close = df["close"].iloc[i]

        future_return = (future_close / current_close) - 1

        results.append({
            "date": df.index[i],
            "signal": forecast["signal"],
            "confidence": forecast["confidence"],
            "regime": forecast["regime"],
            "future_return": future_return
        })

    return results
