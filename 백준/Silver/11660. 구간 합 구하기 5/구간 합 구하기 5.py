import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = [[0] * (N + 1)]

for _ in range(N):
    nums.append([0] + list(map(int, input().split())))

nums2 = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        nums2[i][j] = nums2[i-1][j] + nums2[i][j-1] - nums2[i-1][j-1] + nums[i][j]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    result = nums2[x2][y2] - nums2[x1-1][y2] - nums2[x2][y1-1] + nums2[x1-1][y1-1]
    print(result)
