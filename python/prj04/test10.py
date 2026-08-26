# Python 점수와 Java 점수를 입력받으세요.
# 다음 조건을 모두 만족해야 통과입니다.
# - Python 60점 이상
# - Java 60점 이상
# - 두 과목 평균 70점 이상
# 결과를 `True`, `False`로 출력하세요.
# Python 점수: 80
# Java 점수: 70
# 통과 여부: True

score01 = int(input("py : "))
score02 = int(input("java : "))
sum = score01 + score02
avg = sum / 2

isPassed = score01 >= 60 and score02 >= 60 and avg >= 70

print(isPassed)