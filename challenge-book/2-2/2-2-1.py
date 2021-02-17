#コインの金額
V = (1, 5, 10, 50, 100, 500)

#入力
C = [int(x) for x in input().split()]
A = int(input())


def main():
    ans = 0
    for i in range(5, 0, -1):
        t = min(A/V[i], C[i])
        A -= t*V[i]
        ans += t
    print(ans)

    