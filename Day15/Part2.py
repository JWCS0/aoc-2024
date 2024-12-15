from operator import itemgetter

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

        else:
            instructions.extend(list(line.strip()))

for y, row in enumerate(map):
    newRow = []
    for x, value in enumerate(row):
        match value:
            case "#":
                newRow.append("#")
                newRow.append("#")
            case "O":
                newRow.append("[")
                newRow.append("]")
            case ".":
                newRow.append(".")
                newRow.append(".")
            case "@":
                newRow.append("@")
                robot[1] = newRow.index("@")
                newRow.append(".")
    map[y] = newRow

directions = {
    "^": [-1,0],
    ">": [0,1],
    "v": [1,0],
    "<": [0,-1]
}

pushing = {
    "^": ["[","]"],
    ">": ["["],
    "v": ["[","]"],
    "<": ["]"]
}

def otherSide(side):
    if side == "[":
        return "]"
    else:
        return "["

def getConnectedBoxes(y:int, x:int, upwards:bool, boxes:list, map:list):
    if upwards:
        if map[y-1][x] == "[":
            if [y-1, x] not in boxes:
                boxes.append([y-1, x])
            if [y-1, x+1] not in boxes:
                boxes.append([y-1, x+1])
            getConnectedBoxes(y-1, x, upwards, boxes, map)
            getConnectedBoxes(y-1, x+1, upwards, boxes, map)

        if map[y-1][x] == "]":
            if [y-1, x] not in boxes:
                boxes.append([y-1, x])
            if [y-1, x-1] not in boxes:
                boxes.append([y-1, x-1])
            getConnectedBoxes(y-1, x, upwards, boxes, map)
            getConnectedBoxes(y-1, x-1, upwards, boxes, map)

    if not upwards:
        if map[y+1][x] == "[":
            if [y+1, x] not in boxes:
                boxes.append([y+1, x])
            if [y+1, x+1] not in boxes:
                boxes.append([y+1, x+1])
            getConnectedBoxes(y+1, x, upwards, boxes, map)
            getConnectedBoxes(y+1, x+1, upwards, boxes, map)

        if map[y+1][x] == "]":
            if [y+1, x] not in boxes:
                boxes.append([y+1, x])
            if [y+1, x-1] not in boxes:
                boxes.append([y+1, x-1])
            getConnectedBoxes(y+1, x, upwards, boxes, map)
            getConnectedBoxes(y+1, x-1, upwards, boxes, map)

def listToString(l:list):
    returnString = ""
    for i in l:
        returnString += str(i)
        returnString += ","
    return returnString[:-1]

def stringToList(string:str):
    return [int(x) for x in string.split(",")]

while len(instructions) > 0:
    direction = instructions.pop(0)
    yModifier = directions[direction][0]
    xModifier = directions[direction][1]

    if len(instructions) == 505:
        pass

    nextPosition = [robot[0] + yModifier, robot[1] + xModifier]

    if not isInBounds(nextPosition[0], nextPosition[1], map):
        continue

    if map[nextPosition[0]][nextPosition[1]] == "#":
        continue

    if map[nextPosition[0]][nextPosition[1]] == ".":
        map[nextPosition[0]][nextPosition[1]] = "@"
        map[robot[0]][robot[1]] = "."
        robot[0], robot[1] = nextPosition[0], nextPosition[1]
        continue

    toBeMoved = []
    onlyPushSymbol = None

    if direction in ["^", "v"]:
        onlyPushSymbol = map[nextPosition[0]][nextPosition[1]]

        while map[nextPosition[0]][nextPosition[1]] == onlyPushSymbol:
            toBeMoved.append([nextPosition[0], nextPosition[1]])
            if onlyPushSymbol == "[":
                toBeMoved.append([nextPosition[0], nextPosition[1]+1])
            else:
                toBeMoved.append([nextPosition[0], nextPosition[1]-1])
            nextPosition[0] += yModifier
            nextPosition[1] += xModifier

    else:
        while map[nextPosition[0]][nextPosition[1]] in pushing[direction]:
            toBeMoved.append([nextPosition[0], nextPosition[1]])
            nextPosition[0] += yModifier
            nextPosition[1] += xModifier
            toBeMoved.append([nextPosition[0], nextPosition[1]])
            nextPosition[0] += yModifier
            nextPosition[1] += xModifier

    if direction in ["^","v"]:

        for location in toBeMoved:
            getConnectedBoxes(location[0], location[1], direction == "^", toBeMoved, map)

        toBeMoved = list(dict.fromkeys([listToString(x) for x in toBeMoved]))
        toBeMoved = [stringToList(x) for x in toBeMoved]

        isValid = True

        for box in toBeMoved:
            if direction == "^":
                above = box.copy()
                above[0] -= 1
                if map[above[0]][above[1]] == "#":
                    isValid = False
            if direction == "v":
                below = box.copy()
                below[0] += 1
                if map[below[0]][below[1]] == "#":
                    isValid = False

        if not isValid:
            continue

        toBeMoved = sorted(toBeMoved, reverse=direction == "^", key=itemgetter(0))


    if (map[nextPosition[0]][nextPosition[1]] != "#" and direction in ["^", "v"] or (map[nextPosition[0]][nextPosition[1]] == "." and direction not in ["^", "v"])):
        while len(toBeMoved) > 0:
            moving = toBeMoved.pop()
            map[moving[0]+yModifier][moving[1]+xModifier] = map[moving[0]][moving[1]]
            map[moving[0]][moving[1]] = "."

        map[robot[0] + yModifier][robot[1] + xModifier] = "@"
        map[robot[0]][robot[1]] = "."
        robot[0], robot[1] = robot[0] + yModifier, robot[1] + xModifier
    

total = 0

for y, row in enumerate(map):
    for x, value in enumerate(row):
        if value == "[":
            total += 100*y + x

print(total)

printMap(map)