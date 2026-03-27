import yfinance as yf
import pandas


#-------------------------
# Growth Charts
#-------------------------

def add_growth_curves(dataframe):
    market_return = dataframe["market_return"]
    strategy_return = dataframe["strategy_return"]

    #growht over time
    market_curve = (1 + market_return).cumprod()
    strategy_curve = (1 + strategy_return).cumprod()

    dataframe["market_curve"] = market_curve
    dataframe["strategy_curve"] = strategy_curve

    return dataframe