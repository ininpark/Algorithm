n = int(input())
nums = list(map(int, input().split()))
cnt = 0
result = 0

for i in nums:
    cnt = 0
    for j in range(1,i+1):
        if i == 1:
            break
        elif i ==  j or i%j == 0:
            cnt += 1
        else:
            continue

    if cnt == 2:
        result += 1
    
print(result)        
    
