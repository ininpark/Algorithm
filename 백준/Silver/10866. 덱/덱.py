import sys
from collections import deque
input = sys.stdin.readline

DEQUE = deque()
N =int(input())

for _ in range(N):
    INPUT = list(map(str,input().split()))
    if INPUT[0] == 'push_front':
        DEQUE.appendleft(int(INPUT[1]))
    elif  INPUT[0] == 'push_back':
        DEQUE.append(int(INPUT[1]))
    elif  INPUT[0] == 'pop_front':
        if len(DEQUE) == 0:
            print('-1')
        else:
            result = DEQUE.popleft()
            print(result)
    elif  INPUT[0] == 'pop_back':
        if len(DEQUE) == 0:
            print('-1')
        else:
            result2 = DEQUE.pop()
            print(result2)
    elif INPUT[0] == 'size':
        print(len(DEQUE))
    elif  INPUT[0] == 'empty':
        if len(DEQUE) == 0:
            print('1')
        else:
            print('0')
    elif INPUT[0] == 'front':
        if len(DEQUE) == 0:
            print('-1')
        else:
            print(DEQUE[0])
    else:
        if len(DEQUE) == 0:
            print('-1')
        else:
            print(DEQUE[-1])
