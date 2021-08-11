a, b = map(int, input().split())

if a * b < 0:
    print("Zero")
elif b < 0:
    n_count = b - a + 1
    if n_count % 2 == 0:
        print("Positive")
    else:
        print("Negative")
else:
    print("Positive")
