# Bool 인덱싱
import numpy as np

m = np.linspace(1, 5, 5).astype(int)
# mask = [False, True, True, True, False]
mask = m > 3

print(m.shape)
print(m.ndim)
print(m.size)
print(m.dtype)
print(m[(m > 1) | (m < 5)])
