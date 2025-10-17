import pandas as pd
data = pd.read_csv("AB_NYC_2019.csv")
# data.head()

# data.isna().sum()

# df1 = data.drop("last_review", axis=1)
# print(df1.shape)

# df2 = data.dropna()
# print(df2.shape)

# df3 = data.copy()

# mean_value = df3['reviews_per_month'].mean()
# df3['reviews_per_month'].fillna(mean_value, inplace=True)

# df3.isna().sum()

# df3["last_review"].fillna(df3["last_review"].value_counts().index[0], inplace=True)
# print(df3["last_review"])
# df3["last_review"].fillna("Not Reviewed", inplace=True)
# df3["host_name"].fillna("Unknown", inplace=True)
# df3["reviews_per_month"].interpolate(inplace=True)

# data.duplicated().sum()






# todo : Dealing with Duplicate Data

# print(data.duplicated().sum())

# print(data[data.duplicated()])

# print(data[data.duplicated(keep="first")])

# print(data[data.duplicated(keep="last")])

# print(data[data.duplicated(keep=False)])

# data = data.drop_duplicates()

# print(data)


print('hello')