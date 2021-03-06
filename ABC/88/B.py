N = int(input())
nums = sorted(list(map(int, input().split())),reverse=True)
alice = 0
bob = 0

for n in range(N):
    if n % 2 == 1:
        #bob
        bob += nums[n]
    else:
        #alice
        alice += nums[n]

print(alice - bob)
