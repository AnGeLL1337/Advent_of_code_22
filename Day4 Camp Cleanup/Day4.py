data = open('Day4/4.in').read().strip()
lines = [x for x in data.split('\n')]

part_1 = 0
part_2 = 0
for line in lines:
    left,right = line.split(',')
    left_l,left_r= left.split('-')
    right_l,right_r= right.split('-')

    left_l,left_r,right_l,right_r = [int(x) for x in [left_l,left_r,right_l,right_r]] #retyping to the int
    if (((left_l<=right_l) and (right_r<=left_r)) or ((right_l<=left_l) and (left_r<=right_r))):
        part_1 += 1

    if not (left_r < right_l or left_l > right_r):
        part_2 += 1
print(part_1)
print(part_2)