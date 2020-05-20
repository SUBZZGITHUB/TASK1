import pandas as pd
pd.set_option('display.max_rows', 50)
pd.set_option('display.max_columns', 50)
df = pd.read_csv(r'C:\Users\Shubham Nanda\data\Desktop\diamonds.csv')
print("First 5 rows:")
print(df.head())