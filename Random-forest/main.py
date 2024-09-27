#pip install -U scikit-learn
# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestRegressor
# from sklearn.metrics import mean_squared_error

# # Assuming df is your DataFrame containing the data
# # Select features and target variable
# X = df[['feature1', 'feature2', 'feature3']]  # Replace with your actual feature columns
# y = df['Close']  # Assuming we're predicting the closing price

# # Split the data into training and testing sets
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# # Create the Random Forest model
# rf_model = RandomForestRegressor(n_estimators=100, random_state=0)
# rf_model.fit(X_train, y_train)

# # Make predictions
# y_pred = rf_model.predict(X_test)

# # Calculate Mean Squared Error
# mse = mean_squared_error(y_test, y_pred)
# print("Mean Squared Error: ", mse)

import pandas as pd
 
# creating a data frame
df_crude = pd.read_csv("CLF_data.csv")

df_delta = pd.read_csv("DAL_data.csv")

df_crude = df_crude.rename(columns={'Open': 'COpen', 'High': 'CHigh', 'Low': 'CLow', 'Adj Close': 'CAdj Close', 'Volume': 'CVolume'})
df_delta = df_delta.rename(columns={'Open': 'DOpen', 'High': 'DHigh', 'Low': 'DLow', 'Adj Close': 'DAdj Close', 'Volume': 'DVolume'})

df = pd.merge(df_crude, df_delta, on='Date', how='inner')

df = df.drop_duplicates(subset=['Date'], keep='first')
print(len(df))

df.to_csv('Combined_Data.csv')
