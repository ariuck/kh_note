import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False

# 데이터 로드
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# 데이터 파악
# print(df.isna().sum())


# 결측지 처리 (Age , Embarked , Cabin)
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
df = df.drop(columns=["Cabin"])

# 단변량 분석
# # 생존자 사망자 비율
# print(df["Survived"].value_counts(normalize=True) * 100)
#
# # 범주형 시각화
# fig, axes = plt.subplots(1, 3, figsize=(15, 5))
# axes[0].set_title("생존여부")
# sns.countplot(x="Survived", data=df , ax=axes[0])
#
# axes[1].set_title("성별")
# sns.countplot(x="Sex", data=df , ax=axes[1])
#
# axes[2].set_title("객실 등급")
# sns.countplot(x="Pclass", data=df , ax=axes[2])
#
# # 나이 시각화
# plt.figure(figsize=(5, 5))
# sns.histplot(df["Age"] , bins=30 , kde=True)
# plt.title("나이")
#
# plt.show()

# 이변량 분석 (성별,객실등급,나이대,가족수 에 따른 생존율 파악)
# fig , axes = plt.subplots(2,2 , figsize=(12,10))
# sns.barplot(x="Sex" , y="Survived" , data=df,ax=axes[0,0])
# sns.barplot(x="Pclass" , y="Survived" , data=df,ax=axes[0,1])
#
# df["AgeBand"] = pd.cut(
#     df["Age"],
#     bins=[0,12,18,40,60,100],
#     labels=["아동","청소년","청년","중년","노년"],
# )
#
# # print(df.groupby("AgeBand")["Survived"].mean())
# sns.barplot(x="AgeBand" , y="Survived" , data=df,ax=axes[1,0])
#
# df["FamilySize"] = df["SibSp"] + df["Parch"] + 1
#
# # print( df.groupby("FamilySize")["Survived"].mean() )
# sns.barplot(x="FamilySize" , y="Survived" , data=df,ax=axes[1,1])


# 상관관계
# print(df.info())
# cols = ["Survived", "Pclass", "Age", "SibSp", "Parch", "Fare"]
# cor = df[cols].corr()
#
# plt.figure(figsize=(10, 8))
# sns.heatmap(cor, cmap="coolwarm", annot=True, fmt=".2f")
# plt.show()

# 인사이트
'''
남성보다 여성이 생존율이 높다
객실 등급이 좋을수록(숫자가 낮을수록) 생존율이 높다
나이가 어린 아동의 경우 생존율이 높다
가족 규모가 2~4인 일 때 생존율이 높다
'''

# 성별 + 객실등급에 따른 생존율 파악
# result = df.groupby(["Sex" , "Pclass"])["Survived"].mean().unstack()
# plt.figure(figsize=(6,4))
# sns.heatmap(result, annot=True, cmap="YlGnBu" , fmt=".2f")
# plt.title("성별 + 객실등급에 따른 생존율 파악")
# plt.show()


# 탑승 항구에 따른 생존율 파악
# result = df.groupby("Embarked")["Survived"].mean()
# plt.figure(figsize=(6,4))
# sns.barplot(data=df, x="Embarked", y="Survived" , order=["C","Q","S"])
# plt.title("탑승 항구에 따른 생존율 파악")
# plt.show()
# result = pd.crosstab(df["Embarked"], df["Sex"])
# print(result)


# 운임에 따른 생존율 파악
# df["FareBand"] = pd.qcut(df["Fare"], 10, labels=["A", "B", "C", "D", "E","F","G","H","I","J"])
# result = df.groupby("FareBand")["Survived"].mean()
# print(result)


# 이름에 따른 생존율 파악
df["Title"] = df["Name"].str.extract(r',\s*([^\.]+)\.')

x = ["Mr", "Miss", "Mrs", "Master"]
df["Title"] = df["Title"].where(df["Title"].isin(x), "Rare")

result = df.groupby("Title")["Survived"].mean()
print(result)

# print(df["Title"].value_counts())
