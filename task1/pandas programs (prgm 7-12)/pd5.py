import pandas as pd
df = pd.read_csv(r'C:\Users\Shubham Nanda\data\Desktop\diamonds.csv')
print("total no. of duplicate rows in diamonds dataframe")
print(df.duplicated().sum())