x = 100

sq_sum = pow((x+1)*(x/2),2)

diff = sq_sum

for tmp in range(x,0,-1):
    diff -= pow(tmp,2)

print diff
