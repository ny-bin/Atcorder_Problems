S = list(input())


answer = 'NO'

for i in range(len(S)):
    for j in range(len(S)):
        # iの左に仕切りを置く
        ans = ''
        if i < j:
            S_before = S[:i]
            S_after = S[j:]
            ans = "".join(S_before + S_after)
        else:
            S_before = S[:j]
            S_after = S[i:]
            ans = "".join(S_before + S_after)

        if ans == 'keyence':
            answer = 'YES'
            break
    if answer == 'YES':
        break

print(answer)
