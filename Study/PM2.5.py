import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
from scipy import stats
import seaborn as sb

df=pd.read_csv(r'C:\Users\User\Downloads\PM25.csv')

# df.plot(x='DEWP', y='pm25', kind='line')
# print(plt.show())

# df.plot(x='TEMP', y='pm25', kind='line')
# print(plt.show())

# X=df['DEWP']
# y=df['pm25']
# slope, intercept, r, p, std_err = stats.linregress(X,y)

# def myfunc(x):
#     return slope*x+intercept

# mymodel=list(map(myfunc, X))
# plt.scatter(X,y)
# plt.plot(X,mymodel,color='cyan', label='Fitted line')
# plt.xlabel('Dew point')
# plt.ylabel('pm25')
# plt.show()
# print('Slope = '+str(slope))
# print('Intercept = '+str(intercept))
# print('Relationship is '+str(r))

# def predictPM25(x):
#     return slope*x+intercept
# print('At the dew point is 10, PM2.5 is '+str(predictPM25(10)))
X=df['TEMP']
y=df['pm25']
slope, intercept, r, p, std_err = stats.linregress(X,y)

def myfunc(x):
    return slope*x+intercept

mymodel=list(map(myfunc, X))
plt.scatter(X,y, color='orange')
plt.plot(X, mymodel, color='cyan', label='Fitted line')
plt.xlabel('Temperator', color='red')
plt.ylabel('PM2.5', color='grey')
# plt.show()
print('Slope = '+str(slope))
print('Intercept = '+str(intercept))
print('Relationship is '+str(r))
