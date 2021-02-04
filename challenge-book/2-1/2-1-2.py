#Lake Counting(POJ No.2386)

# 大きさがN * M の庭があります。
# そこに雨が降り、水たまりができました。
# 水たまりは8近傍で隣接している場合に繋がっているとみなします。
# 全部でいくつの水たまりがあるでしょう

_INPUT = """\
10
12
W . . . . . . . . W W .
. W W W . . . . . W W W
. . . . W W . . . W W .
. . . . . . . . . W W .
. . . . . . . . . W . .
. . W . . . . . . W . .
. W . W . . . . . W W .
W . W . W . . . . . W .
. W . W . . . . . . W .
. . W . . . . . . . W .
"""


def dfs(x: int, y: int):
    #今いるところを置き換える
    field[x][y] = '.'

    for dx in range(-1, 2, 1):
        for dy in range(-1, 2, 1):
            #移動後のx,y
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < M and field[nx][ny] == 'W':
                dfs(nx, ny)

def main(*,int=int,input=input):

    ans: int = 0
    for n in range(N):
        for m in range(M):
            if field[n][m] == 'W':
                dfs(n, m)
                ans = ans + 1
    print(ans)


if __name__ == "__main__":
    import io,sys
    sys.stdin = io.StringIO(_INPUT)
    N = int(input())
    M = int(input())
    field = [input().split() for n in range(N)]
    main()


