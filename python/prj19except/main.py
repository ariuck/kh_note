# 예외(Exception) 처리

print("start ~~~~~~~")

try:
    x = int(input("x : "))
    y = int(input("y : "))
    result = x / y
    print(result)
except Exception as e:
    print("암튼 에러 ~~~")
else:
    print("에러 예상했는데,,,, 문제 없었네 ,,,")
finally:
    print("무적권 실행 ~~~")

print("finish ~~~~~~~")
