

sa = input()
a_count = 0
sb = input()
b_count = 0
sc = input()
c_count = 0


def next_person(count, list):
    person = list[count]
    return person


target_count = a_count
target_list = sa
while True:
    person = next_person(target_count, target_list)
    if target_list == sa:
        a_count += 1
    elif target_list == sb:
        b_count += 1
    elif target_list == sc:
        c_count += 1
    if person == "a":
        target_count = a_count
        target_list = sa
    elif person == "b":
        target_count = b_count
        target_list = sb
    elif person == "c":
        target_count = c_count
        target_list = sc

    if target_count == len(target_list):
        break

if person == "a":
    print("A")
elif person == "b":
    print("B")
elif person == "c":
    print("C")
