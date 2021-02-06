getIn = input().split()
n = int(getIn[0])
m = int(getIn[1])

conditions = []

for num in range(m):
    getCondition = input().split()
    conditions.append(getCondition)

k = int(input())

dishList = []

for num in range(k):
    getDish = input().split()
    dishList.append(getDish)

dishSelected = []
for num in range(len(dishList)*len(dishList) - 1):
    binStr = format(num, '0'+str(len(dishList))+'b')
    testUnion = set()
    index = 0
    for string in binStr:
        if string == '0':
            testUnion.add(dishList[index][0])
        else:
            testUnion.add(dishList[index][1])
        index = index + 1
    if len(dishSelected) == 0:
        dishSelected.append(testUnion)
    elif len(dishSelected[0]) < len(testUnion):
        dishSelected.clear()
        dishSelected.append(testUnion)
    elif len(dishSelected[0]) == len(testUnion):
        if testUnion not in dishSelected:
            dishSelected.append(testUnion)

totalans = 0
for union in dishSelected:
    ans = 0
    for condition in conditions:
        if condition[0] in union and condition[1] in union:
            ans = ans + 1
    if totalans < ans:
        totalans = ans
print(totalans)
