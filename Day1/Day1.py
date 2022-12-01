import sys

infile = sys.argv[1] if len(sys.argv)>1 else 'Day1/1.in'

temp = 0
top = [0, 0, 0]
for line in open(infile):  

    if(line == "\n"):
        if(temp > (min(top))):
            top[top.index(min(top))] = temp
        temp = 0
    else:
        temp += int(line)

print(max(top)) #Part 1
print(sum(top)) #Part 2