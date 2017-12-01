#!/usr/bin/env python

import time

def anyFactors(n):
    return len([div for i in range(1, int(n**.5+1)) for div in [i, n//i] if not n % i]) > 2

def truncPrimeRight(n):
    if n == 0:
        return False
    if n == 1:
        return False

    if anyFactors(n):
        return False

    if len(str(n)) == 1:
        return True

    return truncPrimeRight(n//10)

def truncPrimeLeft(n):
    if n == 0:
        return False
    if n == 1:
        return False

    if anyFactors(n):
        return False

    if len(str(n)) == 1:
        return True

    return truncPrimeLeft(n % 10 ** (len(str(n))-1))


start = time.clock()

goal = 10000000
tp_list = []

for i in range(11, goal, 2):
    if truncPrimeRight(i) and truncPrimeLeft(i):
        tp_list.append(i)
        if len(tp_list) == 11:
            print(i)
            break

print(len(tp_list))
print(sum(tp_list))

end = time.clock()
print(end-start)

