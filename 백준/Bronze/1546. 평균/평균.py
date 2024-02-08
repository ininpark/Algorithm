N = int(input())
score = list(map(float,input().split()))

MAX = max(score)
INDEX = score.index(MAX)
result = []
num=0
AVX = 0

for i in range(N):
    num = (score[i]/MAX)*100
    result.append(num)

print(sum(result)/N)