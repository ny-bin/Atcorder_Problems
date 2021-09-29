S = list(input())
count = len(S)

start_odd = []
start_even = []

for i in range(count):
    if i % 2 == 0:
        start_odd.append('0')
        start_even.append('1')
    else:
        start_odd.append('1')
        start_even.append('0')

even_count = 0
odd_count = 0
for i in range(count):
    if S[i] != start_odd[i]:
        odd_count += 1

    if S[i] != start_even[i]:
        even_count += 1


print(min(even_count, odd_count))
