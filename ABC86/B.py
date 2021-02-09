import math

num = input().split()

a = num[0]
b = num[1]

ans = int(a + b)


if (math.ceil(math.sqrt(ans))) ** 2 == ans:
    print("Yes")
    print(math.sqrt(ans))
else:
    print("No")