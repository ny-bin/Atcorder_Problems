from string import ascii_lowercase

S = input()

has_value = False
for c in ascii_lowercase:
    if c not in S:
        print(c)
        has_value = True
        break

if not has_value:
    print("None")
