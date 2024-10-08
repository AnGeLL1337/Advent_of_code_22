import sys
import math
from copy import deepcopy
from collections import defaultdict

infile = sys.argv[1] if len(sys.argv)>1 else 'Day11/Day11.txt'
data = open(infile).read().strip()
lines = [x for x in data.split('\n')]

M = []
OP = []
DIV = []
TRUE = []
FALSE = []

for monkey in data.split('\n\n'):
    id_, items, op, test, true, false = monkey.split('\n')
    print(id_, items, op, test, true, false)
    M.append([int(i) for i in items.split(':')[1].split(',')])
    words = op.split()
    op = ''.join(words[-3:])

    OP.append(lambda old,op=op:eval(op))
    DIV.append(int(test.split()[-1]))
    TRUE.append(int(true.split()[-1]))
    FALSE.append(int(false.split()[-1]))

START = deepcopy(M)


lcm = 1
for x in DIV:
    lcm = (lcm*x)
#print(len(str(lcm)))

for part in [1,2]:
    C = [0 for _ in range(len(M))]
    M = deepcopy(START)
    for t in range(20 if part==1 else 10000):
        for i in range(len(M)):
            for item in M[i]:
                #print(i,item)
                C[i] += 1
                item = OP[i](item)
                if part == 2:
                    item = item % lcm
                #print(i,item)
                if part == 1:
                    item = (item // 3)
                #print(i,item,item%DIV[i],TRUE[i],FALSE[i])
                if item % DIV[i] == 0:
                    #print(f'Item {item} thrown to {TRUE[i]}')
                    M[TRUE[i]].append(item)
                else:
                    #print(f'Item {item} thrown to {FALSE[i]}')
                    M[FALSE[i]].append(item)
            M[i] = []
    print(sorted(C)[-1] * sorted(C)[-2])