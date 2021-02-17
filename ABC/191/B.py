n = input().split()

N = int(n[0])
X = int(n[1])

a = input().split()
    
ans = []

for n in range(len(a)):
    if a[n] != str(X):
        ans.append(a[n])

print(' '.join(ans))