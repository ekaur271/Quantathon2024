import pandas as pd

df = pd.read_csv("monthlyAvg.csv")

print(df.Year.unique()) # 2014 - 2024

# Lets train on 2014 - 2018 and test on 2019 to 2024
train_set = pd.DataFrame()
train_set = df.drop(df[df['Year'] > 2018].index)
print(train_set.Year.unique()) # 2014 - 2024

test_set = pd.DataFrame()
test_set = df.drop(df[df['Year'] < 2019].index)
print(test_set.Year.unique()) # 2014 - 2024