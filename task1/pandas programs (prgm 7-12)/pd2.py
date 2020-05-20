import pandas as pd
df=pd.read_csv(r'C:\Users\Shubham Nanda\data\Desktop\diamonds.csv')
srs=input("input a series from the diamonds data frame")
print(df[srs])
