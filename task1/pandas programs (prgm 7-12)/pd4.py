import pandas as pd
df = pd.read_csv(r'C:\Users\Shubham Nanda\data\Desktop\diamonds.csv')
print("Number of rows and columns:")
print(df.shape)
print("no. of rows and columns after dropping those rows where values are missing:")
print(df.dropna(how='any').shape)