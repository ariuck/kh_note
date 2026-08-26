x = []
value = 10

for j in range(3):
    temp = []
    for i in range(3):
        temp.append(value)
        value += 10
    x.append(temp)

print(x)

