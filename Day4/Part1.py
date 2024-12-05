wordsearch = []

with open("/workspaces/aoc-2024/Day4/dayFourInput.txt") as file:
    for line in file:
        wordsearch.append(list(line))

minCoord = 0
maxCoord = len(wordsearch)
count = 0

directions = {
    "N": [-1,0],
    "NE": [-1, 1],
    "E": [0, 1],
    "SE": [1,1],
    "S": [1,0],
    "SW": [1, -1],
    "W": [0, -1],
    "NW": [-1, -1]
}

matchingWord = "XMAS"

def search(array, originY, originX):
    matches = 0

    for direction in directions:
        Y = originY
        X = originX
        matchingWordIndex = 0

        while matchingWordIndex < len(matchingWord):
            if X >= maxCoord or X < minCoord or Y >= maxCoord or Y < minCoord:
                break
            
            if matchingWordIndex == len(matchingWord)-1 and array[Y][X] == matchingWord[len(matchingWord)-1]:
                matches += 1
                break

            if array[Y][X] != matchingWord[matchingWordIndex]:
                break

            matchingWordIndex += 1
            Y += directions[direction][0]
            X += directions[direction][1]
            
    return matches

total = 0
for y in range(0, maxCoord):
    for x in range(0, maxCoord):
        print(wordsearch[y][x])
        if wordsearch[y][x] == 'X':
            total += search(wordsearch, y, x)

print(total)