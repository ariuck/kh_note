# 1 ~ 10 중에서 3의 배수 합

result = 0
n = 1
while n <= 10 :
    if n % 3 == 0 :
        result = result + n
    n += 1

print(result)
