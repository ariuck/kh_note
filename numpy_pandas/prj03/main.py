# bool 인덱싱
import numpy as np

scores = np.array([100,50,70,30])

print(scores[(scores >= 50) & (scores < 80)])


