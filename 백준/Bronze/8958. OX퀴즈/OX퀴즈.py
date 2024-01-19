n = int(input())
LIST = []

for i in range(n):
    cnt = 0
    result = 0
    INPUT = input()
    for j in INPUT:
        if j == 'O':
            cnt += 1
            result += cnt
        else:
            cnt = 0
    print(result)