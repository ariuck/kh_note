from dog import Dog

age = int(input("age : " ))
if age < 0:
    print("나이가 0 미만이네 ,,, 예외 발생시켜야지 ,,,")
    raise Dog("나이 음수 ㄴㄴ")
print(age)


