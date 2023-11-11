# -----------------Vishal------------------

# ----------show any stock all information----------
# import yfinance as yf
# msft = yf.download("MSFT")
# print(msft)


# --------------if I want to see today and yesterday data----------------

# import yfinance as yf
# from datetime import date, timedelta
# today = date.today()
# yesterday = today - timedelta(5)
# a = yf.download('AAPL', start=yesterday, end=today)
# print(a)


# ---------------for custom (yyyy/mm/dd)--------------
# from datetime import date
# import yfinance as yf
# start = date(2020, 7, 1)
# end = date(2020, 7, 31)
# a = yf.download('AAPL', start=start, end=end)
# print(a)


# ---------see any company graph with custom year-----------
# from matplotlib import pyplot as plt
# import yfinance as yf
# ticker = yf.Ticker('AAPL')
# aapl_df = ticker.history(period="6y")
# aapl_df['Close'].plot(title="APPLE's stock price")
# plt.show()



# -----------comparing any company with graph-------------
# import pandas as pd
# import yfinance as yf
# from datetime import date, timedelta
# from matplotlib import pyplot as plt
#
# Start = date.today() - timedelta(365)
# Start.strftime('%Y-%m-%d')
#
# End = date.today() + timedelta(2)
# End.strftime('%Y-%m-%d')
# def closing_price(ticker):
#     Asset = pd.DataFrame(yf.download(ticker, start=Start,
#       end=End)['Adj Close'])
#     return Asset
#
# TESLA = closing_price('TSLA')
# AMAZON = closing_price('AMZN')
#
# plt.plot(TESLA, color='red', linewidth=2)
# plt.title('TESLA Performance')
# plt.ylabel('Price ($)')
# plt.xlabel('Date')
# plt.show()
#
# plt.plot(AMAZON, color='purple', linewidth=2)
# plt.title('AMAZON Performance')
# plt.ylabel('Price ($)')
# plt.xlabel('Date')
# plt.show()


# -----------If I only want to see garph of  closing point of any stock (Close,High,Volume and many more) ---------------

# import yfinance as yf
# a = yf.download('AAPL')
# from matplotlib import pyplot as plt
# a['Close'].plot(title="APPLE's stock price")
# plt.show()

# ---------- conver your date into dataframe for more flexibility-------------
# import pandas as pd
# df = pd.DataFrame(a)

# ----------------------------(how many days we have traded.. )--------

# from datetime import date
# import yfinance as yf
# import pandas as pd
# start = date(2020, 7, 1)
# end = date(2020, 7, 31)
# a = yf.download('AAPL', start=start, end=end)
# df = pd.DataFrame(a)
# print("From",start, "to",end,"we Trades",len(df),"days")


# -----------------Companies = compare with same graph----------------

# import matplotlib.pyplot as plt
# import yfinance as yf
#
# start = "2014-01-01"
# end = '2019-1-01'
# tcs = yf.download('TCS',start,end)
# infy = yf.download('INFY',start,end)
# wipro = yf.download('WIPRO.NS',start,end)
# plt.plot(tcs, color='red', linewidth=1)
# plt.plot(infy, color='black', linewidth=2)
# plt.plot(wipro, color='purple', linewidth=0.55)
# plt.show()


# -----------------compare many company data with same graph-----------------
#
# import matplotlib.pyplot as plt
# import yfinance as yf
#
# start = "2014-01-01"
# end = '2019-1-01'
# tcs = yf.download('TCS',start,end)
# infy = yf.download('INFY',start,end)
# wipro = yf.download('WIPRO.NS',start,end)
# tcs['MarktCap'] = tcs['Open'] * tcs['Volume']
# infy['MarktCap'] = infy['Open'] * infy['Volume']
# wipro['MarktCap'] = wipro['Open'] * wipro['Volume']
# tcs['MarktCap'].plot(color='black', label = 'TCS', figsize = (15,7))
# infy['MarktCap'].plot(color='purple', label = 'Infosys')
# wipro['MarktCap'].plot(color='red', label = 'Wipro')
# plt.title('Market Cap')
# plt.legend()
# plt.show()

