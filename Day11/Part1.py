stones = [3279, 998884, 1832781, 517, 8, 18864, 28, 0]

blinks = 25

for _ in range(0, blinks):
    newStones = []

    for stone in stones:
        if stone == 0:
            newStones.append(1)
        elif len(str(stone)) % 2 == 0:
            stoneString = str(stone)
            firstPart, secondPart = stoneString[:len(stoneString)//2], stoneString[len(stoneString)//2:]
            newStones.append(int(firstPart))
            newStones.append(int(secondPart))
        else:
            newStones.append(int(stone) * 2024)

    stones = newStones

print(len(stones))