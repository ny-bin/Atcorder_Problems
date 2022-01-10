S = input()

# 回文が偶数→真ん中に回文あり(aa)
# 回文が奇数→中心を挟む3文字に回文あり(a?a)
# →2個以上離す必要あり+今回は3文字のみのため、abcabcabc...のような周期になる
# →数が1個以内の差なら問題なし

a_count = S.count('a')
b_count = S.count('b')
c_count = S.count('c')

if abs(
        a_count -
        b_count) <= 1 and abs(
            a_count -
            c_count) <= 1 and abs(
                c_count -
        b_count) <= 1:
    print('Yes')
else:
    print('No')
