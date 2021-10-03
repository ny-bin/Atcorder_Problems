R, G, B, N = map(int, input().split())

count = 0
for r in range(N + 1):
    for g in range(N + 1):
        red_ball = r * R
        greed_ball = g * G
        blue_ball = N - red_ball - greed_ball

        if 0 <= blue_ball and blue_ball % B == 0:
            count += 1

        if blue_ball < 0:
            break

print(count)
