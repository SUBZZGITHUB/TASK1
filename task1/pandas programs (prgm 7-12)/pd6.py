import pandas as pd
df = pd.read_csv(r'C:\Users\Shubham Nanda\data\Desktop\diamonds.csv')
print("Number of rows and columns:")
print(df.shape)
print("Sample 75% of diamonds DataFrame's rows without replacement:\n")
result = df.sample(frac=0.75, random_state=99)
print(result)
print("Remaining 25% of the rows:\n")
print(df.loc[~df.index.isin(result.index), :])