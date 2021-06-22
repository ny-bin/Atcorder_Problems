N = int(input())

S = []

for n in range(N):
    S.append(input().list())

for i in range(N-2,-1,-1):
    for j in range(1,2*(N-1)):
        if S[i][j] == '#':
            if S[i+1][j-1] == "X":
                S[i][j] = "X"
            if S[i+1][j] == "X":
                S[i][j] = "X"
            if S[i+1][j+1] == "X":
                S[i][j] = "X"
                
for i in range(0,N):
    S[i] = ''.join(S[i])
    print(S[i])


            
