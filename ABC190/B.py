n = input().split()
second = int(n[1])
damage = int(n[2])

ans = False

for num in range(int(n[0])):
    attack = input().split()
    if second > int(attack[0]) and damage < int(attack[1]):
        ans = True
        break

if ans:
    print('Yes')
else:
    print('No')

