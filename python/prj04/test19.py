# 숫자 3개를 입력받으세요.
# 첫 번째 숫자가 두 번째와 세 번째 숫자보다 모두 큰지 출력하세요.
# 숫자1: 30
# 숫자2: 20
# 숫자3: 10
# 숫자1이 가장 큰가?: True

num01 = int(input("숫자1 : "))
num02 = int(input("숫자2 : "))
num03 = int(input("숫자3 : "))
result = num01 > num02 and num01 > num03
print(result)
