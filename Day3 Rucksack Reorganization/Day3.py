def points(c):
    if 'a'<=c<='z':
        return ord(c) - 96 #Ascii of the lowercase alphabet is counted from 97 and we need count it from 1
    else:
        return ord(c) - 38 #Ascii of the uppercase alphabet is counted from 65 and we need count it from 27

part1 = 0
rucksacks = [line.strip() for line in open('Day3/3.in')]
for rusksack in rucksacks:
    firstComponent, secondComponent = rusksack[:len(rusksack)//2], rusksack[len(rusksack)//2:]
    commonChars = list(set(firstComponent)&set(secondComponent))
    part1 += points(min(commonChars))

print(part1)
#_________________________________________________________________________________________________________
part2 = 0
rucksacks = [line for line in open('Day3/3.in')]

i = 0
while(i < len(rucksacks)):
    for c in rucksacks[i]:
        if (c in rucksacks[i+1] and c in rucksacks[i+2]):
            part2 += points(c)
            break
    i += 3

print(part2)