X = int(input())
is_prime = True
count = 0
while True:
    x = X + count
    for i in range(2,x,1):
        if x % i == 0:
            is_prime =  False
            break
        is_prime = True
    
    if is_prime:
        print(x)
        break
    else:
        count += 1