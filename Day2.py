notes = [line.strip() for line in open('Day2/2.in')]
part_1 = 0
part_2 = 0
for x in notes:
    enemy,me = x.split()
    part_1 += {'X': 1, 'Y': 2, 'Z': 3}[me]
    part_1 +=   {('A', 'X'): 3, ('A', 'Y'): 6, ('A', 'Z'): 0,
                ('B', 'X'): 0, ('B', 'Y'): 3, ('B', 'Z'): 6,
                ('C', 'X'): 6, ('C', 'Y'): 0, ('C', 'Z'): 3,
                }[(enemy, me)]

    part_2 += {'X': 0, 'Y': 3, 'Z': 6}[me]
    part_2 +=   {('A', 'X'): 3, ('A', 'Y'): 1, ('A', 'Z'): 2,
                ('B', 'X'): 1, ('B', 'Y'): 2, ('B', 'Z'): 3,
                ('C', 'X'): 2, ('C', 'Y'): 3, ('C', 'Z'): 1,
                }[(enemy, me)]
print(part_1)
print(part_2)