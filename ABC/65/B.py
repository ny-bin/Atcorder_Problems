N = int(input())

a_list = []
for n in range(N):
    a = int(input())
    a_list.append(a)


count = 0
target_index = 0
existed = False
for index in range(len(a_list)):
    target_index = a_list[target_index] - 1
    count += 1
    if target_index == 1:
        print(count)
        existed = True
        break

if not existed:
    print(-1)
