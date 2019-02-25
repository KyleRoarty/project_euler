#!/usr/bin/env python3

from time import process_time
from itertools import permutations
from functools import reduce

IN_ORDER = [[1], [1, 2], [1, 2, 3], [1, 2, 3, 4], [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7, 8],
            [1, 2, 3, 4, 5, 6, 7, 8, 9]]

IN_ORDER.reverse()

def isPrime(num):
    return num > 1 and all(num % n for n in range(2, int(num**0.5)+1))

start = process_time()
for order in IN_ORDER:
    all_perms = list(permutations(order))
    all_perms.reverse()
    num_perms = [reduce(lambda x,y: 10*x+y, perm) for perm in all_perms]
    for perm in num_perms:
        if isPrime(perm):
            print('Perm: {}, time: {}'.format(perm, process_time()-start))
            quit()
