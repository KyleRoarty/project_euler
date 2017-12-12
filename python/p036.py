#!/usr/bin/env python

import time
import math

def isPalindrome(str_in):
    str_len = len(str_in)
    str_mid = math.floor(str_len/2)
    if str_len & 1:
        if str_in[:str_mid] != str_in[:str_mid:-1]:
            return False
    else:
        if str_in[:str_mid] != str_in[:str_mid-1:-1]:
            return False

    return True

start = time.clock()

goal = 1000000
total = 0

for i in range(1, goal):
    if isPalindrome(str(i)) and isPalindrome("{0:b}".format(i)):
        total += i

print(total)
end = time.clock()
print(end-start)

