N, X = map(int, input().split())
A = list(map(int, input().split()))

sum_price = sum(A)
if N // 2 == 0:
    sum_price -= N / 2
else:
    sum_price -= N / 2

if X >= sum_price:
    print("Yes")
else:
    print("No")
