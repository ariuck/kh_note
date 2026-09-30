# 컴프리헨션
matrix = [[1, 2], [3, 4]]
flat = [x for row in matrix for x in row]

labels = ["짝" if n % 2 == 0 else "홀" for n in range(4)]
print(labels)

# 언패킹

# 내장함수
