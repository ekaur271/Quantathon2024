import pandas as pd
from datetime import datetime

data = pd.read_csv("DAL_data.csv")
date_format = "%Y-%m-%d"

#df = pd.DataFrame(data, columns=['Date'])
df = pd.DataFrame()
df.insert(0, 'Date', pd.to_datetime(data['Date']))
df.insert(0, 'Day', df['Date'].dt.day)
df.insert(0, 'Month', df['Date'].dt.month)
df.insert(0, 'Year', df['Date'].dt.year)
df.insert(1,'Daily Price Range', data['High'] - data['Low'])
df.insert(1, 'Daily Price Volatility', df['Daily Price Range']/data['Close'])
df.insert(1, 'Price Change', data['Close']- data['Open'])
df.insert(1, 'Price Momentum', data['Close'].diff())
df.insert(1, 'Price Ratio', data['Close']/data['Open'])
df.insert(1, 'Relative Strength', (data['Close'] - data['Low'])/(data['High'] - data['Low']))
df.insert(1, 'Adj Close', data['Adj Close'])
df.insert(1, 'Volume Change', data['Volume'].diff())
df.insert(1, "Close", data['Close'])

# CSV
df.to_csv('delta_calc.csv')

# Monthly Calculations
df.groupby(['Year', 'Month']).mean()

# CSV
df.to_csv('delta_calc_monthly.csv')



