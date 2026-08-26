import numpy as np

# 데이터 준비
m = np.arange(12)
# m = m.reshape(3,4)

# 차원 추가


print(m)
print(m.shape)
print("=====")
m2 = m[: , np.newaxis]
print(m2)
print(m2.shape)

