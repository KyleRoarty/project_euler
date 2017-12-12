primes = [2,3,5,7,11,13]
potPr = 15
count = 6
while count < 10001:
    index = 0
    for index in range(0,len(primes)):
        if potPr % primes[index] == 0:
            break
        if index == len(primes)-1:
            primes.append(potPr)
            count += 1
    potPr += 2
print primes[10000]
