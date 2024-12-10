characters = []
disk = []

with open("C:\\Users\\J\\source\\repos\\aoc-2024\\Day9\\input.txt", "r") as file:
    while True:
        char = file.read(1)
        if not char:
            break
        characters.append(int(char))

id = 0
isBlockFile = True

for num in characters:
    if isBlockFile:
        disk.extend([id for _ in range(0, num)])
        id += 1
        isBlockFile = False
    else:
        disk.extend(['.' for _ in range(0, num)])
        isBlockFile = True

fileSizes = []
collapsedOrder = []

previous = None
count = 0

for val in disk:
    if previous == None:
        previous = val
        collapsedOrder.append(val)

    if val != previous:
        fileSizes.append(count)
        collapsedOrder.append(val)
        count = 0
        previous = val

    count += 1

fileSizes.append(count)

loopOrder = collapsedOrder.copy()
loopOrder.reverse()

for val in loopOrder:
    if val != '.':
        i = 0
        j = collapsedOrder.index(val)
        
        while collapsedOrder[i] != '.' or (collapsedOrder[i] == '.' and fileSizes[i] < fileSizes[j]):
            i += 1
            if i > j:
                break

        if i<j:
            sizeDifference = fileSizes[i] - fileSizes[j]
            if sizeDifference == 0:
                collapsedOrder[i], collapsedOrder[j] = collapsedOrder[j], collapsedOrder[i]
                fileSizes[i], fileSizes[j] = fileSizes[j], fileSizes[i]
            else:
                fileSizes[i] = sizeDifference
                fileSizes.insert(i, fileSizes[j])
                collapsedOrder[i], collapsedOrder[j] = collapsedOrder[j], collapsedOrder[i]
                collapsedOrder.insert(i+1, collapsedOrder[j])


finalDisk = []

for i, val in enumerate(collapsedOrder):
    finalDisk.extend([val for x in range(0, fileSizes[i])])


total = 0

for i, num in enumerate(finalDisk):
    if num != '.':
        total += i * num
    

print(total)

# [2, 3, 3, 3, 1, 3, 3, 1, 2, 1, 4, 1, 4, 1, 3, 1, 4, 2]
# [0, '.', 1, '.', 2, '.', 3, '.', 4, '.', 5, '.', 6, '.', 7, '.', 8, 9]

# [2, 2, 1, 3, 3, 1, 3, 3, 1, 2, 1, 4, 1, 4, 1, 3, 1, 4, 2]
# [0, 9, '.', 1, '.', 2, '.', 3, '.', 4, '.', 5, '.', 6, '.', 7, '.', 8, '.']