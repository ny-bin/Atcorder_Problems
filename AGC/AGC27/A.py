num = list(map(int,input().split()))
N = num[0]
x = num[1]

ans = 0

a_num = sorted(list(map(int,input().split())))

count = 1
for a in a_num:
    x = x - a

    if x < 0:
        break
    else:
        ans += 1
    
    if x == 0:
        break
    elif count == N:
        ans -= 1
        break
    count += 1

print(ans)