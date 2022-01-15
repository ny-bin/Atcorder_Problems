N = int(input())
task_list = []
for n in range(N):
    task = list(map(int, input().split()))
    task_list.append(task)

sorted_task_list = sorted(task_list, reverse=False, key=lambda x: x[1])

sum_time = 0
for t in sorted_task_list:
    sum_time += t[0]
    max_time = t[1]
    if sum_time > max_time:
        break

if sum_time <= max_time:
    print("Yes")
else:
    print("No")
