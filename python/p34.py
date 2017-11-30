#!/usr/bin/env python

import time

def factorial(n):
    if n == 0:
        return 1

    return n*factorial(n-1)

start = time.clock()

fact_nums = 0

fact_list = []

for i in range(0, 10):
    fact_list.append(factorial(i))

for i in range(3, 1000000):
    if sum([fact_list[int(n)] for n in str(i)]) == i:
        fact_nums += i

print(fact_nums)
end = time.clock()
print(end-start)

