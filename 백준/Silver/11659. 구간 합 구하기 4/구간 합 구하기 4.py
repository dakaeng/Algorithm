import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
sum_nums = []
total = 0
for n in nums :
  total += n
  sum_nums.append(total)

for _ in range(M) :
  i, j = map(int, input().split())
  if i > 1 :
    print(sum_nums[j-1] - sum_nums[i-2])
  else :
    print(sum_nums[j-1])