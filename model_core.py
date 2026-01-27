def run_model(df):
    """
    Einfaches Momentum-Modell:
    Durchschnittliche Rendite der letzten 5 Tage
    """
    df = df.copy()

    df["ret"] = df["close"].pct_change()
    score = df["ret"].rolling(5).mean().iloc[-1]

    # Sicherheit gegen NaN
    if score != score:  # NaN-Check
        score = 0.0

    return {
        "score": float(score)
    }
