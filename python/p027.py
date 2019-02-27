#!/usr/bin/env python3

from euler import *
from time import process_time

'''
Euler discovered the remarkable quadratic formula:

n2+n+41

It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39
. However, when n=40,402+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,412+41+41

is clearly divisible by 41.

The incredible formula n2−79n+1601
was discovered, which produces 80 primes for the consecutive values 0≤n≤79

. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

    n2+an+b

, where |a|<1000 and |b|≤1000

where |n|
is the modulus/absolute value of n
e.g. |11|=11 and |−4|=4

Find the product of the coefficients, a
and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0.
'''

start = process_time()
max_seq_primes = 0
prod_coef = 0

b_primes = sieve1(1001)

for a in range(-999, 1000):
    for b in b_primes:
        seq_primes = 0
        n = 0
        while True:
            value = n*n + a*n + b
            if value < 0 or not is_prime(value):
                break
            seq_primes += 1
            n += 1
        if seq_primes > max_seq_primes:
            max_seq_primes = seq_primes
            prod_coef = a*b

print("Winner: {}\tTime: {}".format(prod_coef, process_time()-start))
