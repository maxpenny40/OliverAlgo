#Program using Max's Pseudocode

import random

n = 0
i = 0
numberlist = []

while n < random.randint(20,100):
    numberlist.append(random.randint(1,1000))
    n += 1

print('Inital List: \n'+str(numberlist)+'\n')

while i <= len(numberlist):
    decreaser = 1
    position = 0

    while position < (len(numberlist)-decreaser):
        if numberlist[position] > numberlist[position + 1]:
            numberlist[position], numberlist[position + 1] = numberlist[position + 1], numberlist[position]
        else:
            pass

        position += 1
    decreaser += 1
    i += 1

print('Final List: \n'+str(numberlist)+'\n')

for num in numberlist:
    print(num)

