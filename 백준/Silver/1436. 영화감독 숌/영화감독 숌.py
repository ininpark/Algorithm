import sys
cnt = 0
num = 666
N = int(sys.stdin.readline())

while True:
    if '666' in str(num):
        cnt +=1
        if cnt == N:
            print(num)
            break
        else:
            num+=1
    else:
        num += 1
