s = input().split()
n = int(s[0])
m = int(s[1])

n_ten = 10 ** n
x = (n / m)   

ans = x % m

print(ans)
