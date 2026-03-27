import yfinance as yf

#-------------------------
# Download Data
#-------------------------

#yahoo finance information

def download_data(ticker_symbol, start_date, end_date):
    stock_data = yf.download(ticker_symbol, start=start_date, end=end_date)

    close_price = stock_data["Close"]

    # if Close comes back as a 1-column DataFrame, convert it to a Series
    if hasattr(close_price, "ndim") and close_price.ndim > 1:
        close_price = close_price.iloc[:, 0]

    dataframe = close_price.to_frame(name="Close")
    return dataframe
