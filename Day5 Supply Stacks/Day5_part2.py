import re
from collections import deque

data = open('Day5/5.in').read()

zadanie, prikazy = data.split("\n\n")
zadanie = zadanie.split("\n")
prikazy = prikazy.split("\n")

part_2: list[deque] = []

for x in range(max(row.count("[") for row in zadanie[:-1])):
    col = deque()
    index = x * 4 + 1

    for i in range(len(zadanie) - 1):
        ch = zadanie[i][index]
        if ch == " ":
            continue

        col.append(ch)

    part_2.append(col)


for prikaz in prikazy:
    move, zobrat_z, dat_do = map(int, re.findall(r'\d+', prikaz))
    temp = deque()

    for _ in range(move):
        temp.appendleft(part_2[zobrat_z - 1].popleft())

    for crate in (temp):
        part_2[dat_do - 1].appendleft(crate)

print("".join(col[0] for col in part_2))
