# data_loader.py
import pandas as pd
import numpy as np

def load_market_data(symbol):
    """
    Dummy-Marktdaten (Platzhalter)
    """
    print(f"Loading market data for {symbol}")

    dates = pd.date_range(end=pd.Timestamp.today(), periods=30)
    prices = 100 + np.cumsum(np.random.normal(0, 1, size=len(dates)))

    df = pd.DataFrame({
        "close": prices
    }, index=dates)

    return df
