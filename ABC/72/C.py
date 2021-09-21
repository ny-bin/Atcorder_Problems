N = int(input())
A = list(map(int, input().split()))

S = {}

# 0で初期化
for n in range(-2, 10**5 + 2):
    S[n] = 0


# i番目まで選択したときのxの個数 => S[x]
for i in range(N):
    a = A[i]
    a_minus = a - 1
    a_plus = a + 1
    S[a] += 1
    S[a_minus] += 1
    S[a_plus] += 1

print(max(S.values()))
