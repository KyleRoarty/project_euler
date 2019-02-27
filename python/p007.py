#!/usr/bin/env python3

from euler import *
from time import process_time

'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''


start = process_time()

primes = [2]
count = 1
pot_p = 3

while count < 10001:
    if is_prime(pot_p, primes):
        primes.append(pot_p)
        count += 1
    pot_p += 2

print('Winner: {}\nTime: {}'.format(primes[10000], process_time()-start))
