# 국어, 영어, 수학 점수를 입력받아 총점과 평균을 출력하세요.
# 국어: 80
# 영어: 90
# 수학: 70
# 총점: 240
# 평균: 80.0

kor = int(input("국어 : "))
eng = int(input("영어 : "))
math = int(input("수학 : "))

total = kor + eng + math
avg = total/3

print(total)
print(avg)

