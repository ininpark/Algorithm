import sys
R = int(input())

S_list =[]
for _ in range(R):
    N_list = sys.stdin.readline().split()
    if N_list[0] == "push":
        S_list.append(int(N_list[1]))
    elif N_list[0] == "pop":
        if len(S_list) == 0:
            print(-1)
        else:
            print(S_list.pop(0))
    elif N_list[0] == "size":
        print(len(S_list))
    elif N_list[0] == "empty":
        if len(S_list) == 0:
            print(1)
        else:
            print(0)
    elif N_list[0] == "front":
        if len(S_list) == 0:
            print(-1)
        else:
            print(S_list[0])
    elif N_list[0] == "back":
        if len(S_list) == 0:
            print(-1)
        else:
            print(S_list[-1])