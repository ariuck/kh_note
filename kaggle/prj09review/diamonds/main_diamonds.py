import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.constants import carat

plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False

df = sns.load_dataset("diamonds")
df.to_csv("diamonds.csv")

print(df.head())
print(df.info())
print(df.describe())
print(df.isna().sum())

#전처리
#값이0인거 제거
# 전처리 (한 줄 작성)
df = df[(df['x'] > 0) & (df['y'] > 0) & (df['z'] > 0)].reset_index(drop=True)
# df = df[df[['x','y','z']] > 0]
#단변량
#가격, 캐럿 히스토그램
# fig, axes = plt.subplots(1,2,figsize = (10,10))
# sns.histplot(data=df["price"], ax = axes[0],bins = 20)
# sns.histplot(data=df["carat"], ax = axes[1],bins = 20)

#이변량
# fig, axes = plt.subplots(1,3,figsize = (15,5))
# sns.scatterplot(data = df,x = "carat",y="price", ax=axes[0],alpha = 0.1)
# plt.show()
#상관관계
num_cols = ["carat","depth","table","price","x","y","z"]
result = df[num_cols].corr()
print(result)

#인사이트
