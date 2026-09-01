#개요
#머신러닝
#지도학습
#비지도학습
#회귀 분류, 특징, 레이블, 훈련:테스트
#fit, predict
#평가

#전처리
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler, OrdinalEncoder

data = fetch_california_housing()

X = data.data
y = data.target

X = pd.DataFrame(X , columns=data.feature_names)
y = pd.DataFrame(y , columns=["target"])

# DataFrame 으로 만들어서 현재 경로에 california_housing.csv 이름의 파일로 저장

df = X
df = X.copy()
df["target"] = y
df.to_csv("california_housing.csv", index=False)

# 데이터 정보 확인 : 다음 2개 반드시 포함
# - shape
# - describe()
df.describe().T.to_csv("california_housing_desc.csv", index=False)
#   - 칼럼별 결측치 갯수 파악할 것
print(df.isna().sum())


# - 데이터 탐색
#   - 가격의 분포를 히스토그램으로 확인
df.hist(figsize=(12,10),grid = False, bins = 20)
plt.show()

sns.heatmap(df.corr(), annot=True, cmap = "coolwarm")
plt.show()

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
pipeline = make_pipeline(StandardScaler(), LinearRegression())
pipeline.fit(X_train, y_train)
#파이프라인을써야 데이터 누수를 막는데
# scaler = StandardScaler()
# X_train_s= scaler.fit(X_train)
# X_test_s = scaler.transform(X_test)
#
# m = LinearRegression()
# m.fit(X_train_s, y_train)
y_pred = pipeline.predict(X_test)

r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print("r2 : ", r2)
print("mae : ", mae)
print("rmse : ", rmse)