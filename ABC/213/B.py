N = int(input())
A = list(map(int, input().split()))

max_num = 0
max_index = 0
max_num2 = 0
max_index2 = 0
for i in range(len(A)):
    a = A[i]
    if a > max_num2:
        if a > max_num:
            max_index2 = max_index
            max_num2 = max_num
            max_num = a
            max_index = i + 1
        else:
            max_num2 = a
            max_index2 = i + 1

print(max_index2)
