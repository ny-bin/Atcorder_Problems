x1, y1, x2, y2 = map(int, input().split())

X = x2 - x1
Y = y2 - y1

bec_X1 = -Y
bec_Y1 = X

bec_X2 = -bec_Y1
bec_Y2 = bec_X1


print(x2 + bec_X1, end=' ')
print(y2 + bec_Y1, end=' ')
print(x2 + bec_X1 + bec_X2, end=' ')
print(y2 + bec_Y1 + bec_Y2, end=' ')

# memo
# 回転行列を用いる問題
# 指定の角度分ベクトルを回転させる
