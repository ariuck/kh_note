import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.datasets import load_iris

# 1. 한글 폰트 설정 (Windows: Malgun Gothic, Mac: AppleGothic)
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# 2. 데이터 로드 및 파생 변수 생성
iris = load_iris(as_frame=True)
df = iris.frame
df.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'target']

species_map = {0: 'Setosa', 1: 'Versicolor', 2: 'Virginica'}
df['species'] = df['target'].map(species_map)
df['petal_area'] = df['petal_length'] * df['petal_width']

# 3. 3개 그래프 비교 시각화
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# [그래프 1] 꽃잎(Petal) - 명확한 구별력
sns.scatterplot(
    data=df, x='petal_length', y='petal_width',
    hue='species', style='species', s=70, ax=axes[0], palette='Set2'
)
axes[0].set_title('1. 꽃잎 특성 (Petal):', fontsize=11)
axes[0].set_xlabel('꽃잎 길이 (cm)')
axes[0].set_ylabel('꽃잎 너비 (cm)')

# [그래프 2] 꽃받침(Sepal) - 비효율적인 이유 (데이터 뒤엉킴)
sns.scatterplot(
    data=df, x='sepal_length', y='sepal_width',
    hue='species', style='species', s=70, ax=axes[1], palette='Set2'
)
axes[1].set_title('2. 꽃받침 특성 (Sepal)', fontsize=11, color='red')
axes[1].set_xlabel('꽃받침 길이 (cm)')
axes[1].set_ylabel('꽃받침 너비 (cm)')

# [그래프 3] 파생 변수(Petal Area) - 성능 극대화
sns.boxplot(
    data=df, x='species', y='petal_area',
    hue='species', ax=axes[2], palette='Set2', legend=False
)
sns.stripplot(
    data=df, x='species', y='petal_area',
    color='black', alpha=0.5, jitter=0.2, ax=axes[2]
)
axes[2].set_title('3. 꽃잎 면적 파생변수 (Petal Area)\n: 두 수치를 곱해 품종 간 격차 극대화', fontsize=11)
axes[2].set_xlabel('붓꽃 품종 (Species)')
axes[2].set_ylabel('꽃잎 면적 (cm²)')

plt.tight_layout()
plt.show()