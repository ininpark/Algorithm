import sys
input=sys.stdin.readline

N = int(input())
P = []
num = 0
result = []

P = list(map(int,input().split()))

P.sort()

for j in P:
    num = num+j
    result.append(num)


print(sum(result))
