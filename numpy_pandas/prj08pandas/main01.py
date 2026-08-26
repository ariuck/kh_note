import pandas as pd

# series : numpy + label (이름표 달려있는 1차원)
sr = pd.Series([80,90,100] , index=["a","b","c"])

# print(sr.values)  # 넘파이 배열
# print(sr.index)   # label
# print(sr + 5)     # vector 연산 가능


