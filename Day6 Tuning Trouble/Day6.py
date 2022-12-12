line = open("Day6/6.in").read()

for i in range(len(line)):
    if len(set(line[i - 4 : i])) == 4:
        print(f"Part 1: {i}")
        break


for i in range(len(line)):
    if len(set(line[i - 14 : i])) == 14:
        print(f"Part 2: {i}")
        break
