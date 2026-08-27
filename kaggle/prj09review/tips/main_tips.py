import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False

#데이터 불러오기
df = sns.load_dataset("tips")
df.to_csv("tips.csv")

#데이터 확인하기]
# print(df.head())
# print(df.info())
#전처리
# print(df.isna().sum())

df["tip_pct"] = df["tip"] / df["total_bill"] * 100
print(df["tip_pct"].describe())

#단변량

#이변량

#상관관계


#금액대비 팁 비율

#if문 사용 