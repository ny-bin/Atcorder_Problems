N = int(input())
A = list(map(int, input().split()))
A.append(0)
sum_A = 0
for i in range(len(A)):
    sum_A += abs(A[i] - A[i - 1])

for i in range(len(A) - 1):
    ans = sum_A + abs(A[i - 1] - A[i + 1]) - \
        (abs(A[i - 1] - A[i]) + abs(A[i] - A[i + 1]))
    print(ans)
