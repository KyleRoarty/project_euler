total = 0
for num in range(1, 1001):
    total = total + pow(num, num)

print(total % 10000000000)
