import math
A, B, C, D = map(int, input().split())

A_row = A - 1
# 1~BまででC,Dの倍数でないものの数
# =C,Dの倍数の数の合計-C*Dの倍数の数
lcmCD = C * D // math.gcd(C, D)
B_ans = ((B // C) + (B // D) - (B // lcmCD))

# 1~AまででC,Dの倍数でないものの数
A_ans = ((A_row // C) + (A_row // D) - (A_row // lcmCD))

print((B - A + 1) - (B_ans - A_ans))
