Num_list = []
for i in range(9):
    INPUT = int(input())
    Num_list.append(INPUT)

MAX = max(Num_list)
print(MAX)
print(Num_list.index(MAX)+1)