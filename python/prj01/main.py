# 자기소개 프로그램

'''
이름 : <사용자입력>
나이 : <사용자입력>
키 : <사용자입력>
몸무게 : <사용자입력>

제 이름은 ㅇㅇㅇ 이고,
나이는 ㅇㅇ살 입니다.
내년에는 ㅇㅇ살이 됩니다.
키랑 몸무게는 ㅇㅇ/ㅇㅇ 입니다.
'''

name = input("이름 : ")
age = int(input("나이 : "))
height = input("키 : ")
weight = input("몸무게 : ")

print(f"제 이름은 {name} 이고")
print(f"나이는 {age} 살 입니다.")
print(f"내년에는 {age+1} 살이 됩니다.")
print(f"키랑 몸무게는 {height}/{weight} 입니다.")


