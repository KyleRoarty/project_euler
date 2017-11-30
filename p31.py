#!/usr/bin/env python

import time

goal=200
valueLUT = [200, 100, 50, 20, 10, 5, 2, 1]

def genTree(num, LUT):
    combs = 0
    for i in range(0, len(LUT)):
        if num + LUT[i] > goal:
            continue
        elif num + LUT[i] < goal:
            combs += genTree(num+LUT[i], LUT[i:])
        elif num + LUT[i] == goal:
            combs += 1

    return combs


start = time.clock()

numCombs = genTree(0, valueLUT)
print(numCombs)

end = time.clock()
print(end-start)
