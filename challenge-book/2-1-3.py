# 大きさがN*Mの迷路があります。
# 1ターンに隣接する４方向への移動が可能です。
# ゴールするまでの最短経路は何ターンですか

import queue
N = 10
M = 10
_INPUT = """\
10
10
# S # # # # # # . #
. . . . . . # . . #
. # . # # . # # . #
. # . . . . . . . .
# # . # # . # # # # 
. . . . # . . . . #
. # # # # # # # . #
. . . . # . . . . .
. # # # # . # # # .
. . . . # . . . G #
"""


def bfs(x: int, y: int):
    q = queue.Queue()
    #すべての点を初期化
    for n in range(N):
        for m in range(M):
            d[n][m] = 1000
        q.put((n, m))
        d[n][m] = 0

    while(len(q) > 0):
        #キューの先頭を取り出す
        p = q.get()
        if p[1] == gx and p[2] == gy:
            break

        #移動4方向をループ
        for i in range(len(dx)):
            nx = p[1] + dx[i]
            ny = p[2] + dy[i]

            #移動可能か、既に訪れているかの判定
            if 0 <= nx <= N and 0 <= ny <= M and field[nx][ny] != '#' and d[nx][ny] == 1000:
                q.push((nx, ny))
                d[nx][ny] = d[x][y] + 1
    return d[gx][gy]

def main(*, int=int, input=input):
    ans = bfs()
    print(ans)


if __name__ == "__main__":
    import io
    import sys
    sys.stdin = io.StringIO(_INPUT)
    N = int(input())
    M = int(input())
    field = [input().split() for n in range(N)]

    d = [N][M]
    gx = 10
    gy = 9
    sx = 1
    sy = 0

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    main()
