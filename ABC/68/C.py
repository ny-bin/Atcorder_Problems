N, M = map(int, input().split())

start_to_list = [False] * N
end_from_list = [False] * N
move_list = []
for n in range(M):
    a, b = map(int, input().split())
    if a == 1:
        start_to_list[b - 1] = True
    elif b == 1:
        start_to_list[a - 1] = True

    if a == N:
        end_from_list[b - 1] = True
    elif b == N:
        end_from_list[a - 1] = True

ans = False
for n in range(N):
    if start_to_list[n] and end_from_list[n]:
        ans = True
if ans:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")
