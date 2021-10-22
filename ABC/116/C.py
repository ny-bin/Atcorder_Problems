N = int(input())
H = list(map(int, input().split()))


def slice_H(h_list, count):
    # 最小値を求めてリストから最小値を引き0を基準としてそれ以外をスライスしたものを返す
    min_h = min(h_list)
    if min_h != 0:
        h_list = [h - min_h for h in h_list]
        count += min_h
    else:
        sliced = []
        start_index = 0
        end_index = 0
        slice_count = 0
        for h in range(len(h_list)):
            if h_list[h] != 0:
                if start_index == 0 and slice_count == 0:
                    start_index = h
                slice_count += 1
            else:
                if slice_count != 0:
                    end_index = h
                    break
        if start_index != 0 and end_index == 0:
            sliced = h_list[start_index:]
            end_index = len(h_list)
        else:
            sliced = h_list[start_index:end_index]
        min_h = min(sliced)
        sliced = [h - min_h for h in sliced]
        count += min_h
        sliced_index = 0
        for n in range(start_index, end_index):
            h_list[n] = sliced[sliced_index]
            sliced_index += 1

    return count, h_list


count = 0

while sum(H) > 0:
    count, H = slice_H(H, count)

print(count)
