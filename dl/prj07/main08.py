import numpy as np

a = np.arange(10)

a = np.where(a % 2 == 0, np.power(a, 2), a)

print(a)