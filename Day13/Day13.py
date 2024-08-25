from functools import cmp_to_key
FILE_NAME = "Day13/input.txt"
#FILE_NAME = "Day13/test2.txt"
PART_1 = 0
PART_2 = 1
data = open(FILE_NAME).read().strip()

def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left > right:
            return -1
        elif left < right:
            return 1
        else:
            return 0
    elif (isinstance(left, list)) and (isinstance(right, list)):
        i = 0
        while i < len(left) and i < len(right):
            tmp = compare(left[i], right[i])
            if tmp == -1:
                return -1
            if tmp == 1:
                return 1
            i += 1
        if i == len(left) and i < len(right):
            return 1 #-1
        elif i == len(right) and i < len(left):
            return -1 #1
        else:
            return 0
    elif isinstance(left, int) and isinstance(right, list):
        return compare([left], right)
    else:
        return compare(left, [right])

packets = []
for i, group in enumerate(data.split("\n\n")):
    left, right = group.split("\n")
    #print(type(left), type(right))
    left = eval(left)
    right = eval(right)
    packets.append(left)
    packets.append(right)
    if compare(left, right) == 1:
        PART_1 += 1 + i

packets.append([[2]])
packets.append([[6]])
packets = sorted(packets ,key=cmp_to_key(lambda x, y: compare(x, y)))
packets.reverse()
for i, packet in enumerate(packets):
    print(i, packet)
    if packet == [[2]] or packet == [[6]]:
        
        PART_2 *= i + 1
print(PART_1)
print(PART_2)
