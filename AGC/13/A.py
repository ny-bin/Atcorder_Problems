N = int(input())
A = list(map(int, input().split()))

ans = 0
before_num = 0
status = ''
for a in A:
    if before_num == 0:
        before_num = a
        continue
    else:
        if a > before_num:
            if status == 'up' or status == '':
                status = 'up'
                before_num = a
                continue
            else:
                before_num = a
                ans += 1
                status = ''
        elif a < before_num:
            if status == 'down' or status == '':
                before_num = a
                status = 'down'
                continue
            else:
                before_num = a
                ans += 1
                status = ''
        elif a == before_num:
            continue

print(ans + 1)
