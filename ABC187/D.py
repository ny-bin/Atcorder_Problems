# https://atcoder.jp/contests/abc187/tasks/abc187_d

a = []
t = []
answer = 0

r = int(input())
for num in range(r):
    s = input().split()
    a.append(int(s[0]))
    t.append(int(s[1]))

#sortでずれる時があるのでNG
a.sort(reverse=True)
t.sort(reverse=True)

asum = sum(a) 
tsum = 0

for num in range(len(a)):
    if asum >= tsum:
        asum -= a[num]
        tsum += t[num] + a[num]
        answer = num
    else:
        break

print(answer)


#解答
N = int(input())
X = 0
x = []
for i in range(N):
    A, B = map(int, input().split())
    X -= A
    x.append(A + A + B)
x.sort()
ans = 0
while X <= 0:
    X += x.pop()
    ans += 1
print(ans)