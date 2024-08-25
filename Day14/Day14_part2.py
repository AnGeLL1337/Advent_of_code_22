FILE_NAME = "Day14/input.txt"
#FILE_NAME = "Day14/test.txt"

data = open(FILE_NAME).read().strip()
lines = [line for line in data.split("\n")]

rocks = []
for line in lines:
    coords = line.strip().split("->")
    tmp = [coords.strip().split(",") for coords in coords]
    coords = [[int(x[0]), int(x[1])] for x in tmp]
    rocks.append(coords)

def process_rocks(coords):
    memory = set()
    min_y = 0
    for line in coords:
        for (x1, y1), (x2, y2) in zip(line, line[1:]):
            x1, x2 = sorted([x1, x2])
            y1, y2 = sorted([y1, y2])
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    memory.add((x, y))
                    if y + 1 > min_y:
                        min_y = y + 1
    return min_y, memory

def fall(min_y, memory, start):
    counter = 0
    while (start, 0) not in memory:
        s = (start, 0)
        while True:
            if s[1] >= min_y:
                break
            if (s[0], s[1] + 1) not in memory:   #Under
                s = (s[0], s[1] + 1)
                continue
            if (s[0] - 1, s[1] + 1) not in memory: #Left under
                s = (s[0] - 1, s[1] + 1)
                continue
            if (s[0] + 1, s[1] + 1) not in memory: #Right under
                s = (s[0] + 1, s[1] + 1)
                continue
            break
        memory.add(s)
        counter += 1
    return counter


min_y, memory = process_rocks(rocks)
print(fall(min_y, memory, 500))