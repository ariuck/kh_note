import seaborn as sns
import matplotlib.pyplot as plt

# 인코딩
plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False

# 데이터 준비
# "total_bill","tip","sex","smoker","day","time","size"
df = sns.load_dataset("tips")

# 도화지 준비
fig, axes = plt.subplots(2, 3, figsize=(12, 8))

# hisplot
sns.histplot(data=df,  bins=20, kde=True, ax=axes[0, 0])

# boxplot
sns.boxplot(data=df, x="day", y="total_bill", ax=axes[0, 1])

# scatterplot
sns.scatterplot(data=df, x="total_bill", y="tip", hue="day", ax=axes[1, 0])

# heatmap
c = df[["total_bill", "tip", "size"]].corr()
sns.heatmap(data=c, annot=True, cmap="coolwarm", fmt=".2f", ax=axes[1][1])

# countplot
sns.countplot(data=df, x="day", hue="sex", ax=axes[0][2])

# pairplot : 변수 쌍 전체 한번에
result = sns.pairplot(data=df)
result.savefig("result.svg")

# 결과 확인
plt.show()



