stones = {3279:1, 998884:1, 1832781:1, 517:1, 8:1, 18864:1, 28:1, 0:1}

blinks = 75

for blink in range(0, blinks):
    newDictionary = {}
    print(blink)
    for stone in stones:
        stoneCount = stones[stone]
        if stone == 0:
            newDictionary[1] = newDictionary.get(1, 0) + stoneCount
        elif len(str(stone)) % 2 == 0:
            stoneString = str(stone)
            firstPart, secondPart = int(stoneString[:len(stoneString)//2]), int(stoneString[len(stoneString)//2:])
            newDictionary[firstPart] = newDictionary.get(firstPart, 0) + stoneCount
            newDictionary[secondPart] = newDictionary.get(secondPart, 0) + stoneCount
        else:
            newDictionary[stone*2024] = newDictionary.get(stone*2024, 0) + stoneCount
    
    stones = newDictionary

total = 0

for key in stones:
    total += stones[key]

print(total)

# 218956