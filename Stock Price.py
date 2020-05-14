import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates
import pandas as pd
import pandas_datareader.data as web
from pandas.util.testing import assert_frame_equal

# style.use('ggplot')

# start = dt.datetime(2000, 1, 1)
# end = dt.datetime(2020, 3, 30)

# df = web.DataReader('ENPH', 'yahoo', start, end)
# print(df.head(6))
# print(df.tail(6))

# df.to_csv('enph.csv')

# print(df.tail())
# $print(df[['Open', 'High']].tail())

# df['Adj Close'].plot()
# plt.show()


df = pd.read_csv('enph.csv', parse_dates = True, index_col=0)

# This creates a new column in the CSV called the 100MA which is calculated by finding the 100 day moving average
#df['100ma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean()

# print(df.head()) # prints the first 5 values
# print(df.tail()) # prints the last 5 values

ax1 = plt.subplot2grid((6, 1), (0, 0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6, 1), (5, 0), rowspan=1, colspan=1, sharex=ax1)

# this creates the graph, plotting Adj Close and 100MA based on volume
# ax1.plot(df.index, df['Adj Close'])
# ax1.plot(df.index, df['100ma'])
# ax2.bar(df.index, df['Volume'])

# plt.show()

# resample can switch the data from being daily data to being 10 day data
df_mean = df['Adj Close'].resample('10D').mean() # get the average value over 10 days
df_volume = df['Volume'].resample('10D').sum() # get the sum value over 10 days
df_ohlc = df['Adj Close'].resample('10D').ohlc() # get the open high low close values over 10 days

df_ohlc.reset_index(inplace=True)

df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num) # this will convert date time to mdate format

ax1.xaxis_date()

candlestick_ohlc(ax1, df_ohlc.values, width =2, colorup = 'g')
ax2.fill_between(df_volume.index.map(mdates.date2num), df_volume.values, 0)

plt.show()
