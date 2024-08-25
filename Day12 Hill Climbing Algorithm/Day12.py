from string import ascii_lowercase
from heapq import heappop, heappush

with open("Day12/Day12.txt") as input_file:
    lines = input_file.read().strip().split()

grid = [list(line) for line in lines]
row = len(grid)
col = len(grid[0])

#Define start and end coordinates
for i in range(row):
    for j in range(col):
        char = grid[i][j]
        if char == "S":
            start = i, j
        if char == "E":
            end = i, j

def height(s):
    if s in ascii_lowercase:
        return ascii_lowercase.index(s)
    if s == 'S':
        return 0
    if s == 'E':
        return 25


def get_neighbors(i, j, part):
        for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            ii = i + di
            jj = j + dj

            if not (0 <= ii < row and 0 <= jj < col):
                continue	# out of bounds
            # PART 1 
            if part == 1:
                if height(grid[ii][jj]) <= height(grid[i][j]) + 1:
                    yield ii, jj
            # PART 2
            else:
                if height(grid[ii][jj]) >= height(grid[i][j]) - 1:
                    yield ii, jj

#Dijkstra's algorithm

for part in [1, 2]:
    visited = [[False] * col for _ in range(row)]
    if part == 1:
        heap = [(0, start[0], start[1])]
    else:
        heap = [(0, end[0], end[1])]
    
    while True:
        
        steps, i, j = heappop(heap)
        #print(grid[i][j], steps)

        if visited[i][j]:
            continue
        visited[i][j] = True
        
        if part == 1:
            if(i, j) == end:
                print(steps)
                break
        else:
            if height(grid[i][j]) == 0:
                print(steps)
                break

        for ii, jj in get_neighbors(i, j, part):
            heappush(heap, (steps + 1, ii, jj))

