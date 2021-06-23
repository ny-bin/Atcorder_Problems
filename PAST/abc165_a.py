K = int(input())

A, B = map(int, input().split())

#A-Bを調べてKの倍数があるかをチェック
# ok = False
# for x in range(A, B + 1):
#     if x % K == 0:
#         ok = True

# if ok:
#     print("OK")
# else:
#     print("NG")


#Kの倍数を順に調べる
# ok = False
# for x in range(0,1000000):
#     if x * K > B:
#         break
    
#     if A <= x * K <= B:
#         ok = True


# if ok:
#     print("OK")
# else:
#     print("NG")

ok = False
x = A // K
u = B // K

if x < u:
    ok = True

if A % K ==0:
    ok = True

if ok:
    print("OK")
else:
    print("NG")