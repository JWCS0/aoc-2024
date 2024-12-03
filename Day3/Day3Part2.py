import re
pattern = "mul\([0-9]+,[0-9]+\)"

doPattern = "do\(\)"
dontPattern = "don't\(\)"

def match(restOfString, lastMatch):
    doMatch = re.search(doPattern, restOfString)
    dontMatch = re.search(dontPattern, restOfString)

    if (doMatch == None and dontMatch == None):
        return lastMatch

    if (doMatch != None):
         return match(restOfString[doMatch.end():], True)
    else:
         return match(restOfString[dontMatch.end():], False)
    

with open("C:\\Users\\J\\source\\repos\\aoc-2024\\Day3\\dayThreeInput.txt") as file:
        total = 0
        enabled = True;

        for line in file:
            splits = re.split(pattern, line)
            matches = re.findall(pattern, line)
            numbers = [re.search("\d+,\d+", x).group() for x in matches]

            for i in range(0, len(numbers)): 
                enabled = match(splits[i], enabled)
                if (enabled):
                    splitNumbers = numbers[i].split(',')
                    total += int(splitNumbers[0]) * int(splitNumbers [1])

        print(total)