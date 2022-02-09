N = int(input())
S = list(input())

w_count = S.count("W")
e_count = S.count("E")

ans = 10 ** 10
w_from_start = 0
e_from_start = 0
for s in S:
    if s == "E":
        diff = (e_count - 1 - e_from_start) + (w_from_start)
        ans = min(ans, diff)
    else:
        diff = (e_count - e_from_start) + (w_from_start)
        ans = min(ans, diff)

    if s == "E":
        e_from_start += 1
    else:
        w_from_start += 1

print(ans)
