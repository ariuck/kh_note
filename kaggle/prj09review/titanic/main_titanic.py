import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False

# 데이터
df = sns.load_dataset("titanic")
df.to_csv("titanic.csv")

#데이터 구경
#데이터 구조 확인 및 결측치 확인

#단변량 ,,, 이런 항목ㅇ이 있구나 ,,, 이렇게 생겼구나 ,,,
#이변량 ,,, 얘랑 쟤랑 관계가 있구나 ,,,
#상관관계(숫자만 뽑아서 상관계수 확인해보기 , 히트맵)

#정보


