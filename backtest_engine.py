import pandas as pd
from forecast_asset import forecast_asset
from data_loader import load_market_data


def run_backtest(asset_name, asset_cfg):

    print(f"Running walk-forward backtest for {asset_name}")

    # komplette Historie laden
    df = load_market_data(asset_cfg["ticker"], asset_cfg)

    if df is None or len(df) < 50:
        raise ValueError("Not enough data for backtest")

    results = []

    # Walk-forward: jeden Tag Forecast erzeugen
    for i in range(60, len(df) - 1):   # warmup für Indikatoren / Modell

        sliced_df = df.iloc[:i].copy()

        try:
            forecast = forecast_asset(
                asset_name,
                asset_cfg,
                df_override=sliced_df
            )
        except Exception as e:
            print(f"Forecast failed at index {i}: {e}")
            continue

        signal = forecast["signal"]

        today_close = df["close"].iloc[i]
        next_close = df["close"].iloc[i + 1]

        future_return = (next_close / today_close) - 1

        # Signal Performance berechnen
        if signal == "LONG":
            strategy_return = future_return
        elif signal == "SHORT":
            strategy_return = -future_return
        else:
            strategy_return = 0.0

        results.append({
            "date": df.index[i],
            "signal": signal,
            "confidence": forecast["confidence"],
            "regime": forecast["regime"],
            "market_return": future_return,
            "strategy_return": strategy_return,
        })

    return pd.DataFrame(results)
