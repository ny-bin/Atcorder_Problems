N, K, S = map(int, input().split())

ans = []
for n in range(N):
    if S == 10 ** 9:
        if n < K:
            ans.append(str(S))
        else:
            ans.append("1")
    else:
        if n < K:
            ans.append(str(S))
        else:
            ans.append(str(S + 1))

string = " ".join(ans)
print(string)
