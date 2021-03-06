num = list(map(int, input().split()))

N = num[0]
K = num[1]
newN = 0

while True:
    if N // K > 1:
        l = N // K
        newN = abs(N - K * l)
    else:
        newN = abs(N - K)
    
    if N > newN:
        N = newN
    else:
        newN = N
        break

print(newN)
