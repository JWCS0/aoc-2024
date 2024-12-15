map = []
instructions = []

def printMap(map):
    mapString = ""
    for row in map:
        for spot in row:
            mapString += spot
        mapString += "\n"
    print(mapString.strip())

def isInBounds(y, x, matrix):
    return y >= 0 and x >= 0 and y < len(matrix) and x < len(matrix[0])

robot =[0, 0]

with open("Day15\input.txt", "r") as file:
    isMap = True
    for i, line in enumerate(file):
        if line == "\n":
            isMap = False

        if isMap:
            map.append(list(line.strip()))
            if "@" in line:
                robot[0] = i
                robot[1] = line.find("@")

        else:
            instructions.extend(list(line.strip()))

directions = {
    "^": [-1,0],
    ">": [0,1],
    "v": [1,0],
    "<": [0,-1]
}

for direction in instructions:
    yModifier = directions[direction][0]
    xModifier = directions[direction][1]

    nextPosition = [robot[0] + yModifier, robot[1] + xModifier]

    if map[nextPosition[0]][nextPosition[1]] == "#":
        continue

    if map[nextPosition[0]][nextPosition[1]] == ".":
        map[nextPosition[0]][nextPosition[1]] = "@"
        map[robot[0]][robot[1]] = "."
        robot[0], robot[1] = nextPosition[0], nextPosition[1]
        continue

    toBeMoved = []

    while map[nextPosition[0]][nextPosition[1]] == "O":
        toBeMoved.append([nextPosition[0], nextPosition[1]])
        nextPosition[0] += yModifier
        nextPosition[1] += xModifier

    if map[nextPosition[0]][nextPosition[1]] == ".":
        while len(toBeMoved) > 0:
            moving = toBeMoved.pop()
            map[moving[0]+yModifier][moving[1]+xModifier] = "O"

        map[robot[0] + yModifier][robot[1] + xModifier] = "@"
        map[robot[0]][robot[1]] = "."
        robot[0], robot[1] = robot[0] + yModifier, robot[1] + xModifier

printMap(map)

total = 0

for y, row in enumerate(map):
    for x, value in enumerate(row):
        if value == "O":
            total += 100*y + x

print(total)