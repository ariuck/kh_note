n = int(input("n : "))
table = []
value = 0

for i in range(n):
    arr = []
    for j in range(n):
        arr.append(value)
    table.append(arr)

for x in table:
    print(x)
