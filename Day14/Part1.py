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
seconds = 100

with open("Day14\input.txt", "r") as file:
    for line in file:
        position = line.split("=")[1].split("v")[0]
        xPosition = int(position.split(",")[0].strip())
        yPosition = int(position.split(",")[1].strip())

        velocity = line.split("=")[2]
        xVelocity = int(velocity.split(",")[0].strip())
        yVelocity = int(velocity.split(",")[1].strip())

        robots.append(Robot(xPosition, yPosition, xVelocity, yVelocity))

for robot in robots:
    robot.X = (robot.X + seconds*robot.xVelocity) % width
    robot.Y = (robot.Y + seconds*robot.yVelocity) % height

def getQuadrant(robot):
    midHeight = height//2
    midWidth = width//2
    if robot.X == midWidth or robot.Y == midHeight:
        return -1
    
    if robot.X < midWidth and robot.Y < midHeight:
        return 0
    
    if robot.X > midWidth and robot.Y < midHeight:
        return 1
    
    if robot.X < midWidth and robot.Y > midHeight:
        return 2
    
    if robot.X > midWidth and robot.Y > midHeight:
        return 3
    
    else:
        return -1
    
quadrantCount = [0, 0, 0, 0]

for robot in robots:
    quadrant = getQuadrant(robot)
    if quadrant != -1:
        quadrantCount[quadrant] += 1

total = 1

for quadrant in quadrantCount:
    total *= quadrant

print(total)