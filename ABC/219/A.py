X = int(input())

ans = 0
if X < 40:
    ans = str(40 - X)
elif X < 70:
    ans = str(70 - X)
elif X < 90:
    ans = str(90 - X)
else:
    ans = 'expert'

print(ans)