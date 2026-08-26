def judgeNum(num):
    if num % 2 == 1:
        return "홀수"
    else:
        return "짝수"



# 사용자로부터 정수를 입력받고, 홀짝 판단하여 출력하기

# 입력받기
x = int(input("정수 : "))

# 판단하기
result = judgeNum(x)

# 출력하기
print(f"입력하신 숫자 {x} 는 {result} 입니다")


