class Stack:
    def __init__(self):
        self.s_list =[]
    def push(self,data):
        self.s_list.append(data)
    def pop(self):
        if not self.isEmpty():
            self.s_list.pop()
    def isEmpty(self):
        return len(self.s_list) == 0
    def size(self):
        return len(self.s_list)

T = int(input())

for i in range(T):
    INPUT = list(input())
    stack = Stack()
    NO = 0 
    for j in INPUT:
        if j == '(':
            stack.push(j)
        else:
            if not stack.isEmpty():
                stack.pop()
            else:
                NO += 1
    if NO == 0 and stack.isEmpty():
        print('YES')
    else:
        print('NO')
            