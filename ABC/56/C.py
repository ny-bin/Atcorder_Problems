
X = int(input())

ans = 0
for x in range(X):
    sumX = x * (1 + x) / 2
    if sumX >= X:
        ans = x
        break
print(ans)
