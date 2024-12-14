class Robot:
    X:int
    Y:int
    xVelocity:int
    yVelocity:int

    def __init__(self, X, Y, xVelocity, yVelocity):
        self.X = X
        self.Y = Y
        self.xVelocity = xVelocity
        self.yVelocity = yVelocity

    def __repr__(self):
        return "Position: " + str(self.X) + ", " + str(self.Y) + " | Velocity: " + str(self.xVelocity) + ", " + str(self.yVelocity)

robots = []
width = 101
height = 103

def printMap(map):
    mapString = ""
    map.reverse()
    for row in map:
        for spot in row:
            mapString += spot
        mapString += "\n"
    print(mapString.strip())

with open("Day14\input.txt", "r") as file:
    for line in file:
        position = line.split("=")[1].split("v")[0]
        xPosition = int(position.split(",")[0].strip())
        yPosition = int(position.split(",")[1].strip())

        velocity = line.split("=")[2]
        xVelocity = int(velocity.split(",")[0].strip())
        yVelocity = int(velocity.split(",")[1].strip())

        robots.append(Robot(xPosition, yPosition, xVelocity, yVelocity))

map = []

def resetMap(map:list):
    map.clear()
    for _ in range(0, height):
        map.append(["." for _ in range(0, width)])

def updateMap(map):
    for robot in robots:
        relativeY = height - robot.Y - 1
        map[relativeY][robot.X] = "O"

seconds = 0

def centerIsFilled(map):
    for i in range(0, height):
        if map[i][50] == '.':
            return False
    return True

resetMap(map)

while not centerIsFilled(map):
    resetMap(map)
    seconds += 1
    for robot in robots:
        robot.X = (robot.X + robot.xVelocity) % width
        robot.Y = (robot.Y + robot.yVelocity) % height

    updateMap(map)
    printMap(map)
    print(seconds,"\n")