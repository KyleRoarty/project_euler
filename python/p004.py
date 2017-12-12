result = 0
max_result = 0

for i in range(100,1000):
    for j in range(100,1000):
        result = str(i*j)
        is_pali = 1
        front = 0
        back = len(result)-1
        while front <= back:
            if result[front] <> result[back]:
                is_pali = 0
                break
            front+=1
            back-=1    
        if is_pali:
            if max_result < i*j:
                max_result = i*j
print max_result
        
