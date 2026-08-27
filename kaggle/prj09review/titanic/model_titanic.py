from unittest import result

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split

plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False


#데이터
df = pd.read_csv("train.csv")

# 전처리 (결측치 , 중복제거 , 인코딩 , 파생변수)
#결측치
df ["Age"] = df ["Age"].fillna(df ["Age"].median())
df ["Embarked"] = df ["Embarked"].fillna(df ["Embarked"].mode()[0])
df ["Fare"] = df ["Fare"].fillna(df ["Fare"].median())
#인코딩
df ["Sex"] = df ["Sex"].map({"male":0,"female":1})
df ["Embarked"] = df ["Embarked"].map({"S":0,"C":1,"Q":2})
#파생변수
df ["FamilySize"] = df ["Parch"] + df ["SibSp"]+1

#모델(데이터 분리, 학습, 예측, 평가)
features = ["Age" , "Embarked" , "Fare" , "Sex" , "FamilySize" , "Pclass"]
X = df[features]
y = df["Survived"]
X_train, X_test, y_train,y_test = train_test_split(
    X,y,test_size=0.2,random_state=42, stratify=y
)

#모델 학습
m = LogisticRegression()
m.fit(X_train,y_train)
#예측
y_pred = m.predict(X_test)
acc_score = accuracy_score(y_test, y_pred)
print(acc_score)
#계수확인
sr = pd.Series(m.coef_[0], index = features).sort_values(ascending=False)
print(sr)

result = classification_report(y_test,y_pred, target_names=["사망","생존"])
print(result)
#혼동행렬
# cm = confusion_matrix(y_test,y_pred)
# plt.figure(figsize = (8,6))
# sns.heatmap(cm
#             , annot=True, cmap="Blues"
#             , xticklabels=["사망예측", "생존예측"]
#             , yticklabels=["사망실제", "생존실제"])
# plt.show()