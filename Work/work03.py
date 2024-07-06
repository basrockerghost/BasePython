import pandas as pd
import numpy as np

df = pd.read_csv(r'C:\Users\User\Downloads\titanic.csv')

df1 = df.info()
df2 = df['age'].fillna(np.mean(df['age']))
a = df['embarked'].mode()[0]
df3 = df['embarked'].fillna(a)


print(df.isnull().sum())
# print(df)
print(df1)
print(df2)
print(df3)