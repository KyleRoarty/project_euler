#!/usr/bin/env python3

from math import sqrt

'''
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×1**2
15 = 7 + 2×2**2
21 = 3 + 2×3**2
25 = 7 + 2×3**2
27 = 19 + 2×2**2
33 = 31 + 2×1**2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
'''

def isPrime(n, primes):
    return n > 1 and all(n%i for i in primes)

i = 1
p_list = []
while True:
    i += 2

    if isPrime(i, p_list):
        p_list.append(i)
        continue

    i_list = [(i-prime)/2 for prime in p_list]
    # Checks if i (after subtracting a prime, div by 2) is a square
    i_root = list(filter(lambda x: sqrt(x).is_integer() == True, i_list))

    # If it's 0, then i can't be made from a square
    if len(i_root) == 0:
        print('Winner: {}'.format(i))
        quit()
