# up down game

import random

cnt = 0
answer = random.randint(1,50)
while True :
    x = int(input("예상 숫자 : "))
    cnt += 1
    if answer > x:
        print("UP")
    elif answer < x:
        print("DOWN")
    else:
        print("GOOD !!!")
        print(cnt , "번 시도함")
        break