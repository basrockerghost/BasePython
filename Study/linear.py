import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df=pd.read_csv(r'C:\Users\User\Downloads\sport_watch.csv')
# print(df.to_string())

df.dropna(inplace=True)
# print(df.to_string())

df.plot(x='Average_Pulse', y='Calorie_Burnage', kind='line')
plt.ylim(ymin=0)
plt.xlim(xmin=0)
# print(plt.show())

def getslope(x1, x2, y1, y2):
    s = (y2-y1)/(x2-x1)
    return s
print(getslope(80, 90, 240, 260))

def getY(x1, x2, y1, y2): #Intercept
    slope = getslope(x1, x2, y1, y2)
    y=-x1*slope+y1
    return y
print(getslope(80, 90, 240, 260))
print(getY(80, 90, 240, 260))

x=df['Average_Pulse']
y=df['Calorie_Burnage']
slope_intercept=np.polyfit(x, y, 1, full=True, cov=True)
print(slope_intercept)

def predict_calorie_burnage(x1, x2, y1, y2, z):
    return getslope(x1, x2, y1, y2)*z+getY(x1, x2, y1, y2)
print(predict_calorie_burnage(80, 90, 240, 260, 135))