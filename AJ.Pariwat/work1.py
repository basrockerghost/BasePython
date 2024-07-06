import numpy as np
from sklearn.linear_model import LinearRegression

#Define the data
x=np.array([1,2,3,4,5,6,7,8,9]).reshape(-1,1) #Reshape x to a 2D array
y=np.array([19.22,18.07,17.67,20.52,29.59,31.27,33.19,32.24,38.11])

#Create and train the linear regression model
model=LinearRegression()
model.fit(x,y)

#Predict a value for a new x
new_x=np.array([[10]]) #input a new value to predict
predicted_y=model.predict(new_x)

# print(f"Predicted value for x=10 : {predicted_y[0]:.2f}")

def myfunc():
    t=(10.51+2.44(3)+0.11(50))
    print(t)
myfunc()