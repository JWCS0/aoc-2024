testValues = []
operandsList = []
target = 0

with open("C:\\Users\\J\\source\\repos\\aoc-2024\\Day7\\daySevenInput.txt") as file:
    for line in file:
        result = line.split(':')[0].strip()
        operands = line.split(':')[1].strip().split(' ')
        testValues.append(int(result))
        operandsList.append([int(x) for x in operands])

def method(list: list, runningTotal, results: set, index):
    if index >= len(list) - 1:
        if index == len(list) - 1:
            results.add(runningTotal + list[index])
            results.add(int(f"{runningTotal}{list[index]}"))
            results.add(runningTotal * list[index] if runningTotal > 0 else list[index])
        else:
            results.add(runningTotal)
        return
    
    if runningTotal > target:
        return
    if index == 0:
        method(list, int(f"{list[index]}{list[index+1]}"), results, index + 2)
    else:
        method(list, int(f"{runningTotal}{list[index]}"), results, index + 1)
    method(list, runningTotal + list[index], results, index + 1)
    method(list, runningTotal * list[index] if runningTotal > 0 else list[index], results, index + 1)

def hasCombination(index):
    possibleResults = set()
    method(operandsList[index], 0, possibleResults, 0)
    return testValues[index] in possibleResults

total = 0

for i in range(0, len(testValues)):
    target = testValues[i]
    hasComb = hasCombination(i)
    total += testValues[i] if hasComb else 0

print("TOTAL:", total)

# 10 19
# => [10 + 19], [10 * 19]

# 81 40 27
# => [81 + 40 + 27], [81 * 40 + 27], [81 + 40 * 27], [81 * 40 * 27],
#    [81 + 27 + 40], [81 * 27 + 40], [81 + 27 * 40], [81 * 27 * 40],
# => [40 + 81 + 27], [40 * 81 + 27], [40 + 81 * 27], [40 * 81 * 27],
#    [40 + 27 + 81], [40 * 27 + 81], [40 + 27 * 81], [40 * 27 * 81],
# => [27 + 40 + 81], [27 * 40 + 81], [27 + 40 * 81], [27 * 40 * 81],
#    [27 + 81 + 40], [27 * 81 + 40], [27 + 81 * 40], [27 * 81 * 40]