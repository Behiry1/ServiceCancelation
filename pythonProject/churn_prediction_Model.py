# -*- coding: utf-8 -*-
"""Churn_prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FcEICA7PHqLw0fp-NBrsmfB9ODdpqkTr
"""

import pandas as pd
import numpy as np
#data visualzation libraries
import matplotlib.pyplot as plt
import seaborn as sns
pd.set_option("display.max_columns", 40)

df=pd.read_csv("CustomersDataset.csv")

df.head(5)

"""##To Drop Customer ID as it is not relevant and wanted"""

df=df.drop('customerID',axis=1)

df.shape

df.info()

for i in df.columns:
  print(i)
  print(df[i].unique())
  print(df[i].dtype)
  print("-------------------------------------------------------------")

"""### we have problem here with total charges data type"""

df['TotalCharges']=df['TotalCharges'].replace(" ",np.nan)

df['TotalCharges'].isnull().sum()

"""### So now we have to deal with total charges nulls"""

plt.figure()
sns.distplot(df['TotalCharges'])
plt.show()

from sklearn.impute import KNNImputer
imputer = KNNImputer()
df['TotalCharges']=imputer.fit_transform(df[['TotalCharges']])
df['TotalCharges'].isnull().sum()

plt.figure()
sns.distplot(df['TotalCharges'])
plt.show()

"""###Split Data according to Data Type"""

df_cat=df.select_dtypes(include=['object'])
df_cat
df_num=df.select_dtypes(include=['int64','float64'])

df_cat.info()

df_num.info()

"""# Analysis of Categorical """

for i in df_cat.columns:
    plt.figure()
    plt.xticks(rotation=45)
    sns.countplot(x=i,data= df_cat,hue='Churn')
    plt.show()

"""1.   We noticed that Gender does not make a big diffrence
2.   We noticed that phoneService doesnot make a big diffrence too

#Label encoding & chi2
"""

from sklearn.preprocessing import LabelEncoder
Le=LabelEncoder()
for i in df_cat.columns:
  df_cat[i]=Le.fit_transform(df_cat[i])

X=df_cat[df_cat.columns.drop(['Churn'])]
y=df_cat['Churn']

df.head(5)

from sklearn.feature_selection import chi2
chi2,p=chi2(X,y)
chi2=pd.DataFrame(chi2,index=df_cat.columns.drop(['Churn']))
p=pd.DataFrame(p,index=df_cat.columns.drop(['Churn']))

p[p[0]<0.05].index

chi2.sort_values(0,ascending=False)

df_cat.drop(['PhoneService','gender'],axis=1,inplace=True)

"""###Numerical Features"""

df_num

plt.figure()
sns.heatmap(df_num.corr(),annot=True)
plt.show()

#try to drop tenure and test accurracy

"""##Feature Extraction"""

df=pd.concat([df_num,df_cat],axis=1)
df.head()
df.info()

payontime=list() #
for i in range(0,7043):
    if (df.iloc[i]['TotalCharges']/df.iloc[i]['tenure']>=df.iloc[i]['MonthlyCharges']):
        payontime.append(1) 
    else:
        payontime.append(0)

df['POT']=pd.Series(payontime)

df.info()

"""##Data Scaling """

col=df.columns

from sklearn.preprocessing import MinMaxScaler
MMsc=MinMaxScaler()
df=pd.DataFrame(MMsc.fit_transform(df.drop('Churn',axis=1)),columns=col.drop('Churn'))
df

col

"""##Train Test Split"""

from sklearn.model_selection import train_test_split

X_train , X_test , y_train , y_test =train_test_split(X,y,test_size=0.3,random_state=2002) 

X_train.shape,y_train.shape,X_test.shape,y_test.shape

"""## Logestic regression"""

from sklearn.linear_model import LogisticRegression
lr=LogisticRegression(random_state=2002)
lr.fit(X_train,y_train)
y_pred=lr.predict(X_test)

from sklearn.metrics import confusion_matrix
confusion_matrix(y_test,y_pred)

from sklearn.metrics import accuracy_score,precision_score ,recall_score
print("Accuracy" , accuracy_score(y_pred,y_test))
print("precision",precision_score(y_pred,y_test))
print("recall",recall_score(y_pred,y_test))

"""## SVM"""

from sklearn.svm import SVC
svm=SVC(random_state=2002)
svm.fit(X_train,y_train)
y_pred=svm.predict(X_test)

from sklearn.metrics import confusion_matrix
confusion_matrix(y_test,y_pred)

from sklearn.metrics import accuracy_score,precision_score ,recall_score
print("Accuracy" , accuracy_score(y_pred,y_test))
print("precision",precision_score(y_pred,y_test))
print("recall",recall_score(y_pred,y_test))

"""## Decision Tree"""

from sklearn.tree import DecisionTreeClassifier
dt=DecisionTreeClassifier(random_state=2002,criterion='entropy',max_leaf_nodes=9)
dt.fit(X_train,y_train)
y_pred=dt.predict(X_test)

from sklearn.metrics import confusion_matrix
confusion_matrix(y_test,y_pred)

from sklearn.metrics import accuracy_score,precision_score ,recall_score
print("Accuracy" , accuracy_score(y_pred,y_test))
print("precision",precision_score(y_pred,y_test))
print("recall",recall_score(y_pred,y_test))

"""## Save AI Model"""

import pickle
filename = 'Logistic Regression.sav'
pickle.dump(lr, open(filename, 'wb'))

filename = 'SVM.sav'
pickle.dump(svm, open(filename, 'wb'))

filename = 'Decision Tree.sav'
pickle.dump(dt, open(filename, 'wb'))

filename = 'MinMaxScale.sav'
pickle.dump(MMsc, open(filename, 'wb'))

