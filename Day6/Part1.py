grid = []

directions = {
    "N": [-1, 0],
    "E": [0,1],
    "S": [1, 0],
    "W": [0, -1]
}

symbol = {
    "N": "^",
    "E": ">",
    "S": "<",
    "W": "v"
}

class Guard:
    x:int = 0
    y:int = 0
    direction = "N"
    symbol = "^"

    def rotate(self):
        currentDirectionIndex = list(directions.keys()).index(self.direction)
        self.direction = list(directions.keys())[(currentDirectionIndex+1)%len(directions)]
        self.symbol = symbol[self.direction]

class Location:
    x:int = 0
    y:int = 0

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

guard = Guard()

with open("C:\\Users\\J\\source\\repos\\aoc-2024\\Day6\\daySixInput.txt") as file:
    for line in file:
        grid.append(list(line.strip()))
        if '^' in line:
            guard.y = len(grid) - 1
            guard.x = line.index('^')

def isInBounds(y, x):
    return y >= 0 and y < len(grid) and x >= 0 and x < len(grid[0])

def isGuardInBounds():
    return isInBounds(guard.y, guard.x)

count = 1
nextSquare = Location(0, 0)

while isGuardInBounds():
    nextSquare.y = guard.y + directions[guard.direction][0]
    nextSquare.x = guard.x + directions[guard.direction][1]

    if not isInBounds(nextSquare.y, nextSquare.x):
        break
    
    if grid[nextSquare.y][nextSquare.x] == '#':
        guard.rotate()
        continue

    if grid[nextSquare.y][nextSquare.x] == '.':
        count += 1
        grid[nextSquare.y][nextSquare.x] = guard.symbol
        grid[guard.y][guard.x] = ' '
    
    guard.y = nextSquare.y
    guard.x = nextSquare.x

print(count)