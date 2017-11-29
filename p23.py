#!/usr/bin/env python

def sumFactors(n):
    return sum(set([div for i in range(1, int(n**.5+1)) for div in [i, 0 if i == 1 else n//i] if not n % i]))


abundants = list()

for i in range(12, 28124):
    if sumFactors(i) > i:
        abundants.append(i)

LUT = set([i+j for i in abundants for j in abundants])

answer = 0

for i in range(1, 28123):
    if i not in LUT:
        answer += i


print(answer)
