S = input()

ans = 'yes'

for s in S:
    count = S.count(s)
    if count > 1:
        ans = 'no'
        break

print(ans)
