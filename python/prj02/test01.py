# 자료구조
'''
list :
    - [ ]
    - 순서O, 수정O, 중복O
tuple :
    - ( )
    - 순서O, 수정X, 중복O
dictionary :
    - {key:value}
    - 키-값 , 수정O
set :
    - { }
    - 순서X, 중복X
'''

x = [100 , 3.14 , 777 , "사과" , True , "사과" , "바나나" ,"사과"]
# x.append(100)
# x.append(3.14)
# x.append(777)
# x.append("사과")
# x.append(True)
print(x)
print(len(x))
x.remove("사과")
x.remove("사과")
x.remove("사과")
print(x)
print(len(x))

print("바나나" in x)
print("오렌지" in x)
