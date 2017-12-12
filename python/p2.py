result = 0
fib_old = 1
fib_new = 2

while fib_new < 4000000:
    if(fib_new % 2 == 0):
        result += fib_new
    fib_new += fib_old
    fib_old = fib_new - fib_old

print result
