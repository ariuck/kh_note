# 사용자로부터 다음 정보를 입력받으세요.
# - 나이
# - 보호자 동반 여부 (`True` 또는 `False` 대신 숫자 `1` 또는 `0` 입력)
# 다음 조건 중 하나를 만족하면 관람 가능합니다.
# - 나이가 15세 이상
# - 보호자와 동반함
# 결과를 `True` 또는 `False`로 출력하세요.
# 나이: 13
# 보호자 동반(1: 예, 0: 아니오): 1
# 관람 가능: True

age = int(input("나이 : "))
isGuardian = int(input("보호자 동반 여부 : "))

result = age >= 15 or isGuardian == 1
print(result)