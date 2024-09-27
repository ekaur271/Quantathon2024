from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import pandas as pd

# Assuming df is your DataFrame and it's already loaded
# Let's say df has features: 'feature1', 'feature2', 'feature3', and the target: 'target'


# X = pd.DataFrame[['Year', 'Price Close', 'Volume Change', 'Adj CLose', 'Relative Strength', 'Price Ratio', 'Price Momentum', 'Price Change', 
# 'Daily Price Volatility', 'Daily Price Range', 'Month', 'Date']]  # Features

X = pd.DataFrame[[pd.read_csv("MonthlyAvg.csv")]]

# y = pd.DataFrame['Price Close']  # Target variable

# Splitting the dataset into training and testing sets
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# data = pd.read_csv("monthlyAvg.csv")
# train_set, test_set= train_test_split(X, y, test_size=0.2, random_state=42)

# # Lets train on 2014 - 2018 and test on 2019 to 2024
# # train_set = pd.DataFrame()
# # train_set = data.drop(data[data['Year'] > 2018].index)

# # test_set = pd.DataFrame()
# # test_set = data.drop(data[data['Year'] < 2019].index)


# # Creating the GBM model
# gbm_model = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1,
#                                       max_depth=3, random_state=42)

# # Training the model
# # gbm_model.fit(X_train, y_train)
# gbm_model.fit(train_set)

# # Making predictions
# # y_pred = gbm_model.predict(X_test)
# y_pred = gbm_model.predict(test_set)

# # Evaluating the model
# # mse = mean_squared_error(y_test, y_pred)
# mse = mean_squared_error(test_Set, y_pred)
# print(f"Mean Squared Error: {mse}")