import math

map = []

def printMap(map):
    mapString = "______"
    for i, _ in enumerate(map):
        mapString += str(i).ljust(5, " ")
    print(mapString.strip())
        
    mapString = ""
    for i, row in enumerate(map):
        mapString += str(i).ljust(5, " ")
        for spot in row:
            mapString += str(spot).ljust(5, " ")
        mapString += "\n"
    print(mapString.strip())

with open("Day16/input.txt", "r") as file:
    for line in file:
        map.append(list(line.strip()))

distanceMap = [[] for _ in map]

for y in range(0, len(map)):
    for x in range(0, len(map[0])):
        if map[y][x] == "#":
            distanceMap[y].append(-1)
        elif map[y][x] == "E":
            distanceMap[y].append(0)
            end = (y, x)
        else:
            distanceMap[y].append(math.inf)
        if map[y][x] == "S":
            start = (y, x)

directions = {
    "^": [-1,0],
    ">": [0,1],
    "v": [1,0],
    "<": [0,-1]
}

def getValidNeighbors(y, x):
    validDirections = []

    for direction in directions:
        if distanceMap[y + directions[direction][0]][x + directions[direction][1]] != -1:
            validDirections.append(direction)

    return validDirections

def traverse(y, x, direction, queue:list, facing):
    validNexts = getValidNeighbors(y, x)

    for next in validNexts:
        cost = distanceMap[y][x]
        nextY = y + directions[next][0]
        nextX = x + directions[next][1]

        directionSymbols = ["^", ">", "v", "<"]

        if directionSymbols.index(next) == (directionSymbols.index(direction) + 2) % len(directionSymbols):
            continue

        if next == direction:
            if distanceMap[nextY][nextX] > cost + 1:
                distanceMap[nextY][nextX] = cost + 1
                if map[nextY][nextX] == "S":
                    facing = next
                queue.append((nextY, nextX, next))

        else:
            if distanceMap[nextY][nextX] > cost + 1001:
                distanceMap[nextY][nextX] = cost + 1001
                if map[nextY][nextX] == "S":
                    facing = next
                queue.append((nextY, nextX, next))

facing = ""
queue = [(end[0], end[1], "v"), (end[0], end[1], "v")]
while len(queue) > 0:
    current = queue.pop()
    traverse(current[0], current[1], current[2], queue, facing)

print(distanceMap[start[0]][start[1]] if facing == ">" else distanceMap[start[0]][start[1]] + 1000)