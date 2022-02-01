H, W = map(int, input().split())

sharp_count = 0
for h in range(H):
    a = list(input())
    sharp_count += a.count("#")

if sharp_count == H + W - 1:
    print("Possible")
else:
    print("Impossible")
