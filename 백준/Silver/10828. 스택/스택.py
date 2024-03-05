import sys

input = sys.stdin.readline 
LIST = []

N = int(input())
for _ in range(N):
    INPUT = list(map(str, input().split()))
    cmd = INPUT[0]

    if cmd == 'push':
        LIST.append(int(INPUT[1]))
    elif cmd == 'pop':
        if len(LIST) == 0:
            print(-1)
        else:
            print(LIST.pop())
    elif cmd == 'size':
        print(len(LIST))
    elif cmd == 'empty':
        if len(LIST) == 0:
            print(1)
        else:
            print(0)
    elif cmd == 'top':
        if len(LIST) == 0:
            print(-1)
        else:
            print(LIST[-1])
