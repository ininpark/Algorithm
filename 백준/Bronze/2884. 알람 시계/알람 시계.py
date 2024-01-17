H,N = map(int,input().split())
time = H*60 + N
result = time - 45

if H != 0:
    print(result//60,result%60) #시간,분
else:
    if N >= 45:
        print(result//60,result%60)
    else:
        print(23,result%60)