import math
a, b, c = map(int, input().split())

diff = c - a - b

if diff > 0 and diff * diff > 4 * a * b:
    print("Yes")
else:
    print("No")
