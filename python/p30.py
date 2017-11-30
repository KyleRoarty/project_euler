#!/usr/bin/env python

import time

def sumNums(n):
    if sum([int(d)**5 for d in str(n)]) == n:
        return True

    return False

start = time.clock()

print(sum([i for i in range(2, 1000000) if sumNums(i)]))

end = time.clock()
print(end-start)
