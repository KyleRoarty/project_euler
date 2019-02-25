#!/usr/bin/env python3

from time import process_time

'''
The prime 41, can be written as the sum of six consecutive primes:
41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?

'''

def e_sieve(max_n):
    prime = [True]*max_n
    p = 2

    while p*p <= max_n:
        if prime[p]:
            prime[2*p::p] = [False]*len(prime[2*p::p])
        p += 1

    return [n for n in range(2, max_n) if prime[n]]

MAX_N = 1000000

start = process_time()
primes = e_sieve(MAX_N)

for i in range(len(primes)-1, 1, -1):
    j = 0
    sum_cons = sum(primes[0:i-1])
    while j + i < len(primes):
        sum_cons += primes[i+j-1]

        if sum_cons > primes[len(primes)-1]:
            break

        if sum_cons in primes:
            print('Winner: {}, {}, {}\nTime: {}'.format(sum_cons, i, j, (process_time()-start)))
            quit()

        sum_cons -= primes[j]
        j += 1
