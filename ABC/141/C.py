N, K, Q = map(int, input().split())

start_point = K - Q
point_list = [K - Q] * N

for q in range(Q):
    a = int(input())
    point_list[a - 1] += 1

for c in point_list:
    if c > 0:
        print("Yes")
    else:
        print("No")
