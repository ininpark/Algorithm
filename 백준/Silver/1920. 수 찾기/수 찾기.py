import sys
input = sys.stdin.readline
arr =[]
result = []

def binary_search(arr, key, low, high) :
    while (low <= high) :

        middle = (low + high) // 2
        if key == arr[middle]: 
            return '1'
        elif (key > arr[middle]):
            low = middle + 1
        else:
            high = middle - 1
    return '0'

N = int(input()) 
N_LIST = list(map(int,input().split()))

M = int(input())
M_LIST = list(map(int,input().split()))

low = 0
high = len(N_LIST)-1
N_LIST.sort()
for i in M_LIST:
    key = i
    SEARCH = binary_search(N_LIST, key, low, high)
    print(SEARCH)