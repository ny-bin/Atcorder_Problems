

N, A, B, C, D = map(int, input().split())

S = '#' + input() + '#'


def can_reach(start, end):
    for i in range(start, end):
        if S[i] == '#' and S[i + 1] == '#':
            return False
    return True


block = 0
space = 0

ans = True

if not can_reach(A, C) or not can_reach(B, D):
    print("No")
elif C > D:
    ans = False
    for j in range(B, D + 1):
        if S[j - 1] == '.' and S[j] == '.' and S[j + 1] == '.':
            ans = True
    if not ans:
        print('No')
    else:
        print('Yes')
else:
    print('Yes')
