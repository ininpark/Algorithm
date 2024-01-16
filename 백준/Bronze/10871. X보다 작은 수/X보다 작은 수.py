N,X = map(int,input().split())
N_num = list(map(int,input().split()))
result = []
for i in range(N):
    if X > N_num[i]:
        result.append(N_num[i])
for num in result:
    print(num,"",end='')