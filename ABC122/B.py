S = input()

count = 0
ans = 0

for s in S:
    if s == "A" or s == "C" or s == "G" or s == "T":
        count += 1
        if ans < count:
            ans = count
    else:
        if ans < count:
            ans = count
            count = 0
        else:
            count = 0

print(ans)