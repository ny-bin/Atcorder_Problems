N = int(input())
A = []
for n in range(N):
    a = int(input())
    A.append(a)

A.sort()
before_num = 0
before_count = 0
count = 0
for num in A:
    if before_num == num:
        before_count += 1
    elif before_num != 0:
        if before_count % 2 == 0:
            count += 1
        before_num = num
        before_count = 0
    else:
        before_num = num
    
if before_count % 2 == 0:
    count += 1

print(count)
