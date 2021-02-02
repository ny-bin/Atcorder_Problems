#深さ優先探索(dfs)

#整数a1~anが与えられます。
#その中からいくつか選び和がkになることができるか判定しなさい

# n = int(input())
# a = list(map(int, input().split()))
# k = int(input())

n = 4
a = [1, 2, 4, 7]
k = 13


def dfs(i: int, sum: int):
    #n個決め終わったらsumと等しいか返す
    if i == n:
        return sum == k

    #a[i]を使わない場合
    if dfs(i + 1, sum):
        return True

    #a[i]を使う場合
    if dfs(i + 1, sum + a[i]):
        return True

    #kが作れないのでFalseを返す
    return False


if dfs(0, 0):
    print("Yes")
else:
    print('No')
