N = int(input())
result = []
for i in range(N):
    A,B = map(int,input().split())
    Num = A + B
    result.append(Num)

for j in range(N):
    print(result[j])