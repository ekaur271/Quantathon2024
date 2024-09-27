import pandas as pd

data1 = pd.read_csv("crude_calc.csv")
data2 = pd.read_csv("delta_calc.csv")

df = pd.DataFrame()
df.insert(0, 'Date', pd.to_datetime(data1['Date']))
df.insert(0, 'Month', data2['Month'])
df.insert(0, 'Year', data2['Year'])
df.insert(1,'Daily Price Range', (data1['Daily Price Range'] + data2['Daily Price Range'])/2)
df.insert(1, 'Daily Price Volatility', (data1['Daily Price Volatility'] + data2['Daily Price Volatility'])/2)
df.insert(1, 'Price Change', (data1['Price Change'] + data2['Price Change'])/2)
df.insert(1, 'Price Momentum', (data1['Price Momentum'] + data2['Price Momentum'])/2)
df.insert(1, 'Price Ratio', (data1['Price Ratio'] + data2['Price Ratio'])/2)
df.insert(1, 'Relative Strength', (data1['Relative Strength'] + data2['Relative Strength'])/2)
df.insert(1, 'Adj Close',(data1['Adj Close'] + data2['Adj Close'])/2)
df.insert(1, 'Volume Change', (data1['Volume Change'] + data2['Volume Change'])/2)
df.insert(1, 'Price Close',(data1['Close'] + data2['Close'])/2)

# Monthly Calculations
df.groupby(['Year', 'Month']).mean()

# CSV
df.to_csv('monthlyAvg.csv')
