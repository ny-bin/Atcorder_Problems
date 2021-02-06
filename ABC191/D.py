import math
# 円と交わる直線の座標を返却


def cli(line, x, y, r):
	points = []

	if "y" in line:
		# y軸に平行な直線の場合
		a = 0
		b = 1
		c = -(line["y"])
	elif "x" in line:
		# x軸に平行な直線の場合
		a = 1
		b = 0
		c = -(line["x"])
	else:
		# y = mx + n
		a = line["m"]
		c = line["n"]
		b = -(c / line["n"])

	l = a ** 2 + b ** 2
	k = a * x + b * y + c
	d = l * r ** 2 - k ** 2

	if d > 0:
		# ２点交わる
		ds = math.sqrt(d)
		apl = a / l
		bpl = b / l
		xc = x - apl * k
		yc = y - bpl * k
		xd = bpl * ds
		yd = apl * ds

		point = {}
		point["x"] = xc - xd
		point["y"] = yc + yd
		points.append(point)
		point = {}
		point["x"] = xc + xd
		point["y"] = yc - yd
		points.append(point)

	elif d == 0:
		# １点交わる
		point = {}
		point["x"] = x - a * k / l
		point["y"] = y - b * k / l
		points.append(point)

	return points


n = input().split()
x = float(n[0])
y = float(n[1])
r = float(n[2])

ans = 0

#考慮する点の個数を考える
#円を囲む四角形内の点の数を計算
# minX = math.ceil(x - r) - 1
# maxX = math.ceil(x + r)
# dx = maxX - minX
# minY = math.ceil(x - r) - 1
# maxY = math.ceil(y + r)
# dy = maxY - minY
# count = dx * dy

# for X in range(math.ceil(x) - math.ceil(r), math.ceil(x) + math.ceil(r) + 1, 1):
#     for Y in range(math.ceil(y) - math.ceil(r), math.ceil(y) + math.ceil(r) + 1, 1):
#         L = (X - x)**2 + (Y-y)**2
#         if L <= r:
#             ans += 1

# print(ans)

maxX = math.floor(x + r)
minX = math.floor(x - r)
for X in range(minX, maxX, 1):
    line = ["x", X]
    test = cli(line, x, y, r)
    print(test)