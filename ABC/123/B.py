import math

first_min = 100 * 10
min_num = 0

sum_time = 0

for n in range(5):
    s = input()
    first_num = int(s[-1])
    if first_min > first_num and first_num != 0:
        first_min = first_num
        min_num = int(s)

    s_num = int(s)
    sum_time += math.ceil(s_num / 10) * 10

sum_time -= math.ceil(min_num / 10) * 10
sum_time += min_num

print(sum_time)
