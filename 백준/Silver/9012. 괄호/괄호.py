T = int(input())

for i in range(T):
    INPUT = list(input())
    stack =[]
    NO = 0 
    for j in INPUT:
        if j == '(':
            stack.append(j)
        else:
            if len(stack) != 0:
                stack.pop()
            else:
                NO += 1
    if NO == 0 and len(stack) == 0:
        print('YES')
    else:
        print('NO')
            