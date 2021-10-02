import copy

S = list(input())
S_deep = copy.deepcopy(S)
T = input()

ans = False

if ''.join(S) == T:
    print('Yes')

else:
    for i in range(len(S) - 1):
        a = S[i]
        b = S[i + 1]
        S[i] = b
        S[i + 1] = a
        if ''.join(S) == T:
            ans = True
            break
        S = copy.deepcopy(S_deep)

    if ans:
        print('Yes')
    else:
        print('No')
