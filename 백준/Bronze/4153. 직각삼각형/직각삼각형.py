while True:
    A,B,C = map(int,input().split())
    if A == 0 and B == 0 and C ==0:
        break
    else:
        MAX = max(A,B,C)
        if MAX == A:
            result = B**2 + C**2 == A**2
        elif MAX == B:
            result = A**2 + C**2 == B**2
        else:
            result = A**2 + B**2 == C**2

    print( 'right' if result  else 'wrong')