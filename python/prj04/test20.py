# 사용자로부터 다음 정보를 입력받으세요.
# - 아이디
# - 비밀번호
# - 비밀번호 확인
# - 나이
# 다음 조건을 **모두 만족하는지** 출력하세요.
# - 아이디가 `"admin"`이 아님
# - 비밀번호와 비밀번호 확인이 같음
# - 나이가 14세 이상
# 예:
# 아이디: hong
# 비밀번호: 1234
# 비밀번호 확인: 1234
# 나이: 20
# 회원가입 가능: True

id = input("id : ")
pw = input("pw : ")
pw_confirm = input("pw_confirm : ")
age = int(input("age : "))

idValid = id != "admin"
pwValid = pw == pw_confirm
ageValid = age >= 14

result = idValid and pwValid and ageValid
print(result)
