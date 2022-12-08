import sys
import itertools
from collections import defaultdict, Counter, deque

infile = sys.argv[1] if len(sys.argv)>1 else 'Day8/8.in'
Trees = []
for line in open(infile):
    Trees.append([int(x) for x in list(line.strip())])

part_1 = 0
part_2 = 0


part_1 = len(Trees)* 2 +  len(Trees[0] * 2) - 4


for i in range(1, len(Trees) - 1):
    for j in range(1, len(Trees[i]) - 1):
        lower = False
        assigned = False
        for x in range(0, j):                #left
            #print(Trees[i][x], Trees[i][j])
            if Trees[i][x] < Trees[i][j]:
                lower = True
            else :
                lower = False
                #print("Tree" , Trees[i][j], i ,j)
                break
            
        
        if lower == True and assigned == False:
            print("LEFT", Trees[i][j], i, j)
            part_1 += 1
            assigned = True
        else:
            for x in range(j + 1, len(Trees[i])): #right
                #print( Trees[i][j], Trees[i][x])
                if Trees[i][j] > Trees[i][x] :
                    lower = True
                else :
                    lower = False
                    #print("Tree" , Trees[i][j], i ,j)
                    break
        if lower == True and assigned == False:
            print("RIGHT", Trees[i][j], i, j)
            part_1 += 1
            assigned = True
        
        else:
            for x in range(0, i):                #up
                #print(Trees[x][j], Trees[i][j])
                
                if Trees[x][j] < Trees[i][j]:
                    lower = True
                else :
                    lower = False
                    break
        
        if lower == True and assigned == False:
            print("UP", Trees[i][j], i, j)
            part_1 += 1
            assigned = True
        else:                                   #down

            for x in range(i + 1, len(Trees)):
                #print(Trees[i][j], Trees[x][j])
                if Trees[i][j] > Trees[x][j]:
                    lower = True
                else:
                    lower = False
                    break
        if lower == True and assigned == False:
            print("DOWN", Trees[i][j], i, j)
            part_1 += 1
            assigned = True

    

print(part_1)
