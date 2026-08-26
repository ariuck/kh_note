num_list = input().split()
a = int(num_list[0])
b = int(num_list[1])

result = 0
for x in range(a, b+1):
    if x % 2 == 1:
        if x == a :
            print(f"{x}", end="")
        else:
            print(f"+{x}", end="")
        result += x
    else:
        print(f"-{x}", end="")
        result -= x

print(f"={result}" , end="")

