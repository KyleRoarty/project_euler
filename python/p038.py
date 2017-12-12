#!/usr/bin/env python

import time

start = time.clock()

max_num = 0

for i in range(1,100000):
    j = 2
    str_i = str(i)

    while len(str_i) <= 9:
        if len(str_i) == 9:
            if sorted(str_i) == ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                if int(str_i) > max_num:
                    max_num = int(str_i)
                    break
        str_i += str(i*j)
        j += 1

print(max_num)

end = time.clock()
print(end-start)

