N = int(input())
A = []

first_max = 0
second_max = 0

for n in range(N):
    a = int(input())
    A.append(a)
    if a >= first_max:
        second_max = first_max
        first_max = a
    elif a >= second_max:
        second_max = a

for a in A:
    if a == first_max:
        print(second_max)
    else:
        print(first_max)
