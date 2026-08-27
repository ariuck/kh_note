import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.interpolate import fitpack
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False

# 1. 데이터 불러오기
df = sns.load_dataset("tips")

# 2. 전처리 및 X, y 설정
#파생
df["tip_pct"] = df["tip"] / df["total_bill"] * 100

features = ['total_bill', 'size', 'tip_pct']

# X , y
X = df[features]
y = df["tip"]

# 학습용/테스트용 데이터 분리 (8:2 비율)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# print(X_train.shape)
# print(y_train.shape)
# print(X_test.shape)
# print(y_test.shape)

#학습
m=LinearRegression()
m.fit(X_train,y_train)

#예측
y_pred = m.predict(X_test)
print(y_pred)

#평가
#모델 점수
x = r2_score(y_test, y_pred)
print(x)
