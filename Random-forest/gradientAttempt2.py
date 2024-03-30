# Import necessary libraries
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import pandas as pd

# Load your dataset (replace X and y with features and target variable)
X = pd.read_csv("monthlyAvg.csv")
#df = pd.DataFrame(data, columns=['Date'])
y = pd.DataFrame()
y = ['Price Close']  # Target variable

# Split data into training and testing sets
#train_set, test_set = train_test_split(X, y, test_size=0.2, random_state=42)

#Lets train on 2014 - 2018 and test on 2019 to 2024
data = pd.read_csv("monthlyAvg.csv")
train_set = pd.DataFrame()
train_set = data.drop(data[data['Year'] > 2018].index)

test_set = pd.DataFrame()
test_set = data.drop(data[data['Year'] < 2019].index)

# Initialize Gbm model
gbm_model = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)

# Train the model
gbm_model.fit(train_set)