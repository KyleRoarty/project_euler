def sieve1(max_n):
    prime = [True] * (max_n//2)
    for i in range(3, int(max_n**0.5)+1, 2):
        if prime[i//2]:
            prime[i*i//2::i] = [False] * ((max_n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in range(1, max_n//2) if prime[i]]

def is_prime(num, primes = None):
    if primes:
        return num > 1 and all(num % p for p in primes)
    else:
        return num > 1 and all(num % n for n in range(2, int(num**0.5)+1))
