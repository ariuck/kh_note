import pandas as pd

# DataFrame

df = pd.DataFrame({
    "이름": ["가영", "나영", "다영"],
    "국어": [70,80,90],
    "영어": [100,50,60],
    "수학": [30,100,80]
})

# print(df.columns)
# print(df.index)
# print(df.shape)
# print(df.head(2))
# print(df.tail(2))
print(df.sample())

