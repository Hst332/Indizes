from forecast_runner import run_all_forecasts
from forecast_writer import write_forecasts


if __name__ == "__main__":
    forecasts = run_all_forecasts()
    write_forecasts(forecasts)
