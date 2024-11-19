import pandas as pd
import numpy as np

# series 
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)

# dataframe
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 24, 35, 32],
    'City': ['New York', 'Paris', 'Berlin', 'London']
}
df = pd.DataFrame(data)
print(df)

# Data Exploration
df = pd.read_csv('yourfile.csv')
print(df.head())

print(df.head())  # View first 5 rows
print(df.tail())  # View last 5 rows
print(df.info())  # View info about the DataFrame
print(df.describe())  # Get summary statistics

print(df['Name'])  # Select a single column
print(df[['Name', 'Age']])  # Select multiple columns
print(df.iloc[0])  # Select a row by position
print(df.loc[0])  # Select a row by label

df_filtered = df[df['Age'] > 30]
print(df_filtered)

## Modidy Data, add or remove columns

df['Country'] = ['USA', 'France', 'Germany', 'UK']
print(df)

# df.drop(['Country'], axis=1, inplace=True)
# print(df)

## Handle missing data

print(df.isnull().sum())
df.fillna(0, inplace=True)
print(df)
df.dropna(inplace=True)
print(df)


## Group Data

# grouped_df = df.groupby('City').mean()
# print(grouped_df)

df1 = pd.DataFrame({
    'key': ['A', 'B', 'C', 'D'],
    'value': [1, 2, 3, 4]
})

df2 = pd.DataFrame({
    'key': ['B', 'D', 'E', 'F'],
    'value': [5, 6, 7, 8]
})

merged_df = pd.merge(df1, df2, on='key', how='inner')
print(merged_df)


