num = list(map(int, input().split()))
N = num[0]
M = num[1]
C = num[2]
B = list(map(int, input().split()))
ans = 0

for n in range(N):
    A = list(map(int, input().split()))
    sum_AB = 0
    for i in range(len(A)):
        sum_AB += A[i]*B[i]
    sum_AB += C
    if sum_AB > 0:
        ans += 1

print(ans)
