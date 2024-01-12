import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = [0]
for _ in range(N) :
  nums.append([0] + list(map(int, input().split())))

nums_sum = [[0] * (N+1) for _ in range(N+1)]
for i in range(1, N+1) :
  for j in range(1, N+1) :
    nums_sum[i][j] = nums[i][j]
    nums_sum[i][j] += nums_sum[i][j-1] + nums_sum[i-1][j]
    nums_sum[i][j] -= nums_sum[i-1][j-1]

for _ in range(M) :
  x1, y1, x2, y2 = map(int, input().split())
  sums = nums_sum[x2][y2]
  sums -= nums_sum[x2][y1-1]
  sums -= nums_sum[x1-1][y2]
  sums += nums_sum[x1-1][y1-1]
  print(sums)