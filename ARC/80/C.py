N = int(input())
A = list(map(int, input().split()))

four_multi = 0
two_multi = 0
odd = 0
for a in A:
    if a % 4 == 0:
        four_multi += 1
    elif a % 2 == 0:
        two_multi += 1
    else:
        odd += 1

if N % 2 == 0 and two_multi / 2 + four_multi >= N / 2:
    print("Yes")
elif N % 2 == 1 and two_multi / 2 + four_multi >= odd - 1:
    print("Yes")
else:
    print("No")
