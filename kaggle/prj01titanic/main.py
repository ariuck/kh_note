import pandas as pd

train = pd.read_csv('data/train.csv')
test = pd.read_csv('data/test.csv')

# 결측치 처리
train["Age"] = train["Age"].fillna(train.groupby("Pclass")["Age"].transform("median") )

# 결측치 갯수  확인
print(train.isna().sum())


# model
