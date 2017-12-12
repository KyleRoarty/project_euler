import math
primes = [2,3,5,7,11,13]
total = 2+3+5+7+11+13
potPr = 15
while potPr < 2000000:
    index = 0
    test = math.floor(math.sqrt(potPr))
    for index in range(0,len(primes)):
        if potPr % primes[index] == 0:
            break
        if primes[index] > test:
            primes.append(potPr)
            total += potPr
            break
    potPr += 2
    if(potPr % 10000 == 1):
        print potPr
print total
