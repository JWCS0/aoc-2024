characters = []
disk = []

with open("C:\\Users\\J\\source\\repos\\aoc-2024\\Day9\\mini.txt", "r") as file:
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

i = 0
j = len(disk) - 1

while i < j:
    while disk[i] != '.':
        i += 1
        if i > j:
            break

    while disk[j] == '.':
        j -= 1
        if i > j:
            break

    if i<j:
        disk[i], disk[j] = disk[j], disk[i]

total = 0

maxIndex = disk.index('.')

for i, num in enumerate(disk):
    if i == maxIndex:
        break
    total += i * num

print(total)