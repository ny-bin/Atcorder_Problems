Q = int(input())

ball_list = []
add_num = 0

for q in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        num = query[1]
        ball_list.append(num - add_num)
    elif query[0] == 2:
        add_num += query[1]
    else:
        num = min(ball_list)
        print(num + add_num)
        ball_list.remove(num)
