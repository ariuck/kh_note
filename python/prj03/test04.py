# list : 순서있음, 변경가능, 중복허용, 다양한 타입

x = ["사과" , "딸기", 3.14 , 100 , True , "계란"]
print(x)
print(x[0])
x[0] = "바나나"
print(x)
x[1:3] = ["포도" , 9.99 , 1,2,3]   # 슬라이싱을 이용한 수정
print(x)
x[1:3] = []               # 슬라이싱을 이용한 삭제
print(x)

x.append(777)
print(x)

x.insert(2 , "홍진호")
print(x)

x.remove("홍진호")
print(x)

# x.clear()
# print(x)

y = ["박혜린", "박하솔", "이상직","홍진호","홍진호"]
x.extend(y)
print(x)

i = x.index("박하솔")
print(i)

cnt = x.count("홍진호")
print(cnt)

x.reverse()
print(x)

x2 = x
print(x2)

x[0] = "임요환"
print(x)
print(x2)



















# 문자열 인덱싱



# tuple
# dictionary
# set