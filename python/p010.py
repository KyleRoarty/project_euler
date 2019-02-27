#!/usr/bin/env python3

from euler import *
from time import process_time
from functools import reduce

'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

start = process_time()

MAX_N = 2000000
primes = sieve1(MAX_N)

total = reduce(lambda x,y: x+y, primes)

print('Winner: {}\nTime: {}'.format(total, process_time()-start))
