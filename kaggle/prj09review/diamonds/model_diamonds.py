import matplotlib.dviread
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.constants import carat
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score, r2_score
from sklearn.model_selection import train_test_split

plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False

df = sns.load_dataset("diamonds")
df.to_csv("diamonds.csv")

#전처리
#값이0인거 제거
# 전처리 (한 줄 작성)
df = df[(df['x'] > 0) & (df['y'] > 0) & (df['z'] > 0)]

#분리
features = ["carat"]
X = df[features]
y = df["price"]
X_train, X_test, y_train, y_test = train_test_split(
    X,y,test_size=0.2,random_state=42,
)
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)
# #학습
m = LinearRegression()
m.fit(X_train, y_train)

#예측
y_pred = m.predict(X_test)


#평가
acc = accuracy_score(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(acc)
print(r2)