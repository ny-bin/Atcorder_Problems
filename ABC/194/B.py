N = int(input())
lista = [0] * N
listb = [0] * N
index = 0
for n in range(N):
    tasktime = list(map(int, input().split()))
    lista[n] = tasktime[0]
    listb[n] = tasktime[1]

a = min(lista)
b = min(listb)
ans = max(a, b)
indexa = lista.index(a)
indexb = listb.index(b)
if(indexa == indexb):
    ans = a + b
    newans = 100000
    if(a > b):
        del lista[indexa]
        newa = min(lista)
        newans = max(newa, b)
    else:
        del listb[indexb]
        newb = min(listb)
        newans = max(newb,a)
    
    if(newans < ans):
        ans = newans

print(ans)