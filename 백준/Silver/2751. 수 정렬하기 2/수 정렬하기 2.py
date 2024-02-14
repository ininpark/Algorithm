import sys
input=sys.stdin.readline

N = int(input())

nums =[]

for i in range(N):
    INPUT = int(input())
    nums.append(INPUT)
    
nums.sort()

for j in nums:
    print(j)