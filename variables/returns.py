
#-------------------------
# Returns made
#-------------------------

def add_returns(dataframe):
    close_price = dataframe["Close"]

    #calculates percent changes
    market_return = close_price.pct_change()
    dataframe["market_return"] = market_return

    #last days returns in reference
    previous_return = dataframe["signal"].shift(1)
    strategy_return = previous_return * market_return

    dataframe["strategy_return"] = strategy_return

    return dataframe