import pandas as pd

# Read the dataset from a CSV file
data = pd.read_csv("googleplaystore.csv")

# print(data.head(10))

print(data.columns)

print(data.shape)

print(type(data))