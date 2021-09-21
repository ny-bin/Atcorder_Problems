A, B, C = map(int, input().split())

used_over_num = []

sum_num = 0

ans = False
while True:
    over_num = A % B
    sum_num += over_num
    sum_num = sum_num % B

    if sum_num in used_over_num:
        break

    used_over_num.append(sum_num)

    if sum_num % B == C:
        ans = True

if ans:
    print("Yes")
else:
    print("No")
