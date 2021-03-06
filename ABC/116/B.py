s = int(input())
count = 1
num = []
while True:
    if s not in num:
        num.append(s)
        if s % 2 == 0:
            s = s / 2
        else:
            s = 3 * s + 1
        count += 1
    else:
        break

print(count)