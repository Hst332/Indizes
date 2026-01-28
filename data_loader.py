# data_loader.py

import yfinance as yf
import pandas as pd


def load_market_data(symbol, period="5y"):
    """
    Lädt historische Marktdaten und gibt sauberen DataFrame zurück.
    """

    print(f"Loading market data for {symbol}")

    df = yf.download(
        symbol,
        period=period,
        auto_adjust=True,
        progress=False
    )

    if df.empty:
        raise ValueError(f"No data returned for {symbol}")

    # Spalten vereinheitlichen
    df = df.rename(columns={
        "Open": "open",
        "High": "high",
        "Low": "low",
        "Close": "close",
        "Volume": "volume"
    })

    # Renditen
    df["ret"] = df["close"].pct_change()

    # NaNs entfernen
    df = df.dropna()

    return df
