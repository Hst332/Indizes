from asset_config import ASSETS
from forecast_asset import forecast_asset


def run_all_forecasts():
    results = []

    for asset, cfg in ASSETS.items():
        result = forecast_asset(asset, cfg)
        results.append(result)

    return results
