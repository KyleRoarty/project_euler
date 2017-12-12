def next_prime():
    index = max(next_prime.primes)+1
    while 1==1:
        for potPrime in range(0,len(next_prime.primes)):
            if index % next_prime.primes[potPrime] == 0:
                break
            if potPrime == len(next_prime.primes)-1:
                next_prime.primes.append(index)
                return index
        index += 1

next_prime.primes = [2]
max_prime = 0
num = 600851475143
prime = 2

while num >= prime:
    while num % prime == 0:
        num /= prime
        print prime
        if prime > max_prime:
            max_prime = prime
    prime = next_prime()
