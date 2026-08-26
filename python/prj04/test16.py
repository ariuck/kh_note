# 학생의 국어, 영어, 수학 점수를 입력받아 리스트에 저장하세요.
# 그리고 다음 결과를 출력하세요.
# - 점수 리스트
# - 총점
# - 평균
# - 평균이 60점 이상인지
# - 모든 과목이 40점 이상인지
# 예:
# 국어: 80
# 영어: 70
# 수학: 50
# 점수: [80, 70, 50]
# 총점: 200
# 평균: 66.66666666666667
# 평균 60점 이상: True
# 모든 과목 40점 이상: True

kor = int(input("kor : " ))
eng = int(input("eng : " ))
math = int(input("math : " ))
score_list = [kor, eng, math]
total = score_list[0] + score_list[1] + score_list[2]
avg = total / 3

print(score_list)
print(total)
print(avg)
print(avg >= 60)
print(score_list[0] >= 40 and score_list[1] >= 40 and score_list[2] >= 40)
