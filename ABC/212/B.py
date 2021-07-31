X = list(input())
status = True

if X[0] == X[1] == X[2] == X[3]:
    status = False

weak = True
for i in range(len(X)):
    now = int(X[i])
    if i == 3:
        break
    next = int(X[i + 1])
    if now == 9:
        if next != 0:
            weak = False
    elif now + 1 != next:
        weak = False

if weak:
    status = False

if status:
    print("Strong")
else:
    print("Weak")
