a = list(range(3))
b = list(range(3))
c = list(range(3))

x = [a, b, c]

value = 10
for j in range(3):
    for i in range(3):
        x[j][i] = value
        value += 10

print(x)
