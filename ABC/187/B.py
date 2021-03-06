# https://atcoder.jp/contests/abc187/tasks/abc187_b
import itertools

n = []
answer = 0

r = int(input())
for num in range(r):
    n.append(input().split())

for pair in itertools.combinations(n, 2):
    x1 = int(pair[0][0])
    x2 = int(pair[1][0])
    y1 = int(pair[0][1])
    y2 = int(pair[1][1])
    b = (y1-y2)/(x1-x2)
    if -1.0 <= b <= 1.0:
        answer += 1

print(answer)