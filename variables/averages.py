
#-------------------------
# Moving Averages and Percentages for whatever done got invested
#-------------------------

def add_averages(dataframe, fast_ma_period, slow_ma_period):
    #collects close prices d

    close_price = dataframe["Close"]

    #averages in market
    fast_moving_average = close_price.rolling(fast_ma_period).mean()
    slow_moving_average = close_price.rolling(slow_ma_period).mean()

    #stores values for later use
    dataframe["ma_fast"] = fast_moving_average
    dataframe["ma_slow"] = slow_moving_average

    return dataframe
