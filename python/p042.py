#!/usr/bin/env python

import time

def isTriangle(string):
    total = 0
    string = string.upper()
    for char in string:
        total += ord(char)-64

    solve = (1+8*total)**.5/2 -.5
    if solve == int(solve):
        return True

    return False

start = time.clock()

in_data = open('p042_words.txt', 'r').read().split(',')

total_tri = 0

for word in in_data:
    if isTriangle(word.strip("\"")):
        total_tri += 1

print(total_tri)

end = time.clock()
print(end-start)

