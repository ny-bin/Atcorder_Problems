import string
import copy

S = list(input())
origin = copy.copy(S)

ans = 100
for n in list(string.ascii_lowercase):
    if set(S) == {n}:
        ans = 0
        break
    if n in S:
        count = 0
        while True:
            next_list = []
            for m in range(len(S)):
                if m == len(S) - 1:
                    break

                if S[m] == n or S[m + 1] == n:
                    next_list.append(n)
                else:
                    next_list.append(S[m])
            if set(next_list) == {n}:
                count += 1
                ans = min(count, ans)
                break
            else:
                count += 1
                S = copy.copy(next_list)
        S = copy.copy(origin)

print(ans)

# △
