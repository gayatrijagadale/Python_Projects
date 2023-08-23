# -*- coding: utf-8 -*-
"""IRIS FLOWER CLASSIFICATION.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1l06mExcvstrR5C4na16BhzZmSab9LS71

#**Task 2 - IRIS FLOWER CLASSIFICATION**#

Importing the Dependencies
"""

import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('/content/Iris.csv')

data.head()

data = data.drop(columns = ['Id'])
data.head()

data.describe()

data.info()

data['Species'].value_counts()

#Data preprocessing
data.isnull().sum()

# Exploratory Data Analysis
data['SepalLengthCm'].hist()

data['SepalWidthCm'].hist()

data['PetalLengthCm'].hist()

data['PetalWidthCm'].hist()

# Scatterplot
colors =['red','orange','black']
species=['Iris-setosa','Iris-versicolor','Iris-virginica']

for i in range(3):
  x= data[data['Species']== species[i]]
  plt.scatter(x['SepalLengthCm'],x['SepalWidthCm'], c=colors[i],label=species[i])
  plt.xlabel('Sepal Length')
  plt.xlabel('Sepal Width')
  plt.legend()

for i in range(3):
  x= data[data['Species']== species[i]]
  plt.scatter(x['PetalLengthCm'],x['PetalWidthCm'], c=colors[i],label=species[i])
  plt.xlabel('Petal Length')
  plt.xlabel('Petal Width')
  plt.legend()

for i in range(3):
  x= data[data['Species']== species[i]]
  plt.scatter(x['SepalLengthCm'],x['PetalLengthCm'], c=colors[i],label=species[i])
  plt.xlabel('Sepal Length')
  plt.xlabel('Petal Length')
  plt.legend()

for i in range(3):
  x= data[data['Species']== species[i]]
  plt.scatter(x['SepalWidthCm'],x['PetalWidthCm'], c=colors[i],label=species[i])
  plt.xlabel('Sepal Width')
  plt.xlabel('Petal Width')
  plt.legend()

# Correlation Matrix 'Showing correlation coefficient btw variable in form of table'
data.corr()

corr = data.corr()
fig , ax = plt.subplots(figsize=(5,4))
sns.heatmap(corr, annot=True, ax=ax, cmap='coolwarm')

# Label Encoder
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()

data['Species'] = le.fit_transform(data['Species'])
data.head()

# Model Training
from sklearn.model_selection import train_test_split
x=data.drop(columns=['Species'], axis=1)
y=data['Species']
X_train,X_test,Y_train,Y_test=train_test_split(X,y,test_size=0.38, random_state=2529)

# Logistic Regression
from sklearn.linear_model import LogisticRegression
model = LogisticRegression(max_iter=500)

model.fit(X_train,y_train)

# print metric to get performance
print('Accuracy: ',model.score(X_test,y_test)*100)

# knn - knearest neighbour
from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier()

model.fit(X_train,y_train)

print('Accuracy: ',model.score(X_test,y_test)*100)

