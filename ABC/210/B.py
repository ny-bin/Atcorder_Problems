N = int(input())
S = input()


for n in range(N):
    card = S[n]
    if card == "1":
        if n % 2 == 0:
            print("Takahashi")
            break
        else:
            print("Aoki")
            break
