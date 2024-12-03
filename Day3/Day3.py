import re
pattern = "mul\([0-9]+,[0-9]+\)"

with open("C:\\Users\\J\\source\\repos\\aoc-2024\\Day3\\dayThreeInput.txt") as file:
        total = 0
        for line in file:
            for mul in re.findall(pattern, line):
                  numsWithComma = re.findall("\d+,\d+", mul)[0].split(',')
                  total += int(numsWithComma[0]) * int(numsWithComma [1])

        print(total)