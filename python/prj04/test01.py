# 현재 연도를 2026이라고 할 때 사용자의 출생 연도를 입력받아 나이를 출력하세요.
# (만나이 ㄴㄴ, 연나이 ㅇㅇ)

current_year = 2026
birth_year = int( input("출생년도 : ") )
age = current_year - birth_year + 1
print(f"{current_year}년 기준 나이는 {age} 입니다")
