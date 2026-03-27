import yfinance as yf
import pandas


#-------------------------
# Profit Rate
#-------------------------

def calculate_win_rate(dataframe):
    position_in_days = dataframe["signal"].shift(1) == 1
    trades = dataframe.loc[position_in_days, "strategy_return"].dropna()

    winning_trades = trades > 0
    win_rate = winning_trades.mean()

    return win_rate