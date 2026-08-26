import random
from game.kh import judgeUpDown as abc

print("===== UP DOWN =====")

# 정답(랜덤)숫자 준비하기
answer = random.randint(1, 50)

while True:
    # 유저한테 입력받기
    num = int(input("숫자 : "))

    result = abc(answer , num)
    # 판단하기 및 결과출력
    print(result)
    if result :
        break



