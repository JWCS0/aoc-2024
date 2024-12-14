map = []
def printMap(map):
    for row in map:
        print(row)

with open("/home/j/aoc2024/aoc-2024/Day12/mini2.txt", "r") as file:
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
        return str(self.plant) + " " + str(self.positions) + " " + str(self.area) + " " + str(self.sides)

    def __repr__(self) -> str:
        return str(self.plant) + " " + str(self.positions) + " " + str(self.area) + " " + str(self.sides)

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
        positionsInRegion.sort()
        groupings.append(Region(currentArea, positionsInRegion, plant))

directions = {
    "S":[1, 0],
    "N":[-1,0],
    "E":[0, 1],
    "W":[0, -1]
}

def updateSides(region:Region):
    borders = set()

    for position in region.positions:
        positionSplit = position.split(",")
        y, x = int(positionSplit[0]), int(positionSplit[1])    
        currentPlant = map[y][x]

        for direction in directions:
            newY = y + directions[direction][0]
            newX = x + directions[direction][1]

            bordering = direction+str(newX) if direction == "W" or direction == "E" else direction+(str(newY))
            print(bordering)
            
            if not (newY >= 0 and newX >= 0 and newY < len(map) and newX < len(map[0])):
                borders.add(bordering)
                continue

            if map[newY][newX] != currentPlant:
                borders.add(bordering)

            
        print(position, len(borders))

    region.sides = len(borders)

totalCost = 0
for region in groupings:
    updateSides(region)
    totalCost += region.sides * region.area
    
print(totalCost)


