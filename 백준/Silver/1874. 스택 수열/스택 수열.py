import sys

stack = []
result = []  
num = 1  

N = int(sys.stdin.readline())

for _ in range(N):
    INPUT = int(sys.stdin.readline())
    while num <= INPUT:
        stack.append(num)
        result.append('+')
        num += 1

    if stack[-1] == INPUT:
        stack.pop()
        result.append('-')
    else:
        print('NO')
        sys.exit(0) 

for op in result:
    print(op)
