N = int(input())
A = sorted(list(map(int, input().split())), reverse=True)

ans = 0
match_count = 0
node_list = [0, 0]
skip = False
for i in range(len(A)):

    if skip:
        skip = False
        continue

    if i + 1 >= len(A):
        break

    if A[i] == A[i + 1]:
        skip = True
        node_list[match_count] = A[i]
        match_count += 1
        if match_count == 2:
            break

print(node_list[0] * node_list[1])
