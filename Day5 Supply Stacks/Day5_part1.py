import re
from collections import deque

data = open('Day5/5.in').read()

zadanie, prikazy = data.split("\n\n")
zadanie = zadanie.split("\n")
prikazy = prikazy.split("\n")

part_1: list[deque] = []

for x in range(max(row.count("[") for row in zadanie[:-1])):
    col = deque()
    index = x * 4 + 1

    for i in range(len(zadanie) - 1):
        ch = zadanie[i][index]
        if ch == " ":
            continue

        col.append(ch)

    part_1.append(col)

for prikaz in prikazy:
    move, zobrat_z, dat_do = map(int, re.findall(r'\d+', prikaz))

    for _ in range(move):
        part_1[dat_do - 1].appendleft(part_1[zobrat_z - 1].popleft())

print("".join(col[0] for col in part_1))
