from itertools import combinations

N,M = map(int,input().split())
INPUT = list(map(int,input().split()))
num = []
result = []

for i in combinations(INPUT, 3):
    SUM = sum(i)
    if SUM <= M:
        result.append(SUM)
print(max(result))