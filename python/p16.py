import numpy as np
# 2^10 * 2^10 * 2^10
# 1024^10^10
array = np.zeros(350);

for i in range(0,1000):
    for j  in range(0, len(array)-1):
        array[j] *= 2
        array[j+1] += int(array[j]/10)
        array[j] = array[j] % 10

result = 0
for i in range(0,len(array)):
    result += array[i]
