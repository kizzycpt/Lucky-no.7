from variables.variables import ticker_symbol, start_date, end_date, fast_ma_period, slow_ma_period
from variables.download_data import download_data
from variables.averages import add_averages
from variables.signals import add_signals
from variables.returns import add_returns
from variables.growth_curve import add_growth_curves
from variables.profit_rate import calculate_win_rate


def results():
    dataframe = download_data(ticker_symbol, start_date, end_date)
    dataframe = add_averages(dataframe, fast_ma_period, slow_ma_period)
    dataframe = add_signals(dataframe)
    dataframe = add_returns(dataframe)
    dataframe = add_growth_curves(dataframe)

    win_rate = calculate_win_rate(dataframe)

    final_strategy_value = dataframe["strategy_curve"].iloc[-1]
    final_market_value = dataframe["market_curve"].iloc[-1]

    strategy_total_return = (final_strategy_value - 1) * 100
    market_total_return = (final_market_value - 1) * 100

    try:
        print("Win rate:", round(win_rate * 100, 2), "%")
        print("Strategy total return:", round(strategy_total_return, 2), "%")
        print("Market total return:", round(market_total_return, 2), "%")
    except Exception as e:
        print(f"[!] Error in getting results [!]\n{e}. Please try again.")

if __name__ == "__main__":
    results()