#!/usr/bin/env python

import time

def get(n):
    x = 9
    y = 1
    n -= 1
    while n > x:
        n -= x*y
        x = x*10
        y += 1

    z = n//y
    zz = 10**(y-1) + z
    return int(str(zz)[ n % y ])

start = time.clock()

ans2 = 1

for i in range(0, 7):
    ans2 *= get(10**i)

print("{}".format(ans2))

end = time.clock()
print(end-start)

