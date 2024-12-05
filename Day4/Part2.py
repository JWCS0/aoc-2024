wordsearch = []

with open("/workspaces/aoc-2024/Day4/dayFourInput.txt") as file:
    for line in file:
        wordsearch.append(list(line))

minCoord = 0
maxCoord = len(wordsearch)
count = 0

directions = {
    "NE": [-1, 1],
    "SE": [1,1],
    "SW": [1, -1],
    "NW": [-1, -1]
}

keys = list(directions.keys())

def isInBounds(Y, X):
    return Y > minCoord and Y < maxCoord-1 and X > minCoord and X < maxCoord-1

def charInDirection(array, originY, originX, direction):
    print(originX, originY)
    return array[originY + directions[direction][0]][originX + directions[direction][1]]

def isXmas(array, originY, originX):
    for i in range(0, len(directions)):
        if charInDirection(array, originY, originX, keys[i]) == 'M' and charInDirection(array, originY, originX, keys[(i+1)%len(directions)]) == 'M' and charInDirection(array, originY, originX, keys[(i+2)%len(directions)]) == 'S'and charInDirection(array, originY, originX, keys[(i+3)%len(directions)]) == 'S':
            return 1
    return 0
# def search(array, originY, originX):
#     matches = 0

#     for direction in directions:
#         Y = originY
#         X = originX
#         matchingWordIndex = 0

#         while matchingWordIndex < len(matchingWord):
#             if X >= maxCoord or X < minCoord or Y >= maxCoord or Y < minCoord:
#                 break
            
#             if matchingWordIndex == len(matchingWord)-1 and array[Y][X] == matchingWord[len(matchingWord)-1]:
#                 matches += 1
#                 break

#             if array[Y][X] != matchingWord[matchingWordIndex]:
#                 break

#             matchingWordIndex += 1
#             Y += directions[direction][0]
#             X += directions[direction][1]
            
#     return matches

total = 0

for y in range(0, maxCoord):
    for x in range(0, maxCoord):
        if wordsearch[y][x] == 'A' and isInBounds(y,x):
            total += 1 if isXmas(wordsearch, y, x) else 0

print(total)