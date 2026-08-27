import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False

# 데이터 준비
df = sns.load_dataset("penguins")
df.to_csv("penguins.csv")

# 데이터 확인
#결측치
#단변량
#이변량
#상관관계
#정보