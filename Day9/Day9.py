import sys

FILE_NAME = "Day9/Day9.txt"
FILE_NAME = "Day9/test.txt"


data = open(FILE_NAME).read().strip()
lines = [x for x in data.split('\n')]

head_x = head_y = tail_x = tail_y = 0

visited = {(0,0)}

def updtail():
	global tail_x, tail_y
	if tail_x == head_x and tail_y < head_y - 1:
		tail_y = head_y - 1
	elif tail_x == head_x and tail_y > head_y + 1:
		tail_y = head_y + 1
	elif tail_y == head_y and tail_x < head_x - 1:
		tail_x = head_x - 1
	elif tail_y == head_y and tail_x > head_x + 1:
		tail_x = head_x + 1
	elif tail_x != head_x and tail_y != head_y:
		dif_x = head_x - tail_x
		dif_y = head_y - tail_y
		abs_dif_x, abs_dif_y = abs(dif_x), abs(dif_y)
		sdx, sdy = dif_x // abs_dif_x, dif_y // abs_dif_y
		if abs_dif_x >= 2 or abs_dif_y >= 2:
			tail_x += sdx
			tail_y += sdy
	visited.add((tail_x, tail_y))


for line in lines:
    d, n = line.split(' ')

    if d == 'U':
	    for i in range(int(n)):
		    head_y -= 1
		    updtail()
    elif d == 'D':
        for i in range(int(n)):
            head_y += 1
            updtail()
    elif d == 'L':
        for i in range(int(n)):
            head_x -= 1
            updtail()
    elif d == 'R':
        for i in range(int(n)):
            head_x += 1
            updtail()

print(visited)

