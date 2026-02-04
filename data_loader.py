import yfinance as yf
import pandas as pd

def load_market_data(symbol, cfg):
    print(f"Loading market data for {symbol}")

    period = cfg.get("period", "1y")
    interval = cfg.get("interval", "1d")

    df = yf.download(
        symbol,
        period=period,
        interval=interval,
        auto_adjust=False,
        progress=False
    )

    if df.empty:
        raise ValueError(f"No data loaded for {symbol}")

    df = df.rename(columns=str.lower)
    return df


    if df.empty:
        raise ValueError(f"No data loaded for {symbol}")

    # Einheitliche Spalten
    df = df.rename(columns={
        "Close": "close",
        "Open": "open",
        "High": "high",
        "Low": "low",
        "Volume": "volume"
    })

    # Rendite
    df["ret"] = df["close"].pct_change()

    # Aufräumen
    df = df.dropna()

    last_close = float(df["close"].iloc[-1])

    print(
        f"{symbol}: rows={len(df)} | "
        f"last close={last_close:.2f}"
    )


    return df
