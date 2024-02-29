import sys
N = int(sys.stdin.readline()) 
num = [0] * 10001

for _ in range(N):
    INPUT = int(sys.stdin.readline())
    num[INPUT] = num[INPUT] + 1

for i in range(10001):
    if num[i] != 0:
        for j in range(num[i]):
            print(i)
