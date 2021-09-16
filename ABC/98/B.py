N = int(input())
S = input()

ans = 0

# 何文字カッとするか
for n in range(N - 1):
    if n == 0 or n == N:
        continue

    slice_first = S[0:n]
    slice_end = S[n:]

    count = 0
    counted_str = []
    for item in slice_first:
        if item in slice_end and item not in counted_str:
            count += 1
            counted_str.append((item))
    ans = max(count, ans)

print(ans)
