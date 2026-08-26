n = int(input("n : "))
table = []
value = 0

for i in range(n):
    arr = []
    for j in range(n):
        if i == j:
            arr.append(1)
        else:
            arr.append(0)
    table.append(arr)

for x in table:
    print(x)
