import numpy as np

names = ["가희", "나희", "다희", "라희", "마희"]
scores = np.array([[85, 90, 100],  # 가희
                   [70, 60, 50],  # 나희
                   [95, 88, 92],  # 다희
                   [40, 55, 65],  # 라희
                   [100, 100, 80]])  # 마희

# 학생별 총점
# result01 = np.sum(scores , axis=1)
# print(result01)

# 과목별 평균
# result02 = np.mean(scores, axis=0)
# print(result02)

# 1등 찾기 (총점 제일 높은 학생 이름)
# result = names[np.argmax( np.sum(scores , axis=1) )]
# print(result)


# 보충 대상 (60점 미만)
print(scores[scores < 60])