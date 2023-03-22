import yahooquery

ticker = yahooquery.Ticker("aapl")
print(ticker.financial_data['aapl'].keys())