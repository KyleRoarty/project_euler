#!/usr/bin/env python

import time

IN_ORDER = [[], ['1'], ['1', '2'], ['1', '2', '3'], ['1', '2', '3', '4'], ['1', '2', '3', '4', '5'],
            ['1', '2', '3', '4', '5', '6'], ['1', '2', '3', '4', '5', '6', '7'], ['1', '2', '3', '4', '5', '6', '7', '8'],
            ['1', '2', '3', '4', '5', '6', '7', '8', '9']]

def partialSieve(start, end, primes):
    skip = [0]*(end-start)

    for prime in primes:
        x = start + prime % start
        while x < start + len(skip):
            skip[x-start] = 1
            x += prime

    for i in range(0, len(skip)):
        if skip[i]:
            continue

        primes.append(i+start)

        j = (i+start)*(i+start)
        while j < start + len(skip):
            skip[j-start] = 1
            j += (i+start)

    return primes


start = time.clock()

primes = []
for i in range(2, 1000000000, 100000000):
    primes = partialSieve(i, i+100000000, primes)

for p in reversed(primes):
    sort_p = sorted(str(p))
    if sort_p == IN_ORDER[len(sort_p)]:
        print(p)
        break


end = time.clock()
print(end-start)

