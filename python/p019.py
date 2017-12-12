#!/usr/bin/env python

# Count the number of Sundays that fell on the first of a month during the
# twentieth century (1 Jan 1901 to 31 Dec 2000)

MON_LEN_LY = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
MON_LEN = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

jan_1_1900 = 1 #Was on monday

num_sun = 0

is_sun = (jan_1_1900+365) % 7

for i in range(1901, 2001):
    is_ly = i % 4 == 0 and (i % 100 != 0 or i % 400 == 0)
    for j in range(0, 12):
        if is_sun == 0:
            num_sun += 1
        if is_ly:
            is_sun = (is_sun + MON_LEN_LY[j]) % 7
        else:
            is_sun = (is_sun + MON_LEN[j]) % 7

print(num_sun)
