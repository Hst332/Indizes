def generate_signal(model_output, regime):
    """
    Erzeugt ein Handelssignal aus Modell + Regime
    """
    score = model_output.get("score", 0.0)

    if score > 0.2:
        signal = "BUY"
    elif score < -0.2:
        signal = "SELL"
    else:
        signal = "HOLD"

    return {
        "signal": signal,
        "confidence": abs(score)
    }
