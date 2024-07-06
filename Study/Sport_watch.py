import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns

df = pd.read_csv(r'C:\Users\User\Downloads\sport_watch.csv')
df.dropna(inplace=True)
max_pulse=df['Max_Pulse']
percentile10=np.percentile(max_pulse, 10)
percentile80=np.percentile(max_pulse, 80)
std=np.std(df)
df.plot(x='Average_Pulse', y='Max_Pulse', kind='scatter')
# plt.show()

#r=np.corrcoef(df['Average_Pulse'], df['Calorie_Burnage'])
#slope, intercept, r, p, str_err= stats.linregress(df['Average_Pulse'], df['Calorie_Burnage'])
#print(r)
#x=1 หา slope but x=0 หา intercept

corr_matrix=round(df.corr(), 2)
axis=sns.heatmap(corr_matrix, vmin=-1, vmax=1, center=0, cmap="Blues", square=True, annot=True)
axis.set_title('Correlation Heatmap', fontdict={'fontsize':12}, pad=12)
plt.show()

# print(df)
# print(df.describe())
# print(df.isnull())
# print(max_pulse)
# print(percentile10)
# print(percentile80)
# print(std)