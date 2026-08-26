# 배열 생성 및 속성
import numpy as np


shape = (100,100)
v = 123
result = np.zeros(shape)      # 전부 0으로 채움
result = np.ones(shape)       # 전부 1로 채움
result = np.full(shape , v)   # 전부 v로 채움
result = np.eye(2)              # 단위행렬(n x n) (대각선 요소들이 전부 1)

print(result.shape)
print(result.ndim)
print(result)


