#!/usr/bin/env python3

import itertools
from functools import reduce

'''
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of
each of the digits 0 to 9 in some order, but it also has a rather interesting
sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

    d2d3d4=406 is divisible by 2
    d3d4d5=063 is divisible by 3
    d4d5d6=635 is divisible by 5
    d5d6d7=357 is divisible by 7
    d6d7d8=572 is divisible by 11
    d7d8d9=728 is divisible by 13
    d8d9d10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
'''


pd_nums = []

# Need to generate all possible permutations of 0,1,2,3,4,5,6,7,8,9
nums = list(range(10))
all_perms = list(itertools.permutations(nums))

# Check that the permutations follow the rules listed above
for perm in all_perms:
    if (perm[3] % 2) != 0:
        continue
    if (reduce(lambda x,y: x*10+y, perm[2:5]) % 3) != 0:
        continue
    if (perm[5] % 5) != 0:
        continue
    if (reduce(lambda x,y: x*10+y, perm[4:7]) % 7) != 0:
        continue
    if (reduce(lambda x,y: x*10+y, perm[5:8]) % 11) != 0:
        continue
    if (reduce(lambda x,y: x*10+y, perm[6:9]) % 13) != 0:
        continue
    if (reduce(lambda x,y: x*10+y, perm[7:10]) % 17) != 0:
        continue

    pd_nums.append(reduce(lambda x,y: x*10+y, perm))


print('The winner is: {}'.format(sum(pd_nums)))
