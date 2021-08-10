A, B = list(map(int, input().split()))
S = input()

ans = 'No'
if S[A] == '-':
    new_S = S.replace('-', '', 1)
    if new_S.isdigit():
        ans = 'Yes'

print(ans)
