import sys
input=sys.stdin.readline

N,M = map(int,sys.stdin.readline().split())
nums = list(map(int,sys.stdin.readline().split()))

S = 0
n_list = [0]

for i in nums:
    S += i
    n_list.append(S)

for cnt in range(M):
    i,j = map(int,sys.stdin.readline().split())
    print(n_list[j]-n_list[i-1])