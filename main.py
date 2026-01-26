from forecast_runner import run_all_forecasts
from forecast_writer import write_forecasts

def main():
    forecasts = run_all_forecasts()
    write_forecasts(forecasts)

if __name__ == "__main__":
    main()
