N = int(input())
nums = dict()
for _ in range(N) :
  num = int(input())
  if num in nums :
    nums[num] += 1
  else :
    nums[num] = 1
    
print(sorted(nums.items(), key = lambda x: (x[1], -x[0]), reverse = True)[0][0])