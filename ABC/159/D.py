N = int(input())
A = list(map(int, input().split()))

B = sorted(A)
B.append(0)
count = 0
before_num = 0
num_dic = {}

all_sum = 0
for a in B:
    if a == before_num:
        count += 1
        continue
    else:
        if count != 0:
            all_sum += (count * (count - 1)) // 2
            num_dic[before_num] = count
        count = 1
        before_num = a

for a in A:
    target_count = num_dic[a]
    if target_count > 2:
        minus_value = (target_count - 1) * (target_count - (target_count - 2))
        print(all_sum - (minus_value // 2))
    elif target_count == 2:
        print(all_sum - 1)
    else:
        print(all_sum)
