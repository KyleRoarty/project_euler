#!/usr/bin/env python3

from euler import *
from time import process_time

'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

def next_prime():
    pot_p = primes[-1]+1

    while True:
        if is_prime(pot_p):
            primes.append(pot_p)
            return pot_p
        pot_p += 1

start = process_time()
primes = [2]
max_prime = 0
num = 600851475143
prime = 2

while num >= prime:
    while num % prime == 0:
        num /= prime
        if prime > max_prime:
            max_prime = prime
    prime = next_prime()
print('Winner: {}\nTime: {}'.format(max_prime, process_time()-start))
