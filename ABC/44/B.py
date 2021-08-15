W = input()

counted_list = []
isOk = True

for w in W:
    if w in counted_list:
        continue
    else:
        num_count = W.count(w)
        counted_list.append(num_count)
        if num_count % 2 == 1:
            isOk = False
            break

if isOk:
    print('Yes')
else:
    print('No')
