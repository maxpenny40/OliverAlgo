#Program using Alex's Pseudocode

import random

TargetArray = [0,1,2,3,4,5,6,7,8,9]

RandomArray = random.shuffle(TargetArray)

print(RandomArray)

REPS = 0

while TargetArray != RandomArray:
    n = 0
    i=0
    while i <= REPS:
        if RandomArray[n] >= RandomArray[n+1]:
            temp = RandomArray[n]
            RandomArray[n] = RandomArray[n+1]
            RandomArray[n+1] = temp
            i += 0

#   This doesnt work
#   What is temp?
#   Doesn't swap positions
#   Target