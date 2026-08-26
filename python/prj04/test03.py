# 초를 입력받아 몇 시간, 몇 분, 몇 초인지 계산하세요.
# 예를 들어 3725초는 1시간 2분 5초입니다.
# 출력 예시:
# 초를 입력하세요: 3725
# 1 시간 2 분 5 초

sec = int(input("초를 입력하세요 : "))

hours = sec // 3600
mins = (sec % 3600) // 60
secs = sec % 60

print("시간 : " , hours)
print("분 : " , mins)
print("초 : " , secs)
