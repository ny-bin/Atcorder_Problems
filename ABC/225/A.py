S = list(input())

a = S[0]
b = S[1]
c = S[2]

if a == b == c:
    print(1)
elif a == b or a == c or b == c:
    print(3)
else:
    print(6)
