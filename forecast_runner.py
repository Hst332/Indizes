from assets.asset_config import ASSETS
from forecast_asset import forecast_asset

def run_all_forecasts():
    results = []

    for asset, cfg in ASSETS.items():
        try:
            result = forecast_asset(asset, cfg)
            results.append(result)
        except Exception as e:
            print(f"Forecast failed for {asset}: {e}")

    return results
