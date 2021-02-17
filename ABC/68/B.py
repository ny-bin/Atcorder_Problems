N = int(input())
ans = 1

for i in range(8):
    num = 2 ** i
    if num <= N:
        ans = num
    else:
        break

print(ans)