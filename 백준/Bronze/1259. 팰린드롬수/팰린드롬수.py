class Stack:
    def __init__(self):
        self.LIST = []
    def push(self,data):
        self.LIST.append(data)
    def pop(self):
        if not self.IsEmpty():
            return self.LIST.pop(-1)
    def IsEmpty(self):
        return len(self.LIST) == 0
    def size(self):
        return len(self.LIST)
    def clear(self):
        self.LIST = []

STACK = Stack()    
            
while True:
    STACK.clear()
    INT_INPUT = int(input())
    INPUT = list(str(INT_INPUT))
    if INT_INPUT == 0:
        break
    else:
        for i in INPUT:
            STACK.push(i)
        
        for j in INPUT:
            if not j == STACK.pop():
                print('no')
                break

            if STACK.IsEmpty():
                print('yes')
            