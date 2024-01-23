MAX = 0
num = []
while True:
    A,B,C = map(int,input().split())
    if A == 0 and B ==0 and C == 0:
        break
    else:
        num.append(A)
        num.append(B)
        num.append(C)
        for i in num:
            if MAX < i :
                MAX = i
            else:
                continue
        num.remove(MAX)
        if num[0]**2 + num[1]**2 == MAX**2:
            print('right')
        else:
            print('wrong')
    num = []
    MAX = 0