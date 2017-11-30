#!/usr/bin/env python

import time
import math

PERM_LUT = [362880, 40320, 5040, 720, 120, 24, 6, 2, 1, 1]
start = time.clock()

permutation = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

goal = 1000000

for i in range(0, len(permutation)):
    swap = math.ceil(goal/PERM_LUT[i]) - 1
    tmp = permutation[swap+i]
    del permutation[swap+i]
    permutation.insert(i, tmp)
    goal -= PERM_LUT[i]*(swap)
    if goal <= 0:
        break

print(permutation)
end = time.clock()
print(end-start)
