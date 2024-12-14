import numpy as np

class Machine:
    buttonAIncreaseX:int
    buttonAIncreaseY:int
    buttonBIncreaseX:int
    buttonBIncreaseY:int
    xTarget:int
    yTarget:int

    def __init__(self, buttonAIncreaseX, buttonAIncreaseY, buttonBIncreaseX, buttonBIncreaseY, xTarget, yTarget):
        self.buttonAIncreaseX = buttonAIncreaseX
        self.buttonAIncreaseY = buttonAIncreaseY
        self.buttonBIncreaseX = buttonBIncreaseX
        self.buttonBIncreaseY = buttonBIncreaseY
        self.xTarget = xTarget
        self.yTarget = yTarget

    def __repr__(self):
        return "\nButton A: X+" + str(self.buttonAIncreaseX) + " , Y+" + str(self.buttonAIncreaseY) + "\nButton B: X+" + str(self.buttonBIncreaseX) + " , Y+" + str(self.buttonBIncreaseY) + "\nPrize: X=" + str(self.xTarget) + " , Y=" + str(self.yTarget) + "\n"

machines = []

with open("Day13\input.txt", "r") as file:
    buttonA = None
    buttonB = None
    prize = None

    for line in file:
        if line == "\n":
            continue

        if buttonA == None:
            buttonA = line.strip()
            continue

        if buttonB == None:
            buttonB = line.strip()
            continue

        if prize == None:
            prize = line.strip()

            aButtonX = int(buttonA.split("+")[1].split(",")[0].strip())
            aButtonY = int(buttonA.split("+")[2].strip())

            bButtonX = int(buttonB.split("+")[1].split(",")[0].strip())
            bButtonY = int(buttonB.split("+")[2].strip())

            a = prize.split("=")
            prizeX = int(prize.split("=")[1].split(",")[0].strip()) + 10000000000000
            prizeY = int(prize.split("=")[2].strip()) + 10000000000000

            machines.append(Machine(aButtonX, aButtonY, bButtonX, bButtonY, prizeX, prizeY))
            
            buttonA = None
            buttonB = None
            prize = None


def solve(machine:Machine):
    a = np.array([[machine.buttonAIncreaseX, machine.buttonBIncreaseX],[machine.buttonAIncreaseY, machine.buttonBIncreaseY]])
    b = np.array([machine.xTarget, machine.yTarget])

    return np.linalg.solve(a,b)

total = 0

for machine in machines:
    solution = solve(machine)
    if round(solution[0], 2).is_integer() and round(solution[1], 2).is_integer():
        total += solution[0]*3
        total += solution[1]

print(int(total))