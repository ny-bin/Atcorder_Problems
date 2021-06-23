#S = ahytiuhbsdf
#T = h.s

def is_match(T, S):
    # Sを頭から順にチェックしていく
    for i in range(0, len(S) - len(T) + 1, 1):
        match = True

        # Tの文字をチェック
        for j in range(0, len(T)):

            if S[i + j] != T[j] and T[j] != '.':
                match = False

        if match:
            return True

    return False


# 使える文字の一覧
C = "abcdefghijklmnopqrstuvwxyz."

S = input()
M = []

for T in C:
    if is_match(T, S):
        M.append(T)

for c1 in C:
    for c2 in C:
        T = c1 + c2
        if is_match(T, S):
            M.append(T)

for c1 in C:
    for c2 in C:
        for c3 in C:
            T = c1 + c2 + c3
            if is_match(T, S):
                M.append(T)
