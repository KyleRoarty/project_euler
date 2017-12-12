import math
# a+b+c = 1000, a<b<c
# a^2+b^2 = c^2
# c = sqrt(a^2+b^2)
a = 1
b = 2

while True:
    c = math.sqrt(pow(a,2)+pow(b,2))
    if c == int(c):
        if a+b+c == 1000:
            print a*b*c
            break
    if a+b+c > 1000:
        a += 1
        b = a+1
    else:
        b +=1
        
