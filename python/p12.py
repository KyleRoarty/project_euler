import math
divisors = 1
n = 2
triangle = 1
while divisors < 500:
    triangle += n
    n += 1
    divisors = 2
    testNum = math.ceil(math.sqrt(triangle))
    for potDiv in range(1, int(testNum)):
        if triangle % potDiv == 0:
            divisors += 2

print triangle
