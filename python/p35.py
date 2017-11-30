#!/usr/bin/env python

import time


goal = 1000000
def anyFactors(n):
    return len([div for i in range(1, int(n**.5+1)) for div in [i, n//i] if not n % i]) > 2


start = time.clock()

primes = []

circ_primes = []

do_these = [1]*goal

for i in range(2, goal):
    if not do_these[i]:
        continue

    if anyFactors(i):
        continue

    cp = True
    str_i = str(i)
    teststr = str_i[1:]+str_i[:1]
    add_list = [i]
    while teststr != str_i:
        if anyFactors(int(teststr)):
            add_list = [i]
            cp = False
            break
        add_list.append(int(teststr))
        teststr = teststr[1:]+teststr[:1]

    if cp:
        circ_primes.extend(add_list)
        for x in add_list:
            do_these[x] = 0

    for val in add_list:
        tmp = val*val
        while val < goal:
            do_these[val] = 0
            val += val

print(len(circ_primes))
end = time.clock()
print(end-start)

