import numpy as np
x = np.array([10,20,30,40,50])

'''
합계
평균
표준편차
최소값
최대값
중앙값
where
rng
'''
# sum1 = np.sum(x)
# avg1 = np.mean(x)
# std1 = np.std(x)
# max1 = np.max(x)
# min1 = np.min(x)
# mid1 = np.median(x)
# y = np.array([sum1,avg1,std1,max1,min1,mid1])
# print(y)
# print(np.sum(y))


# np.where(조건식, A,B)


rng = np.random.default_rng(seed = 42)

result = rng.normal(90,5,size=10)
print(result)