import yfinance as yf
import pandas


#-------------------------
# Signals for algorithm to act
#-------------------------

def add_signals(dataframe):
    # not in trade
    default_signal = 0

    #in trade
    buy_signal = 1


    dataframe["signal"] = default_signal

    #self explanatory
    buy_condition = dataframe["ma_fast"] > dataframe["ma_slow"]
    dataframe.loc[buy_condition, "signal"] = buy_signal

    return dataframe

