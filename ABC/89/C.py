N = int(input())

M = []
A = []
R = []
C = []
H = []

for n in range(N):
    s = input()
    if s[0] == "M":
        M.append(s)
    if s[0] == "A":
        A.append(s)
    if s[0] == "R":
        R.append(s)
    if s[0] == "C":
        C.append(s)
    if s[0] == "H":
        H.append(s)

m = len(M)
a = len(A)
r = len(R)
c = len(C)
h = len(H)

ans = m * a * r
ans += m * a * c
ans += m * a * h
ans += m * r * c
ans += m * r * h
ans += m * c * h
ans += a * r * c
ans += a * r * h
ans += a * c * h
ans += r * c * h

print(ans)
