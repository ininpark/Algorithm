N,K = map(int,input().split())

num1 = 1
num2 = 1
num3 = 1

for i in range(1,N+1):
    num1 = num1*i

for j in range(1,K+1):
    num2 = num2*j

for _ in range(1,(N-K+1)):
    num3 = num3*_

result = num1/(num2*num3)

print(int(result))
