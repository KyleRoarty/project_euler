#!/usr/bin/env python

f = open("p022_names.txt", "r")

list_names = f.read().split(',')

print(len(list_names))

list_names.sort()

total = 0
pos = 1
for name in list_names:
    tmp = sum([ord(x)-64 for x in name.upper() if x != '"'])*pos
    pos += 1
    total += tmp

print(total)
