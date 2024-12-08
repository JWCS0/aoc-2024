antennaMap = []
antiNodes = set()
antennas = set()

with open("C:\\Users\\J\\source\\repos\\aoc-2024\\Day8\\dayEightInput.txt") as file:
    for line in file:
        antennaMap.append(list(line.strip()))
        for point in antennaMap[len(antennaMap)-1]:
            if point not in antennas and point != '.':
                antennas.add(point)

def getLocations(point: chr):
    locations = []

    for y, row in enumerate(antennaMap):
        for x, pt in enumerate(row):
            if pt == point:
                locations.append(str(y) + "," + str(x))

    return locations

def getYXDelta(higherPoint, lowerPoint):
    point1 = stringLocationToIntList(higherPoint)
    point2 = stringLocationToIntList(lowerPoint)

    return [point1[0] - point2[0], point1[1] - point2[1]]
    
def isInBounds(y, x, matrix):
    return y >= 0 and x >= 0 and y < len(matrix) and x < len(matrix[0])

def stringLocationToIntList(location):
    return [int(x) for x in location.split(",")]

def intLocationToString(list):
    return str(list[0]) + "," + str(list[1])

for antenna in antennas:
    locationsOfAntenna = getLocations(antenna)
    for i in range(0, len(locationsOfAntenna)):
        for j in range(i+1, len(locationsOfAntenna)):
            delta = getYXDelta(locationsOfAntenna[i], locationsOfAntenna[j])

            hp = stringLocationToIntList(locationsOfAntenna[i])
            hp[0] = hp[0] + delta[0]
            hp[1] = hp[1] + delta[1]

            if isInBounds(hp[0], hp[1], antennaMap):
                antiNodes.add(intLocationToString(hp))

            lp = stringLocationToIntList(locationsOfAntenna[j])
            lp[0] = lp[0] - delta[0]
            lp[1] = lp[1] - delta[1]

            if isInBounds(lp[0], lp[1], antennaMap):
                antiNodes.add(intLocationToString(lp))

print(len(antiNodes))