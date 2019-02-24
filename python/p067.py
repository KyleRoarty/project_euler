#!/usr/bin/env python3

import os
import csv

# Get input data from file
dname = os.path.dirname(__file__)
fname = os.path.join(dname, '../txt/p067_triangle.txt')

data = []

with open(fname, 'r') as f:
    csvreader = csv.reader(f, delimiter=' ')
    for row in csvreader:
        data.append([int(item) for item in row])

# Flip data to make things easier
data.reverse()

# Remember, range already does the len-1 thing
for i in range(1, len(data)):
    for j in range(0, len(data[i])):
        # Start at bottom, sum bigger number, and repeat
        # This could be recursive, couldn't it...
        data[i][j] += data[i-1][j] if data[i-1][j] > data[i-1][j+1] else data[i-1][j+1]

print('The winner: {}'.format(data[len(data)-1][0]))
