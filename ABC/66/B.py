S = input()


count = 0
for n in range(len(S), -1, -1):

    if n == len(S):
        continue
    if n % 2 == 1:
        continue
    sf = S[0:n // 2]
    se = S[n // 2:n]

    if sf == se:
        print(n)
        break
