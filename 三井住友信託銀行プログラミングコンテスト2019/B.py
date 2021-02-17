import math

N = int(input())

perX = N // 1.08

if math.floor(perX * 1.08) == N:
    print(math.floor(perX))
elif math.floor((perX + 1) * 1.08) == N:
    print(math.floor(perX + 1))
elif math.floor((perX - 1) * 1.08) == N:
    print(math.floor(perX - 1))
else:
    print(":(")