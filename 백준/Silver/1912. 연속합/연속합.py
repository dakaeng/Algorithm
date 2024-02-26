n = int(input())
nums = list(map(int, input().split()))
max_sum = [0] * n
max_sum[0] = nums[0]
for i in range(1, n) :
  max_sum[i] = max(max_sum[i-1] + nums[i], nums[i])
print(max(max_sum))