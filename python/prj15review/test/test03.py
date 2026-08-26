x = []

value = 1
for i in range(3):
    arr = []
    for j in range(1, 4):
        arr.append(value)
        value += 1
    x.append(arr)

for temp in x:
    print(temp, end=" ")
