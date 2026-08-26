# list : 여러 값 순서대로 묶어줌

# 생성
x = ["aaa","bbb","ccc","ddd","eee"]
y = list(range(5)) # 0,1,2,3,4

# 접근
# x[-1]

# 슬라이싱
# x[begin:end:step]

# 추가
# x.append("zzz")
# x.insert(2,"hello")
# result = x + y
x.extend(y)
print(x)

# 수정
x[0:3] = "first"
print(x)

# 삭제
# x.remove(3) : 값으로 삭제
# del x[3] : 인덱스 삭제
temp = x.pop()
print(temp)
# x.clear()
print(x)

# len(x) : 요소 개수
# x.index(값) : 값의 인덱스
# x.count(값) : 값이 몇개 들어있는지
# x.sort() : 정렬
# x.reverse() : 순서 뒤집기
# sum(x) : 요소 합계
# max(x) : 최댓값
# min(x) : 최솟값
# in
x = [100,2,3,4,777,0,999]
print("정렬 이전 x : " , x)
x.sort()
print("정렬 이후 x : " , x)
x.reverse()
print("reverse 이후 x : " , x)

