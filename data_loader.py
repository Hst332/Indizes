import yfinance as yf
import pandas as pd


def load_market_data(symbol, period="6mo"):
    """
    Lädt Marktdaten über yfinance und gibt sauberes DataFrame zurück
    """
    print(f"Loading market data for {symbol}")

    df = yf.download(
        symbol,
        period=period,
        interval="1d",
        auto_adjust=True,
        progress=False
    )

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

    print(
        f"{symbol}: rows={len(df)} | "
        f"last close={df['close'].iloc[-1]:.2f}"
    )

    return df
