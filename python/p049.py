#!/usr/bin/env python3

'''
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases
by 3330, is unusual in two ways:
(i) each of the three terms are prime, and
(ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?

'''


def e_sieve(max_n):
    to_sieve = list(range(2, max_n+1))
    primes = []

    while to_sieve:
        primes.append(to_sieve[0])
        to_sieve = list(filter(lambda x: x % to_sieve[0], to_sieve))

    return primes

# Get primes up to 9999
primes = e_sieve(9999)
# Filter out < 4-digit numbers
primes = list(filter(lambda x: x >= 1000, primes))

for prime in primes:
    if prime+3330 in primes and prime+6660 in primes:
        # Turn primes into lists
        l_prime = list(str(prime))
        l_prime2 = list(str(prime+3330))
        l_prime3 = list(str(prime+6660))

        # Sort for ease of comparison
        l_prime.sort()
        l_prime2.sort()
        l_prime3.sort()

        if l_prime == l_prime2 and l_prime == l_prime3:
            print('{}{}{}'.format(prime, prime+3330, prime+6660))
