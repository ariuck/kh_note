# 행 + 열 동시 선택
import pandas as pd

df = pd.read_csv("data/people.csv")
df = df.set_index("이름")
# print(df.iloc[0:3,0:3])
print(df.loc["가영":"다희","나이":"도시"])

