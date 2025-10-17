import pandas as pd
import seaborn as sns

df = pd.read_csv("AB_NYC_2019.csv")

#Retrieves the dimensions (rows, columns) of DataFrame df
# Description: Returns a tuple representing the number of rows and columns in DataFrame df.
# print(df.shape)

# Provides a summary of DataFrame df
# Description: Displays information about the DataFrame df, including the data types of each column and the number of non-null values.
# df.info()

# Counts the missing values in each column of DataFrame df
# Description: Computes the number of missing values (NaN) in each column of DataFrame df and returns a Series containing the counts.
# print(df.isna().sum())

# Generates descriptive statistics for DataFrame df
# Description: Computes summary statistics (count, mean, std, min, 25%, 50%, 75%, max) for numerical columns in DataFrame df.
# print(df.describe())

# print(df.duplicated().sum())

# Counts the number of unique values in each column of DataFrame df
# Description: Computes the number of unique values in each column of DataFrame df and returns a Series containing the counts.
# print(df.nunique())

# Retrieves unique values from the "neighbourhood_group" column of DataFrame df
# Description: Returns an array containing all unique values present in the "neighbourhood_group" column of DataFrame df.
# print(df["neighbourhood_group"].unique())

# Creates a box plot of the "price" column using Seaborn
# Description: Visualizes the distribution of values in the "price" column of DataFrame df using a box plot, which displays the median, quartiles, and outliers.
# print(sns.boxplot(df["price"]))

# print(sns.boxplot(df["availability_365"]))