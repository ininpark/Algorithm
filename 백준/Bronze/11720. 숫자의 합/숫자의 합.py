N = int(input())
N_list = list(input()) 
result = 0

num_int = list(map(int, N_list))

for j in num_int:
    result += j    
print(result)

