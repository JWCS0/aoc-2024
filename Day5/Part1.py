orders = {}
sequences = []

with open("C:\\Users\\J\\source\\repos\\aoc-2024\\Day5\\Day5Input.txt") as file:
    readingOrders = True
    for line in file:
        if readingOrders and line == "\n":
            readingOrders = False
            continue
        if readingOrders:
            numbers = line.split('|')
            numbers = [x.strip() for x in numbers]
            if orders.get(numbers[1]) != None:
                temp = orders.get(numbers[1])
                temp.append(numbers[0])
                orders[numbers[1]] = temp
            else:
                orders[numbers[1]] = [numbers[0]]
        else:
            sequences.append(line.strip())

def isValid(sequence):
    preceders = set()
    for num in sequence.split(','):
        if num not in preceders:
            mustPrecedes = orders.get(num)
            if mustPrecedes != None:
                preceders.update(mustPrecedes)
        else:
            return False
    
    return True

def getMiddleValue(sequence):
    splitNums = sequence.split(',')

    return int(splitNums[len(splitNums)//2])

total = 0

for sequence in sequences:
    if (isValid(sequence)):
        total += getMiddleValue(sequence)

print(total)