#!/usr/bin/env python

import time

start = time.clock()

num_arr = [0]*1001

a = 1
b = a

while a+b <= 1000:
    c = (a*a+b*b)**.5
    if c != int(c):
        if a+b+c > 1000:
            a += 1
            b = a
        else:
            b += 1
        continue

    c = int(c)

    if a+b+c > 1000:
        a += 1
        b = a
        continue

    num_arr[a+b+c] += 1
    b += 1

print(max(enumerate(num_arr), key=lambda v: v[1]))

end = time.clock()
print(end-start)

