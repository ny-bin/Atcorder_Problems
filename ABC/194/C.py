N = int(input())
As = list(map(int, input().split()))

import itertools
ans = 0
hiku = 0
for pair in itertools.combinations(As, 2):
    xy = pair[0] * pair[1]
    hiku += xy

for i in As:
    ans += pow(i,2)

ans = (ans * (N-1)) - (hiku * 2)
print(ans)