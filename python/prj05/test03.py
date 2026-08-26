# 숫자 하나 받아서, 양수 음수 zero 판단하기

num = int(input("숫자 : "))

if num > 0 :
    print("양수")
    if num < 0 :
        print("음수")
else :
    print("ZERO")

