# -*- coding: utf-8 -*-
"""Project.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1i2Q3mHAHP9im_xw1sqmL_tqezzVVzO46
"""





# Importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv('Heart_Attack_Risk_Levels_Dataset.csv')

# Remove heart rate outliers
df = df[df['Heart rate'] < 200]  # Remove absurd heart rates >200

# Label encode categorical variables
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
df['Result'] = le.fit_transform(df['Result'])
df['Risk_Level'] = le.fit_transform(df['Risk_Level'])
df['Recommendation'] = le.fit_transform(df['Recommendation'])

# Final look
print(df.head())

#Hypothesis Test
from scipy.stats import f_oneway, ttest_ind

# ANOVA
groups = [group['Blood sugar'].values for name, group in df.groupby('Risk_Level')]
anova_result = f_oneway(*groups)
print('ANOVA Result:', anova_result)

# T-test
pos = df[df['Result'] == 1]['CK-MB']
neg = df[df['Result'] == 0]['CK-MB']
ttest_result = ttest_ind(pos, neg)
print('T-Test Result:', ttest_result)

#Probability and Normal Distribution

import scipy.stats as stats

# QQ plot
for col in ['Age', 'Heart rate', 'Blood sugar']:
    stats.probplot(df[col], dist="norm", plot=plt)
    plt.title(f'QQ plot for {col}')
    plt.show()

#Exploratory Data Analysis
# Histograms
df.hist(figsize=(15,10))
plt.tight_layout()
plt.show()

# Boxplot for outliers
plt.figure(figsize=(12,6))
sns.boxplot(data=df)
plt.xticks(rotation=90)
plt.show()

# Correlation heatmap
plt.figure(figsize=(10,8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.show()

#Linear regression
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

y = df['CK-MB']
X = df[['Age', 'Heart rate', 'Blood sugar']]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

print('Score:', model.score(X_test, y_test))

#Logistic Regression
from sklearn.linear_model import LogisticRegression

y = df['Result']
X = df[['Age', 'Heart rate', 'Blood sugar']]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

logreg = LogisticRegression()
logreg.fit(X_train, y_train)

print('Accuracy:', logreg.score(X_test, y_test))

#Clustering(Kmean)
from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=3)
kmeans.fit(df[['Age', 'Heart rate', 'Blood sugar']])

df['Cluster'] = kmeans.labels_

from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=3, random_state=42)
df['Cluster'] = kmeans.fit_predict(X_scaled)

# Plot clusters
plt.scatter(X_pca[:,0], X_pca[:,1], c=df['Cluster'], cmap='viridis')
plt.title('KMeans Clusters')
plt.show()

#Decision Tree
from sklearn.tree import DecisionTreeClassifier

tree = DecisionTreeClassifier()
tree.fit(X_train, y_train)

print('Accuracy:', tree.score(X_test, y_test))

#Ramdom Forest
from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier()
rf.fit(X_train, y_train)

print('Accuracy:', rf.score(X_test, y_test))

#Support Vector Machine
from sklearn.svm import SVC

svm = SVC()
svm.fit(X_train, y_train)

print('Accuracy:', svm.score(X_test, y_test))

#Adaboost
from sklearn.ensemble import AdaBoostClassifier

ada = AdaBoostClassifier()
ada.fit(X_train, y_train)

print('Accuracy:', ada.score(X_test, y_test))

import pickle

# Example: Save your model
pickle.dump(model, open('Project.pkl', 'wb'))

# To load it again later:
model = pickle.load(open('final_model.pkl', 'rb'))
