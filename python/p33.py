#!/usr/bin/env python

import time

def gcd(a, b):

    while b:
        a, b = b, a % b

    return a

start = time.clock()

nt_list = [1, 1]

# i is denom, j is num
for i in range(11,100):
    i_l = list(str(i))
    for j in range(10, i):
        val = j / float(i)
        i_list = list(i_l)
        j_list = list(str(j))

        char = [x for x in j_list if x in i_list]
        if char == []:
            continue

        if char[0] == '0':
            continue
        else:
            i_list.remove(char[0])
            j_list.remove(char[0])
            try:
                if int(j_list[0])/float(i_list[0]) == val:
                    nt_list[0] *= int(j_list[0])
                    nt_list[1] *= int(i_list[0])
            except ZeroDivisionError:
                pass



print([a/b for a,b in zip(nt_list, [gcd(nt_list[0], nt_list[1])]*len(nt_list))])
end = time.clock()
print(end-start)

