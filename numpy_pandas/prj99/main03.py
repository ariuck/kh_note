import numpy as np
'''
reshape
flatten

axis
.T 행렬 바꾸는거 이긴한데

newaxis
vstack
hstack
'''

x = np.arange(0, 12, 1)
x = x.reshape(-1, 4)
x = x.flatten()
# x = x.reshape(-1, 1)
print(x.shape)
print(x.ndim)
print(x)