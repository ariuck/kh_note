# 구구단 (2 ~ 9단)

# for dan in range(2, 10):
#     for i in range(1, 10):
#         print(f"{dan} * {i} = {dan * i}")

# 시간 출력
# 0 : 0
# 0 : 1
# ...
# 23 : 59

for hour in range(0,24):
    for min in range(0,60):
        print(f"{hour} : {min}")


