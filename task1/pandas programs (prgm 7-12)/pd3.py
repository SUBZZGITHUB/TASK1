import pandas as pd
df=pd.read_csv(r'C:\Users\Shubham Nanda\data\Desktop\diamonds.csv')
print("count, minimum, maximum price for each cut of diamonds DataFrame.")
print(df.groupby('cut').price.agg(['count', 'min', 'max']))
