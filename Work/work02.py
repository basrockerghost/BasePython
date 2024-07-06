import pandas as pd
import numpy as np
import seaborn as sb

df = pd.read_csv(r'C:\Users\User\Downloads\dirtydata.csv')

# df1 = df.info()
# df2 = df.isnull()
df3 = df['Date'].fillna(pd.Timestamp(df['Date']))
# df4 = df['Calories'].fillna(np.mean(df['Calories']))


# x = df['Date'].median()[0]
# df3 = df['Date'].fillna(x)
y = df['Calories'].mean()
df4 = df['Calories'].fillna(y)


print(df)
print(df['Duration'].value_counts())
# print(df1)
# print(df2)
# print(df3)
print(df4)