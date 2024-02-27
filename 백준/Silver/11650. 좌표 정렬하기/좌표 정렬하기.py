import sys
X_Y = []

N = int(sys.stdin.readline()) 

for _ in range(N):
    INPUT = list(map(int,sys.stdin.readline().split()))
    X_Y.append(INPUT)

X_Y.sort()
for i in X_Y:
    for j in i:
        print(j,end=' ')
    print(end = '\n')

