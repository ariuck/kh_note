import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split

plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False

# 데이터 준비
df = sns.load_dataset("penguins")


#데이터 전처리(결측치, 중복, 인코딩, 스케일, 파생칼럼
df = df.dropna()

#학습용 시험용 분류
features = ['bill_length_mm','bill_depth_mm','flipper_length_mm','body_mass_g']
X = df[features]
y = df["species"]


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)
#학습
m = LogisticRegression(max_iter=5000)
m.fit(X_train,y_train)
#예측
y_pred = m.predict(X_test)

#평가
acc_score = accuracy_score(y_test,y_pred)
print("acc_score : ",acc_score)
# #혼동행렬
# cm = confusion_matrix(y_test,y_pred)
# print(cm)
# plt.figure(figsize=(8,6))
# sns.heatmap(
#     cm
#     , annot=True
#     , cmap="Blues"
#     , xticklabels=["Adelie" , "Chintrap" , "Gentoo"]
#     , yticklabels=["Adelie" , "Chintrap" , "Gentoo"]
# )
# plt.xlabel("실제")
# plt.ylabel("예측")
# plt.show()

print(m.coef_)
cr = classification_report(y_test,y_pred)
print("cr : ",cr)