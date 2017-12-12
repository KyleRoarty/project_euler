#!/usr/bin/env python

import time
import itertools

def factors(n):
    return [[list(str(i)), list(str(n//i))] for i in range(1, int(n**.5+1)) if not n % i]

def checkUnique(l):
    if '0' in l[0]:
        return False
    if '0' in l[1]:
        return False
    if len(l[0]) != len(set(l[0])):
        return False
    if len(l[1]) != len(set(l[1])):
        return False
    if not set(l[0]).isdisjoint(l[1]):
        return False

    return True

def getProds(unique_list):
    total = 0

    for item in unique_list:
        num = int(''.join(item))
        facts = factors(num)

        for fact in facts:
            if not checkUnique(fact):
                continue
            if not set(fact[0]).isdisjoint(item):
                continue
            if not set(fact[1]).isdisjoint(item):
                continue

            if len(item)+len(fact[0])+len(fact[1]) == 9:
                total += num
                break

    return total


start = time.clock()

nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

total = 0

unique_list = itertools.permutations(nums, 4)

total += getProds(unique_list)

print(total)
end = time.clock()
print(end-start)

