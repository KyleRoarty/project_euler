nums = set()
val = 100
result = 0

for a in range(2, val+1):
    for b in range(2, val+1):
        result = pow(a,b)
        if result not in nums:
            nums.add(result)
        

print(len(nums))
