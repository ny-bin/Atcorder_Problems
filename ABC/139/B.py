import math

num = input().split()
a = int(num[0])
b = int(num[1])
now = 1
ans = 0

while b > now:
    now += a - 1
    ans += 1

print(ans)