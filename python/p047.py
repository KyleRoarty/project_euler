#!/usr/bin/env python3

from math import sqrt
from functools import reduce

'''
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
'''

def is_prime(n, primes):
    return n > 1 and all(n%i for i in primes)

# completely factors out d from n, returning -1 if not divisible
def factor_out(n, d):
    f = 0

    if n % d:
        return -1
    while not n % d:
        n /= d
        f += 1
    return d**f

NUM_FACT = 4

h_buff = [False]*NUM_FACT
p_list = [2, 3]
i = 3
while True:
    i += 1

    if is_prime(i, p_list):
        p_list.append(i)
        h_buff.remove(0)
        h_buff.append(False)
        continue

    p_tmp = list(map(lambda x: factor_out(i, x), p_list))
    p_fact = list(filter(lambda x: x > 0, p_tmp))

    if len(p_fact) == NUM_FACT and i == reduce(lambda x,y: x*y, p_fact):
        h_buff.pop(0)
        h_buff.append(True)
    else:
        h_buff.remove(0)
        h_buff.append(False)


    if all(h_buff):
        print('Winner: {}'.format(i-(NUM_FACT-1)))
        quit()
