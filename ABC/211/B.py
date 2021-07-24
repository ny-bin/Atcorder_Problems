L = ["H", "2B", "3B", "HR"]

for n in range(4):
    S = input()
    if S in L:
        L.remove(S)

if len(L) == 0:
    print("Yes")
else:
    print("No")
