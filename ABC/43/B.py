from collections import deque

S = list(input())

ans = deque([])
for s in S:
    if s == "0":
        ans.append("0")
    elif s == "1":
        ans.append("1")
    else:
        if len(ans) > 0:
            ans.pop()

print("".join(ans))
