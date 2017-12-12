nums = [11,12,13,14,15,16,17,18,19,20]
x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
primes = [1][2][3][2,2][5][2,3][7][2,2,2][3,3][5,2][11][3,2,2]
         [13][7,2][5,3][2,2,2,2][17][3,3,2][19][5,2,2]
         2*2*2*2*19*17*13*11*7*5*3*3
check = False
num = 2520

while not check:
    num += 2
    for index in range(0,len(nums)):
        if num % nums[index] != 0:
            break
        if index == len(nums)-1:
            check = True

print num
