table = [
    [10, 20, 30],
    [40, 50, None],
    [70, 80, 90]
]
print(table)
for i in range(3):
    if None in table[i]:
        del table[i]
        break

# 결측치를 찾고, 해당 행 삭제
print(table)
