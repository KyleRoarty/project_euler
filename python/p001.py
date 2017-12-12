result = 0

for index in range(1,1000):
    if (index % 5 == 0 or index % 3 == 0):
        result += index

print result
