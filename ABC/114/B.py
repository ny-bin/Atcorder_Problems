S = input()

ans = 10**10

for n in range(len(S) - 2):
    s = int(S[n:n + 3])
    ans = min(ans, abs(s - 753))

print(ans)
