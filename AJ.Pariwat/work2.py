import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

data=pd.read_csv(r'C:\Users\User\Downloads\diabetes_dataset - diabetes_dataset.csv.csv')
# print(data)
# data.info()
X=data[['Age', 'BMI', 'Glucose_Level']]
y=data['Diabetes_Status']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

logistic_regression_model = LogisticRegression()
logistic_regression_model.fit(X_train, y_train)
y_pred = logistic_regression_model.predict(X_test)
accurary = accuracy_score(y_test, y_pred)
print("Accurary : ", accurary)
print(classification_report(y_test, y_pred))