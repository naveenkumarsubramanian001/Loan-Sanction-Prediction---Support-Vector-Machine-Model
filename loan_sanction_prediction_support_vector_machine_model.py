# -*- coding: utf-8 -*-
"""Loan Sanction Prediction - Support Vector Machine Model.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1uyx-CAnU5xLRb8x8KK6ne7nQcA2AC3Mc
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder

loan_data = pd.read_csv('/content/loan_data.csv')

loan_data.head()

loan_data.shape

loan_data.isnull().sum()

loan_data.dropna(inplace=True)

loan_data.shape

loan_data.describe()

label =LabelEncoder()

loan_data['Gender'] = label.fit_transform(loan_data['Gender'])
loan_data['Married'] = label.fit_transform(loan_data['Married'])
loan_data['Education'] = label.fit_transform(loan_data['Education'])
loan_data['Self_Employed'] = label.fit_transform(loan_data['Self_Employed'])
loan_data['Property_Area'] = label.fit_transform(loan_data['Property_Area'])
loan_data['Loan_Status'] = label.fit_transform(loan_data['Loan_Status'])
loan_data.head()

loan_data['Dependents'].value_counts()

loan_data['Dependents'].replace('3+',3,inplace=True)

loan_data.head()

loan_data['Loan_Status'].value_counts()

X = loan_data.drop(columns=['Loan_ID','Loan_Status'],axis=1)
Y = loan_data['Loan_Status']

X_train , X_test , Y_train , Y_test = train_test_split(X,Y,test_size=0.2,stratify=Y)

model = SVC(kernel='linear')

model.fit(X_train,Y_train)

tain_pred = model.predict(X_train)
test_pred = model.predict(X_test)

train_score = accuracy_score(Y_train,tain_pred)
test_score = accuracy_score(Y_test,test_pred)

print('train score : ',train_score)
print('test score : ',test_score)

report = classification_report(Y_test,test_pred)

print("The Classification Report is :", report)

print("The Confusion matrix is :",confusion_matrix(Y_test,test_pred))

