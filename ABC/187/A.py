#S(123)  = 1+ 2 + 3 = 6

# 入力
# A B

# 出力
# S(A) とS(B) のうち大きい方の値を出力せよ。
# S(A) とS(B) が等しい場合は、S(A) を出力せよ。

n = input().split()

S1 = int(n[0][0]) + int(n[0][2]) +  int(n[0][1])
S2 = int(n[1][0]) + int(n[1][2]) +  int(n[1][1])
 
if S1 > S2:
    print(S1)
else:
    print(S2)