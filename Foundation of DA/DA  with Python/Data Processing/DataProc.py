import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
# df = pd.read_csv("googleplaystore.csv")

# # print(df.isnull().sum())
# print(df.shape)

# df = df.dropna()
# # print(df.isnull().sum())

# print(df.shape)


# todo : Data analysis

# df.head()

# print("Average rating of these apps:", float(str(int(df['Rating'].sum()) / len(df['Rating']))[:4]))



# todo : DA Categorical
# print(df['Category'].unique()) # * Print The Name of Unique Values

# n=df['Category'].nunique() # * Print the number of unique values
# print("There are a total of ",n," unique values in Category columns")


# c = 0
# for i in df['Category']:
#     if(i == 'ART_AND_DESIGN'):
#         c += 1
# print("There are total", c, "applications in ART_AND_DESIGN")


# print(df['Type'].unique())


# f = 0
# for i in df['Type']:
#     if(i == 'Free'):
#         f += 1
# print("There are total", f, "free and", end=" ")

# p = 0
# for i in df['Type']:
#     if(i == 'Paid'):
#         p += 1
# print("and", p, "paid applications")


# for i in df['Content Rating'].unique():
    # print(i)
    
    
    
# todo : DA Categorical

# categories = {}

# for name in df['Category'].unique():
#     ct = 0
#     for i in df['Category']:
#         if(i == name):
#             ct += 1
#     categories[name] = ct

# print(categories)


# types = {}

# for name in df['Type'].unique():
#     ct = 0
#     for i in df['Type']:
#         if(i == name):
#             ct += 1
#     types[name] = ct
    
# print(types)


# content_rating = {}

# for name in df['Content Rating'].unique():
#     ct = 0
#     for i in df['Content Rating']:
#         if(i == name):
#             ct += 1
#     content_rating[name] = ct
    
# print(content_rating)


# df['Reviews'].describe()



# todo : Automatic Categorial

# categories = {}

# for name in df['Category'].unique():
#     ct = 0
#     for i in df['Category']:
#         if(i == name):
#             ct += 1
#     categories[name] = ct
    
# # print(categories)
# for i in categories:
#     print(i, ":", categories[i])



# types = {}

# for name in df['Type'].unique():
#     ct = 0
#     for i in df['Type']:
#         if(i == name):
#             ct += 1
#     types[name] = ct
    
# print(types)



# content_rating = {}

# for name in df['Content Rating'].unique():
#     ct = 0
#     for i in df['Content Rating']:
#         if(i == name):
#             ct += 1
#     content_rating[name] = ct
    
# print(content_rating)



# print(df['Reviews'].describe())



# todo : Null Values Handling - Numeric

# df=pd.read_csv('Data.csv')
# print(df)


# print(df.dropna())


# imputer = SimpleImputer(missing_values=np.nan, strategy='most_frequent')

# imputer.fit(df.iloc[:, 1:3].values)
# df.iloc[:, 1:3] = imputer.transform(df.iloc[:, 1:3].values)
# OR 
# df.iloc[:, 1:3] = imputer.fit_transform(df.iloc[:, 1:3].values)

# print(df)




# todo : Null Values Handling - Categorical

# imputer = SimpleImputer(missing_values=np.nan, strategy='most_frequent')

# imputer.fit(df.iloc[:, :].values)

# df.iloc[:, :] = imputer.transform(df.iloc[:, :].values)

# print(df)


# todo : Null Value Handling on GooglePlaystore
# df=pd.read_csv("googleplaystore.csv")
# print(df.head())
# print(df.isnull().sum())

# impute = SimpleImputer(missing_values=np.nan, strategy='mean')

# impute.fit(df.iloc[:, 2:3].values)

# df.iloc[:, 2:3] = impute.transform(df.iloc[:, 2:3].values)
# print(df.iloc[:, 2:3])

# df=df.dropna()
# print(df.isnull().sum())

# print("Initial dataset size:", 10841)
# print("Final dataset size:", len(df))