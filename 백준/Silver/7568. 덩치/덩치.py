N   = int(input())
cnt = [1]*N
nums = []

for _ in range(N):
    INPUT = list(map(int,input().split()))
    nums.append(INPUT)

for i in range(N):
    for j in range(N):
        if nums[i][0] < nums[j][0] and nums[i][1] < nums[j][1]:
            cnt[i]+=1

for _ in range(N):
    print(cnt[_],end=' ')