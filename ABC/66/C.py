n = int(input())
A = list(input().split())

count = len(A)
B = []

is_reversed = True
if len(A) % 2 == 0:
    is_reversed = False
else:
    is_reversed = True

if not is_reversed:
    for i in range(len(A) - 1, 0, -2):
        print(A[i], end=' ')

    for i in range(0, len(A), 2):
        print(A[i], end=' ')
else:
    for i in range(len(A) - 1, 0, -2):
        print(A[i], end=' ')
    print(A[0], end=' ')

    for i in range(1, len(A), 2):
        print(A[i], end=' ')
