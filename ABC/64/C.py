N = int(input())
A = list(map(int, input().split()))

free_count = 0

gray = False
brown = False
green = False
light_blue = False
blue = False
yellow = False
orange = False
red = False

for a in A:
    if a < 400:
        gray = True
    elif a < 800:
        brown = True
    elif a < 1200:
        green = True
    elif a < 1600:
        light_blue = True
    elif a < 2000:
        blue = True
    elif a < 2400:
        yellow = True
    elif a < 2800:
        orange = True
    elif a < 3200:
        red = True
    else:
        free_count += 1

color_count = 0
if gray:
    color_count += 1
if brown:
    color_count += 1
if green:
    color_count += 1
if light_blue:
    color_count += 1
if blue:
    color_count += 1
if yellow:
    color_count += 1
if orange:
    color_count += 1
if red:
    color_count += 1

if color_count == 0:
    min_ans = 1
else:
    min_ans = color_count

print(str(min_ans) + ' ' + str(color_count + free_count))
