result =[]
cnt = 0 

for i in range(10):
    INPUT = int(input())
    num = INPUT%42

    if num not in result:
        cnt += 1
        result.append(num)
    else:
        continue
print(cnt)