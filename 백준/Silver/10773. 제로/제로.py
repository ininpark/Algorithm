n = int(input())
stack = []

for i in range(n):
    INPUT = int(input())
    if INPUT == 0:
        stack.pop()
    else:
        stack.append(INPUT)

SUM = sum(stack)
print(SUM)
