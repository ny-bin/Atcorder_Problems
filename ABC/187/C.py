# https://atcoder.jp/contests/abc187/tasks/abc187_b
# https://atcoder.jp/contests/abc187/tasks/abc187_b
n = []
answer = 0

r = int(input())
for num in range(r):
    n.append(input())

success = False
for item in n:
    if item[0] == '!':
        pass
    else:
        newStr = "!" + item
        if n.__contains__(newStr):
            print(item)
            success = True
            break
if not success:
    print("satisfiable")

#時間over


#解説
# https://atcoder.jp/contests/abc187/editorial/485
N = int(input())
S = set(input() for i in range(N))
for s in S:
    if "!" + s in S:
        print(s)
        exit()
print("satisfiable")
