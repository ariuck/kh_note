import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor

# 데이터 로드
train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")

# 공통 매핑 및 파생변수 함수 정의
qual_map = {"None": 0, "Po": 1, "Fa": 2, "TA": 3, "Gd": 4, "Ex": 5}
ordinal_cols = ["ExterQual", "ExterCond", "BsmtQual", "BsmtCond", "HeatingQC", "KitchenQual", "FireplaceQu", "GarageQual", "GarageCond"]

def map_ord(df):
    df_c = df.copy()
    for col in ordinal_cols:
        if col in df_c.columns:
            df_c[col] = df_c[col].fillna("None").map(qual_map)
    return df_c

def add_fe(df):
    df_c = df.copy()
    df_c["TotalSF"] = df_c["TotalBsmtSF"].fillna(0) + df_c["1stFlrSF"].fillna(0) + df_c["2ndFlrSF"].fillna(0)
    df_c["TotalBath"] = df_c["FullBath"].fillna(0) + (0.5 * df_c["HalfBath"].fillna(0)) + df_c["BsmtFullBath"].fillna(0) + (0.5 * df_c["BsmtHalfBath"].fillna(0))
    df_c["HouseAge"] = df_c["YrSold"] - df_c["YearBuilt"]
    return df_c


# =========================================================
# [1단계 제출] 수치형 데이터 전처리 (결측치 + 스케일링)
# 제출 파일: submission_step1.csv
# =========================================================
X1 = train.drop(columns=["Id", "SalePrice"])
y1 = train["SalePrice"]
test1 = test.drop(columns=["Id"])

num_cols1 = X1.select_dtypes(include=[np.number]).columns
prep1 = ColumnTransformer([("num", Pipeline([("imp", SimpleImputer(strategy="median")), ("scal", StandardScaler())]), num_cols1)])

m1 = Pipeline([("prep", prep1), ("model", RandomForestRegressor(n_estimators=100, random_state=42))])
m1.fit(X1, y1)

sub1 = pd.DataFrame({"Id": test["Id"], "SalePrice": m1.predict(test1)})
sub1.to_csv("submission_step1.csv", index=False)
print("1단계 완료 -> submission_step1.csv 생성")


# =========================================================
# [2단계 제출] + 범주형 인코딩 (순서형 map + 명목형 OneHotEncoder)
# 제출 파일: submission_step2.csv
# =========================================================
X2 = map_ord(X1)
test2 = map_ord(test1)

num_cols2 = X2.select_dtypes(include=[np.number]).columns
cat_cols2 = X2.select_dtypes(include=["object"]).columns

prep2 = ColumnTransformer([
    ("num", Pipeline([("imp", SimpleImputer(strategy="median")), ("scal", StandardScaler())]), num_cols2),
    ("cat", Pipeline([("imp", SimpleImputer(strategy="most_frequent")), ("enc", OneHotEncoder(handle_unknown="ignore", sparse_output=False))]), cat_cols2)
])

m2 = Pipeline([("prep", prep2), ("model", RandomForestRegressor(n_estimators=100, random_state=42))])
m2.fit(X2, y1)

sub2 = pd.DataFrame({"Id": test["Id"], "SalePrice": m2.predict(test2)})
sub2.to_csv("submission_step2.csv", index=False)
print("2단계 완료 -> submission_step2.csv 생성")


# =========================================================
# [3단계 제출] + 도메인 파생변수 생성 (TotalSF, TotalBath, HouseAge)
# 제출 파일: submission_step3.csv
# =========================================================
X3 = add_fe(X2)
test3 = add_fe(test2)

num_cols3 = X3.select_dtypes(include=[np.number]).columns
cat_cols3 = X3.select_dtypes(include=["object"]).columns

prep3 = ColumnTransformer([
    ("num", Pipeline([("imp", SimpleImputer(strategy="median")), ("scal", StandardScaler())]), num_cols3),
    ("cat", Pipeline([("imp", SimpleImputer(strategy="most_frequent")), ("enc", OneHotEncoder(handle_unknown="ignore", sparse_output=False))]), cat_cols3)
])

m3 = Pipeline([("prep", prep3), ("model", RandomForestRegressor(n_estimators=100, random_state=42))])
m3.fit(X3, y1)

sub3 = pd.DataFrame({"Id": test["Id"], "SalePrice": m3.predict(test3)})
sub3.to_csv("submission_step3.csv", index=False)
print("3단계 완료 -> submission_step3.csv 생성")


# =========================================================
# [4단계 제출] + 이상치(Outlier) 제거만 적용
# 제출 파일: submission_step4.csv
# =========================================================
# 면적(GrLivArea > 4000)은 매우 크지만 가격이 30만달러 미만인 특이 이상치 2개 데이터 제거
train_clean = train.drop(train[(train["GrLivArea"] > 4000) & (train["SalePrice"] < 300000)].index)
X4 = add_fe(map_ord(train_clean.drop(columns=["Id", "SalePrice"])))
y4 = train_clean["SalePrice"]
test4 = test3.copy()

num_cols4 = X4.select_dtypes(include=[np.number]).columns
cat_cols4 = X4.select_dtypes(include=["object"]).columns

prep4 = ColumnTransformer([
    ("num", Pipeline([("imp", SimpleImputer(strategy="median")), ("scal", StandardScaler())]), num_cols4),
    ("cat", Pipeline([("imp", SimpleImputer(strategy="most_frequent")), ("enc", OneHotEncoder(handle_unknown="ignore", sparse_output=False))]), cat_cols4)
])

# 1~3단계와 동일한 인자값 유지
m4 = Pipeline([("prep", prep4), ("model", RandomForestRegressor(n_estimators=100, random_state=42))])
m4.fit(X4, y4)

sub4 = pd.DataFrame({"Id": test["Id"], "SalePrice": m4.predict(test4)})
sub4.to_csv("submission_step4.csv", index=False)
print("4단계 완료 -> submission_step4.csv 생성")

print("\n모든 단계 제출 파일 생성 완료!")