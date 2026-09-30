from unittest import result
import time
import numpy as np

#만드는 방법 다름
py_list = [1,2,3,4,5]
np_array = np.array([1,2,3,4,5])
#생긴거 다름
# print(py_list)
# print(np_array)

#연산 차이
# result_list = []
# for x in py_list:
#     result = x*2
#     result_list.append(result)
# print(result_list)
#

#====np ====(속도라가듦 np가 훨빠름)
# print(np_array*2)


# 속도
# === py ===
# py_list = list(range(1_000_000))
# start_time = time.time()
# result = 0
# for x in py_list:
#     result += x
# end_time = time.time()
# result_time = time = end_time-start_time
# print("result : " , result)
# print("result_time : " , result_time)

# === np ===
np_array = np.arange(1_000_000)
start_time = time.time()
result = np.sum(np_array)
end_time = time.time()
result_time = time = end_time-start_time
print("result : " , result)
print("result_time : " , result_time)