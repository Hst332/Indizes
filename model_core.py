def run_model(df):
    """
    Einfaches Momentum-Modell (robust gegen Spaltennamen)
    """
    df = df.copy()

    # mögliche Close-Spalten
    close_cols = ["close", "Close", "adj_close", "Adj Close"]

    close_col = None
    for c in close_cols:
        if c in df.columns:
            close_col = c
            break

    if close_col is None:
        raise ValueError(f"No close price column found. Columns: {df.columns}")

    df["ret"] = df[close_col].pct_change()
    score = df["ret"].rolling(5).mean().iloc[-1]

    if score != score:  # NaN
        score = 0.0

    return {
        "score": float(score)
    }
