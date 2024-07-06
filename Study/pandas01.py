import pandas as pd
d={'col':[1,2,3,4,7], 'col2': [4,5,6,9,5], 'col3':[7,8,12,1,11]}

df=pd.DataFrame(data=d)
print(df)

print(df.shape)
print(df.shape[0])
print(df.shape[1])
df.info()
df.head()
df.tail()
print(df.describe()) #stat