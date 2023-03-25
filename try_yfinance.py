import yfinance as yf
from yahoo_fin import stock_info as si
import yahooquery

ticker = yahooquery.Ticker("MSFT")
data_total = ticker.financial_data

print(data_total["MSFT"].keys())

# # Get a list of all publicly traded companies
# tickers = yf.Tickers('')

# print(tickers)

# # Loop through each ticker to get market cap data
# for ticker in tickers.tickers:
#     data = ticker.info
#     # Check if the company has market cap data and if it is above 300 billion
#     if 'marketCap' in data and data['marketCap'] > 2*(10**6):
#         print(data['symbol'], data['longName'])




