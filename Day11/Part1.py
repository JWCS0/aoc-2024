stones = [3279]

blinks = 25

for _ in range(0, blinks):
    for i, stone in enumerate(stones):
        if stone == 0:
            stones[i] += 1
        elif len(str(stone)) % 2 == 0:
            stoneString = str(stone)
            first_part, second_part = stoneString[:len(stoneString)//2], stoneString[len(stoneString)//2:]
            stones[i] = first_part
            stones.insert(i+1, second_part)
        else:
            stones[i] = int(stone)*2024

print(len(stones))