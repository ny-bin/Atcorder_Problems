K = int(input())

A, B = input().split()

a = 0
b = 0

index = 0
for n in A[::-1]:
    a = a + int(n) * (K ** index)
    index += 1

index = 0
for n in B[::-1]:
    b = b + int(n) * (K ** index)
    index += 1

print(a * b)
