# 盤面を黒と白に分けて黒の部分を右隣に移動する
# □□■□□■□□■□
# □□□□□□□■■■
# 最大値では黒がすべて右寄りになる

# 累積和で計算可能
b_index_list = []
after_list = []
b_count = 0
S = input()

index = 0
for s in S:
    if s == 'B':
        b_count += 1
        b_index_list.append(index)
    index += 1

before_sum = sum(b_index_list)

w_count = len(S) - b_count
for num in range(w_count, len(S)):
    after_list.append(num)
after_sum = sum(after_list)

print(after_sum - before_sum)
