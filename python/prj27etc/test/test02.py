# 컴프리헨션
from test.test01 import result

# result = []
# for x in range(10):
#     if x % 2 == 0:
#         result.append("짝")
#     else:
#         result.append("홀")


# // swy
# for n in range(10):
#     if n % 2 == 0:
#         result.append("짝")
# result = ["짝" for n in range(10) if n % 2 == 0 ]

for n in range(10):
    if n % 2 == 0:
        result.append("짝")
    else:
        result.append("홀")

result = ["짝" if n % 2 == 0 else "홀" for n in range(10)]

print(result)
