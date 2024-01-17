N = int(input())

for i in range(N):
    NUM,STR = input().split()
    for j in list(STR):
        print(j*int(NUM),end='')
    print(end='\n')