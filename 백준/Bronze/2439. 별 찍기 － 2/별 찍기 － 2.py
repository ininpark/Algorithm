n = int(input())
star = '*'
space =' '

for i in range(1,n+1):
    num = n - (i)
    print(space*num,end='')
    print(star*i)