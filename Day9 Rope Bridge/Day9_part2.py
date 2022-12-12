FILE_NAME = "Day9 Rope Bridge/Day9.txt"
# FILE_NAME = "Day9 Day9 Rope Bridge/test2.txt"


data = open(FILE_NAME).read().strip()
lines = [x for x in data.split("\n")]

N = 10
rope = [[0, 0] for i in range(N)]
# print(rope)

visited = {(0, 0)}


def updtail():
    for i in range(1, N):
        updrope(i)
    # print(rope)
    visited.add(tuple(rope[-1]))


def updrope(i):
    # rope_y       rope_y           rope_x        rope_x
    if rope[i][0] == rope[i - 1][0] and rope[i][1] < rope[i - 1][1] - 1:
        rope[i][1] = rope[i - 1][1] - 1
    elif rope[i][0] == rope[i - 1][0] and rope[i][1] > rope[i - 1][1] + 1:
        rope[i][1] = rope[i - 1][1] + 1
    elif rope[i][1] == rope[i - 1][1] and rope[i][0] < rope[i - 1][0] - 1:
        rope[i][0] = rope[i - 1][0] - 1
    elif rope[i][1] == rope[i - 1][1] and rope[i][0] > rope[i - 1][0] + 1:
        rope[i][0] = rope[i - 1][0] + 1
    elif rope[i][0] != rope[i - 1][0] and rope[i][1] != rope[i - 1][1]:
        dif_x = rope[i - 1][0] - rope[i][0]
        dif_y = rope[i - 1][1] - rope[i][1]
        abs_dif_x, abs_dif_y = abs(dif_x), abs(dif_y)
        sdx, sdy = dif_x // abs_dif_x, dif_y // abs_dif_y
        if abs_dif_x >= 2 or abs_dif_y >= 2:
            rope[i][0] += sdx
            rope[i][1] += sdy


for line in lines:
    d, n = line.split(" ")

    if d == "U":
        for i in range(int(n)):
            rope[0][1] -= 1
            updtail()
    elif d == "D":
        for i in range(int(n)):
            rope[0][1] += 1
            updtail()
    elif d == "L":
        for i in range(int(n)):
            rope[0][0] -= 1
            updtail()
    elif d == "R":
        for i in range(int(n)):
            rope[0][0] += 1
            updtail()

print(len(visited))
