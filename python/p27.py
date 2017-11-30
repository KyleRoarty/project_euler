#!/usr/bin/env python

import time

def lenFactors(n):
    return len(set([div for i in range(1, int(n**.5+1)) for div in ([i] if i == 1 else [i, n//i]) if not n % i]))

start = time.clock()

max_seq_primes = 0
prod_coef = 0

b_primes = [b for b in range(0, 1001) if lenFactors(b) == 1]

for a in range(-999, 1000):
    for b in b_primes:
        seq_primes = 0
        n = 0
        while True:
            value = n*n + a*n + b
            if value < 0:
                break
            if lenFactors(value) != 1:
                break
            seq_primes += 1
            n += 1
        if seq_primes > max_seq_primes:
            max_seq_primes = seq_primes
            prod_coef = a*b

print("{}, {}".format(prod_coef, max_seq_primes))

end = time.clock()
print(end-start)
