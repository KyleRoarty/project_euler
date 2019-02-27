#!/usr/bin/env python3

from euler import *
from time import process_time

'''
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
'''

start = process_time()

primes = sieve1(1000000)
circ_primes = 0

for prime in primes:
    str_p = str(prime)
    rot_p = str_p[1:]+str_p[:1]
    circ = True

    while rot_p != str_p:
        if not is_prime(int(rot_p)):
            circ = False
            break
        rot_p = rot_p[1:]+rot_p[:1]

    if circ:
        circ_primes += 1

print('Winner: {}\nTime: {}'.format(circ_primes, process_time()-start))
