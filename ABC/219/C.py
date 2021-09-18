X = input()
N = int(input())

str_list = {}
find_list = []

for n in range(N):
    string = input()
    find_list.append(string)
    index_list = []
    for char in string:
        index_list.append(X.index(char))

    str_list[string] = index_list

sorted = sorted(str_list.items(), key=lambda x: x[1])

for n in range(len(sorted)):
    print(sorted[n][0])
