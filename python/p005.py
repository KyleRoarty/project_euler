#!/usr/bin/env python3

from euler import *
from time import process_time

from functools import reduce

'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

start = process_time()

MAX_N = 20
primes = sieve1(MAX_N)
factors = []

for prime in primes:
    factor = prime
    while factor*prime <= MAX_N:
        factor *= prime
    factors.append(factor)

ans = reduce(lambda x,y: x*y, factors)
print('Winner: {}\nTime: {}'.format(ans, process_time()-start))
