#전처리
'''
결측
중복
인코딩
파생변수
시계열
스케일
'''

from pandas.core.interchange import column
from sklearn.datasets import load_iris
from sklearn.impute import SimpleImputer
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler, OrdinalEncoder

# # #결측치 처리
# # df = pd.DataFrame({
# #     "age": [20, 30, np.nan, 40, 50],
# #     "score": [100, np.nan, 80, 70, np.nan]
# # })
# #
# # # df["age"] = df["age"].fillna(df["age"].mean())
# # # df["score"] = df["score"].fillna(df["score"].median())
# #
# # imputer = SimpleImputer(strategy="median").set_output(transform="pandas")
# # result = imputer.fit_transform(df)
# # print(result)
# # print(type(result))
#
# #스케일링
# X = np.array([[1.0, 100.0],
#               [2.0, 300.0],
#               [3.0, 500.0],
#               [4.0, 700.0]])
#
# scaler = StandardScaler()
# X_scaled = scaler.fit_transform(X)
# print(X_scaled)

#범주형 인코딩(순위 없는거 원 핫 인코딩, 순위 잇는거 map())

# 범주형 인코딩(순위x)
# df = pd.DataFrame({"color": ["red", "green", "blue", "green"]})
# result =pd.get_dummies(df,columns = ['color'],drop_first = True)
# print(result)

# #범주형 인코딩(순위o)
# df = pd.DataFrame({
#     "size" : ["소","대","중","소"],
#     "grade" : ["Bronze", "Gold", "Silver", "Bronze"]})
# # result = df["size"].map({"소": 1, "중": 2, "대": 3})
#
# enc = OrdinalEncoder(categories =[
#                     ["소","중","대"],
#                     ["Bronze","Silver","Gold"],
#                      ])
# df[["size","grade"]]= enc.fit_transform(df[["size","grade"]])
# print(df)

#파생칼럼, 중복제거, 시계열 인덱싱


#=====누수없이 전처리
#데이터 준비
X,y = load_iris(return_X_y=True)

X_train, X_test, y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=42)

#전처리
scaler = StandardScaler()
# X_train = scaler.fit_transform(X_train)
# X_test = scaler.transform(X_test)

#모델
m = KNeighborsClassifier(n_neighbors=3)

#파이프라인(전처리+모델)
pipe = make_pipeline(scaler,m)
#학습
pipe.fit(X_train,y_train)

#예측
y_pred = pipe.predict(X_test)

#평가

print(y_pred)

acc = accuracy_score(y_test,y_pred)
print(acc)