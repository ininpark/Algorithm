import sys
input = sys.stdin.readline
arr =[]

N = int(input()) 
for _ in range(N):
    x,y = map(int,input().split())
    arr.append([y,x])

arr.sort()

for putput in arr:
    print(putput[1],putput[0])