# 짝수 행은 1
# 홀수 행은 0

row_number = 3
col_number = 3
table = []

for j in range(row_number):
    arr =[]
    for i in range(col_number):
        if j % 2 == 0 :
            arr.append(1)
        else:
            arr.append(0)
    table.append(arr)

print(table)
