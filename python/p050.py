#!/usr/bin/env python3

from time import process_time

'''
The prime 41, can be written as the sum of six consecutive primes:
41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?

'''

def sieve1(max_n):
    prime = [True] * (max_n//2)
    for i in range(3, int(max_n**0.5)+1, 2):
        if prime[i//2]:
            prime[i*i//2::i] = [False] * ((max_n-i*i-1)//(2*i)+1)

    return [2] + [2*i+1 for i in range(1, max_n//2) if prime[i]]

MAX_N = 1000000

start = process_time()
primes = sieve1(MAX_N)
print('Sieve time: {}'.format(process_time()-start))

start = process_time()
global_max = 0
global_num = 0
# Start from smallest prime to largest prime
for i in range(0, len(primes)):
    # Check if max number of primes we can add is less than the largest
    # we already added together
    if len(primes)-i < global_max:
        break

    # Know it has to be at least global_max in length, so sum global_max terms
    # initially
    sum_cons = sum(primes[i:i+global_max])

    for j in range(global_max, len(primes)-i):
        # Add next consecutive term
        sum_cons += primes[i+j]

        # Bigger than largest prime, bad. Computing after this is wasteful
        if sum_cons > primes[len(primes)-1]:
            break

        # If we hit a prime, we know it's a larger sequential sum
        # Due to the initial sum out of the loop
        if sum_cons in primes:
            global_max = j+1
            global_num = sum_cons

print('Winner: {}, {}\nProcessing time: {}'.format(global_num, global_max, process_time()-start))
