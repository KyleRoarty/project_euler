#!/usr/bin/env python

import time

def repeatingSequence(numr, denr):
    nums = []
    in_dict = {}

    remainder = numr % denr

    while remainder != 0 and remainder not in in_dict:
        in_dict[remainder] = len(nums)

        remainder *= 10

        nums.append(int(remainder/denr))

        remainder %= denr

    return [] if remainder == 0 else nums[in_dict[remainder]:]

start = time.clock()

ret_rep_seq = []
max_len = 0
max_ind = 0

for i in range(1, 1001):
    rep_seq = repeatingSequence(1, i)
    if len(rep_seq) > max_len:
        max_len = len(rep_seq)
        ret_rep_seq = rep_seq
        max_ind = i


print("{}; {}, {}".format(max_ind, max_len, ret_rep_seq))

end = time.clock()
print(end-start)
