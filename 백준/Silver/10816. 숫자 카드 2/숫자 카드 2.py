import sys
INPUT = []
INPUT2 = []
DIC = {}
result = []

N = int(sys.stdin.readline()) 
INPUT = list(map(int,sys.stdin.readline().split()))

M = int(sys.stdin.readline()) 
INPUT2 = list(map(int,sys.stdin.readline().split()))

for _ in INPUT:
    if _ not in DIC.keys():
        DIC[_] = 1
    else:
        DIC[_] += 1

for OUTPUT in INPUT2:
    if OUTPUT not in DIC.keys():
        result.append(0)
    else:
        result.append(DIC[OUTPUT])

for __ in result:
    print(__,end=' ')