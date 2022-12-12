from collections import defaultdict

data = open("Day7/test.in").read()
lines = [x for x in data.split("\n")]

# print(lines)
PS = defaultdict(int)
path = []
for line in lines:
    words = line.strip().split()
    if words[1] == "cd":  # $ cd .. | cd <dir-name>
        if words[2] == "..":
            path.pop()
        else:
            path.append(words[2])  # $ cd <dir-name>
    elif words[1] == "ls":  # $ ls
        continue
    elif words[0] == "dir":  # $ dir <dir-name>
        continue
    else:
        size = int(words[0])
        for i in range(1, len(path) + 1):
            PS["/".join(path[:i])] += size

part_1 = 0
part_2 = []

disk_space = 70000000  # Defines in part 2
update_size = 30000000  # Defines in part 2
needed_space = disk_space - update_size


for key, value in PS.items():
    PS[key.replace("//", "/")] = value
    print(key, value)
    if value < 100000:
        part_1 += value
    if value > (PS["/"] - needed_space):
        part_2.append(value)


print(part_1)
print(min(part_2))
