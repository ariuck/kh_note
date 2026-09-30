'''
np.array() -  간격 알고있을때
np.linspace() = 개수 알고있을때
zeros()
zeros()
ones()
full()
eye()

shape
ndim
size
type

astype()

'''
import numpy as np

x = np.eye(9)
print(x)

s = (3,4)
matrix = np.zeros(s)
print(matrix)

y = np.zeros_like(matrix)
print(y)
temp = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
x = np.array([temp,temp,temp,temp,temp])
print(x.shape)
print(x.ndim)
