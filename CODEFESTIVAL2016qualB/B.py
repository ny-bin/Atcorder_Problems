N = list(map(int,input().split()))
S = input()

sum = 0
b_sum = 0
for i in range(len(S)):
    if S[i] == "c":
        print("No")
    if S[i] == "b":
        b_sum += 1
        if sum < N[1] + N[2]:
            if N[2] >= b_sum:
                print("Yes")
                sum += 1
            else:
                print("No")
        else:
            print("No")
    if S[i] == "a":
        if sum < N[1] + N[2]:
            print("Yes")
            sum += 1
        else:
            print("No")
        



