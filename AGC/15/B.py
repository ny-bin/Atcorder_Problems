S = list(input())

count = 0
for s in range(len(S)):
    direction = S[s]
    if direction == 'U':
        count += (len(S) - s - 1) + (s * 2)
    else:
        count += (s) + ((len(S) - s - 1) * 2)

print(count)

# ○
