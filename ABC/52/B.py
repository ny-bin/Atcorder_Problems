N = int(input())
S = input()

count = 0
ans = 0
for s in S:
    if s == "I":
        count += 1
    elif s == 'D':
        count -= 1

    ans = max(ans, count)

print(ans)
