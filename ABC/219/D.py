N = int(input())
X, Y = map(int, input().split())


takoyaki = [0]
taiyaki = [0]

for n in range(N):
    tako, tai = list(map(int, input().split()))
    takoyaki.append(tako)
    taiyaki.append(tai)

value = []
