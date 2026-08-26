# 1229
data = input().split()
height = float(data[0])
weight = float(data[1])

if height < 150 :
    std_weight = (height - 100)
elif height < 160 :
    std_weight = (height - 150) /2 + 50
else :
    std_weight = (height - 100) * 0.9


bmi = (weight - std_weight)  * 100 / std_weight

if bmi <= 10 :
    print("정상")
elif bmi <= 20 :
    print("과체중")
else :
    print("비만")
