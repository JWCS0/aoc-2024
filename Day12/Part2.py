map = []
def printMap(map):
    for row in map:
        print(row)

with open("Day12\input.txt", "r") as file:
    for line in file:
        map.append(list(line.strip()))

regions = []

class Region():
    plant:str
    positions:list
    area:int
    sides:int = 0

    def __init__(self, area:int, positions:list, plant:str) -> None:
        self.area = area
        self.positions = positions
        self.plant = plant
        pass

    def __str__(self) -> str:
        return "\nPlant: " + str(self.plant) + "| Positions: " + str(self.positions) + " | Area: " + str(self.area) + " | Sides: " + str(self.sides)

    def __repr__(self) -> str:
        return "\nPlant: " + str(self.plant) + "| Positions: " + str(self.positions) + " | Area: " + str(self.area) + " | Sides: " + str(self.sides)

def isInBounds(y, x, matrix):
    return y >= 0 and x >= 0 and y < len(matrix) and x < len(matrix[0])

def getArea(y, x, popFrom:list, addTo:list):
    if not isInBounds(y, x, map):
        return 0
    
    current = str(y) + "," + str(x)
    if current not in popFrom:
        return 0

    addTo.append(current)
    popFrom.remove(current)

    return getArea(y+1, x, popFrom, addTo) + getArea(y-1, x, popFrom, addTo) + getArea(y, x+1, popFrom, addTo) + getArea(y, x-1, popFrom, addTo) + 1

plantLocationMap = {}

for y, row in enumerate(map):
    for x, plant in enumerate(row):
        currentPosition = str(y) + "," + str(x)
        currentPlantLocations = plantLocationMap.get(plant, [])
        currentPlantLocations.append(currentPosition)
        plantLocationMap[plant] = currentPlantLocations
        
groupings = []

for plant in plantLocationMap:
    locationsOfPlant = plantLocationMap[plant].copy()

    while len(locationsOfPlant) > 0:
        positionsInRegion = []
        startLocationString = locationsOfPlant[0]
        startLocationY = int(startLocationString.split(",")[0])
        startLocationX = int(startLocationString.split(",")[1])
        currentArea = getArea(startLocationY, startLocationX, locationsOfPlant, positionsInRegion)
        groupings.append(Region(currentArea, positionsInRegion, plant))

directions = {
    "S":[1, 0],
    "N":[-1,0],
    "E":[0, 1],
    "W":[0, -1]
}

def advanceBorder(position:str):
    splitPosition = position.split(",")
    direction = splitPosition[0]
    y = int(splitPosition[1])
    x = int(splitPosition[2])

    if direction == "N" or direction == "S":
        return direction + "," + str(y) + "," + str(x+1)
    else:
        return direction + "," + str(y+1) + "," + str(x)
    
def retreatBorder(position:str):
    splitPosition = position.split(",")
    direction = splitPosition[0]
    y = int(splitPosition[1])
    x = int(splitPosition[2])

    if direction == "N" or direction == "S":
        return direction + "," + str(y) + "," + str(x-1)
    else:
        return direction + "," + str(y-1) + "," + str(x)

def updateSides(region:Region):
    borders = set()

    for position in region.positions:
        positionSplit = position.split(",")
        y, x = int(positionSplit[0]), int(positionSplit[1])    
        currentPlant = map[y][x]

        for direction in directions:
            newY = y + directions[direction][0]
            newX = x + directions[direction][1]

            bordering = direction+","+str(newY)+","+str(newX)
            
            if not (newY >= 0 and newX >= 0 and newY < len(map) and newX < len(map[0])) or map[newY][newX] != currentPlant:
                borders.add(bordering)

    trueBorders = 0

    while len(borders) > 0:
        currentBorder = borders.pop()

        nextBorder = advanceBorder(currentBorder)
        while nextBorder in borders:
            borders.remove(nextBorder)
            nextBorder = advanceBorder(nextBorder)

        prevBorder = retreatBorder(currentBorder)
        while prevBorder in borders:
            borders.remove(prevBorder)
            prevBorder = retreatBorder(prevBorder)
        
        trueBorders += 1

    region.sides = trueBorders

totalCost = 0
for region in groupings:
    updateSides(region)
    totalCost += region.sides * region.area
    
print(totalCost)