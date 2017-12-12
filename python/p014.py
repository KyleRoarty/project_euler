max_chain = 0
num = 0
## Maybe do DP instead?
for i in range(2,1000000):
    n = i
    chain = 1
    while n > 1:
        if n % 2 == 0:
            n = n/2
        else:
            n = 3*n+1
        chain += 1
    if chain > max_chain:
        max_chain = chain
        num = i

print num
