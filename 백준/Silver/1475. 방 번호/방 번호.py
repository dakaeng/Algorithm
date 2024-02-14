import math

N = input()
nums = [0] * 9
for i in N :
  if i == '9' :
    i = '6'
  nums[int(i)] += 1

nums[6] = math.ceil(nums[6] / 2)
print(max(nums))