# #지도학습
# import numpy as np
# from sklearn.datasets import load_breast_cancer, load_iris
# from sklearn.linear_model import LogisticRegression
# from sklearn.metrics import accuracy_score
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler
#
# =#===== 로지스틱 회귀 ========
# # return_X_y=True를 쓰면 처음부터 x y 불러 올 수 있음
# # X,y = load_breast_cancer(return_X_y=True)
# X,y = load_iris(return_X_y=True)
# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, test_size=0.2, random_state=42)
#
#
# scaler = StandardScaler()
# scaler.fit(X_train)
# X_train_s = scaler.transform(X_train)
# X_test_s = scaler.transform(X_test)
#
# m = LogisticRegression(max_iter=500)
# m.fit(X_train_s, y_train)
# y_pred = m.predict(X_test_s)
#
#
# acc_score = accuracy_score(y_test, y_pred)
# print("acc_score : ", acc_score)
#
# prob = m.predict_proba(X_test_s)
# print("prob : ", np.round(prob,3))
# print("prob",type(prob))
from sklearn.datasets import load_wine, load_iris, load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

# #=== KNN === : 학습단계에서 할게 없음 (lazy learning)
# import numpy as np
# from sklearn.datasets import load_wine
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.metrics import accuracy_score
#
# # 1. 데이터 로드
# X, y = load_wine(return_X_y=True)
#
# # 2. Train / Test 데이터 분할
# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, test_size=0.2, random_state=42
# )
#
# # 3. 데이터 스케일링 (KNN 알고리즘은 거리를 측정하므로 스케일링이 매우 중요합니다)
# scaler = StandardScaler()
# scaler.fit(X_train)
# X_train_s = scaler.transform(X_train)
# X_test_s = scaler.transform(X_test)
#
# # 4. KNN 모델 생성 및 학습
# m = KNeighborsClassifier(n_neighbors=5)  # 이웃 개수 지정 (기본값 5)
# m.fit(X_train_s, y_train)
#
# # 5. 예측 및 평가
# y_pred = m.predict(X_test_s)
#
# acc_score = accuracy_score(y_test, y_pred)
# print("acc_score : ", acc_score)
#
# # 각 클래스별 확률 및 타입 확인
# prob = m.predict_proba(X_test_s)
# print("prob :\n", np.round(prob, 3))
# print("prob type :", type(prob))
#
# #SVM
# # 1. 데이터 로드
# X, y = load_wine(return_X_y=True)
#
# # 2. Train / Test 데이터 분할
# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, test_size=0.2, random_state=42
# )
#
# # 3. 데이터 스케일링 (KNN 알고리즘은 거리를 측정하므로 스케일링이 매우 중요합니다)
# scaler = StandardScaler()
# scaler.fit(X_train)
# X_train = scaler.transform(X_train)
# X_test = scaler.transform(X_test)
#
# m = SVC(kernel="rbf")
# m.fit(X_train, y_train)
# Y_pred = m.predict(X_test)
# acc_score = accuracy_score(y_test, Y_pred)
#
# print("accuracy score : ", acc_score)



#모델별 성능 비교
# X,y = load_iris(return_X_y=True)
X, y = load_breast_cancer(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

p1 = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000))
p2 = make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=5))
p3 = make_pipeline(StandardScaler(), SVC())

pipelines = {"로지스틱":p1, "KNM":p2, "SVM":p3}
for model_name, model_pipeline in pipelines.items():
    model_pipeline.fit(X_train, y_train)
    y_pred = model_pipeline.predict(X_test)
    acc_score = accuracy_score(y_test, y_pred)
    print(model_name+"acc_score : " , acc_score)