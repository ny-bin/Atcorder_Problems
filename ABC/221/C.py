N = list(input())
num = len(N)

A = []
B = []

ans = 0

for i in range(2 ** num):
    A = []
    B = []
    for j in range(num):
        if ((i >> j) & 1):
            A.append(N[j])
        else:
            B.append(N[j])
    if len(A) == 0:
        a = 0
    else:
        A = sorted(A, reverse=True)
        a = int(''.join(A))

    if len(B) == 0:
        b = 0
    else:
        B = sorted(B, reverse=True)
        b = int(''.join(B))

    ans = max(a * b, ans)


print(ans)
# A = []
# B = []

# index = 0
# for n in N:

#     if index == len(N) - 1:
#         B.append(n)
#     else:
#         if index % 2 == 0:
#             A.append(n)
#         else:
#             B.append(n)
#     index += 1

# list_a = [str(n) for n in sorted(A, reverse=True)]
# list_b = [str(n) for n in sorted(B, reverse=True)]

# a_str = ''.join(list_a)
# b_str = ''.join(list_b)

# print(int(a_str) * int(b_str))
