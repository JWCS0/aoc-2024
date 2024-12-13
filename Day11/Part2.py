stones = {3279:1, 998884:1, 1832781:1, 517:1, 8:1, 18864:1, 28:1, 0:1}

blinks = 75

for i in range(0, blinks):
    newDictionary = {}
    print(i)
    for stone in stones:
        for _ in range(0, stones[stone]):
            if stone == 0:
                newDictionary[1] = newDictionary.get(1, 0) + 1
            elif len(str(stone)) % 2 == 0:
                stoneString = str(stone)
                firstPart, secondPart = int(stoneString[:len(stoneString)//2]), int(stoneString[len(stoneString)//2:])
                newDictionary[firstPart] = newDictionary.get(firstPart, 0) + 1
                newDictionary[secondPart] = newDictionary.get(secondPart, 0) + 1
            else:
                newDictionary[stone*2024] = newDictionary.get(stone*2024, 0) + 1
    
    stones = newDictionary

total = 0

for key in stones:
    total += stones[key]

print(total)

# 218956