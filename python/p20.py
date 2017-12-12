import math

x = math.factorial(100)
total = 0
while x > 0:
    total += x % 10
    x /= 10

print total
