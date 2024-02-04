T = int(input())

for NUM in range(T):
    k = int(input())
    n = int(input())

    people = []
    people = [num for num in range(1,n+1)]
    LIST=[]

    for i in range(k):
        LIST = [] 
        for j in range(n): 
            num = sum(people[:j+1])
            LIST.append(num)
        people = LIST
    
    print(people[-1])