import pandas as pd
import seaborn as sns
import numpy as np
df = pd.read_csv(r'C:\Users\User\Downloads\health_data.csv')


# df1= df.info()
# df2= df.isnull().sum()
# df3= df.dropna()
# df4= df.fillna(0)
# numpy style
# df5= df['Duration'].fillna(np.mean(df['Duration']))
# df5=df['Calorie_Burnage'].fillna(np.median(df['Calorie_Burnage']))
# seaborn style
x=df['Duration'].mode()[0]
df5=df['Duration'].fillna(x)

y=df['Calorie_Burnage'].median()
df6=df['Calorie_Burnage'].fillna(y)


print(df)
# print(df1)
# print(df2)
# print(df3)
# print(df4)
print(df5)
print(df6)