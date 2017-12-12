#!/usr/bin/env python

def sumFactors(n):
    return sum(set([div for i in range(1, int(n**.5+1)) for div in [i, 0 if i == 1 else n//i] if not n % i]))

num_dict = dict()

for i in range(1, 10001):
    tmp = sumFactors(i)
    if tmp != i:
        num_dict[i] = tmp

num_sum = 0

for i in range(1, 10001):
    try:
        if num_dict[num_dict[i]] == i:
            num_sum += i + num_dict[i]
            del num_dict[num_dict[i]]
            del num_dict[i]
    except:
        pass

print(num_sum)
