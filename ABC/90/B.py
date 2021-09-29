A, B = map(int, input().split())


count = 0
for i in range(A, B + 1):
    num_str = list(str(i))
    ans = True
    for n in range(len(num_str) // 2):
        f = num_str[n]
        l = num_str[-n - 1]
        if f != l:
            ans = False
            break

    if ans:
        count += 1

print(count)
