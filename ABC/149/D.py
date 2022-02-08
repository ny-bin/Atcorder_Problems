N, K = map(int, input().split())
r, s, p = map(int, input().split())
t = input()

ans = 0
hand_log = [""] * N

for n in range(N):
    hand = t[n]
    if hand == "r":
        command = "p"
        point = p
    elif hand == "s":
        command = "r"
        point = r
    else:
        command = "s"
        point = s

    if (n - K >= 0) and (hand_log[n - K] == command):
        command = ""
        point = 0
    ans += point
    hand_log[n] = command


print(ans)
