def readFileToLists(filename, listOne, listTwo):
    with open(filename) as file:
        for line in file:
            separated = line.rstrip().split()
            listOne.append(int(separated[0]))
            listTwo.append(int(separated[1]))

def calculateDistance(listOne, listTwo):
    listOne.sort()
    listTwo.sort()

    distance = 0

    for i in range(0, len(listOne) - 1):
        distance += abs(listOne[i] - listTwo[i])

    return distance

listOne = []
listTwo = []
readFileToLists("C:/Users/J/source/repos/aoc-2024/Day1/dayOneInput.txt", listOne, listTwo)
print(calculateDistance(listOne, listTwo))