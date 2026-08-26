import numpy as np

# 데이터 준비
x = np.linspace(1, 24 , 24)


# 차원 변경
# x = x.reshape(3,4)
x = x.reshape(2, 3, 2, 2)

# 데이터 출력
print(x)
print(x.shape)
