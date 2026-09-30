import numpy as np
import pandas as pd

a = np.array([90,80,100])

sr = pd.Series([90,80,100] , index=['국어','수학','영어'])
print(sr["국어"])


df = pd.DataFrame({
    "이름": ["가영", "나영", "다영"],
    "나이": [21, 22, 23],
})

print("df.columns : " , df.columns)
print("df.index : " , df.index)
print("df.shape : " , df.shape)