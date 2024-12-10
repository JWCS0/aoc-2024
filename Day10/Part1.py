map = []
def printMap(map):
    for row in map:
        print(row)

with open("C:\\Users\\J\\source\\repos\\aoc-2024\\Day10\\input.txt", "r") as file:
    for line in file:
        map.append([int(x) for x in str(line.strip())])

startPoints = []

for y in range(0, len(map)):
    for x in range(0, len(map[0])):
        if map[y][x] == 0:
            startPoints.append(str(y) + ',' + str(x))

def isInBounds(y, x, matrix):
    return y >= 0 and x >= 0 and y < len(matrix) and x < len(matrix[0])

def searchFor(y, x, target, lookingFor, nines:set):
    if not isInBounds(y, x, map):
        return
    
    currentYX = map[y][x]
    
    if lookingFor != currentYX:
        return
    
    if lookingFor == currentYX and target == currentYX:
        nines.add(str(y) + ',' + str(x))
        return

    searchFor(y+1, x, target, lookingFor+1, nines)
    searchFor(y-1, x, target, lookingFor+1, nines)
    searchFor(y, x+1, target, lookingFor+1, nines)
    searchFor(y, x-1, target, lookingFor+1, nines)
    

total = 0

for point in startPoints:
    y = int(point.split(',')[0])
    x = int(point.split(',')[1])

    pathsToNines = set()

    searchFor(y+1, x, 9, 1, pathsToNines)
    searchFor(y-1, x, 9, 1, pathsToNines)
    searchFor(y, x+1, 9, 1, pathsToNines)
    searchFor(y, x-1, 9, 1, pathsToNines)

    total += len(pathsToNines)

print(total)