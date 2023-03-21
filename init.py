import yfinance as yf
from yahoo_fin import stock_info as si


# We'll start by only looking through stocks in SP500, later we'll use more (maybe even all stocks?) 
tickers = si.tickers_sp500()
print(tickers)

print(ticker.info)

# # Get a list of all publicly traded companies
# tickers = yf.Tickers('')

# print(tickers)

# # Loop through each ticker to get market cap data
# for ticker in tickers.tickers:
#     data = ticker.info
#     # Check if the company has market cap data and if it is above 300 billion
#     if 'marketCap' in data and data['marketCap'] > 2*(10**6):
#         print(data['symbol'], data['longName'])