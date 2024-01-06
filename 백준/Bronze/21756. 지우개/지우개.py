N = int(input())
nums = [0] + [i for i in range(1, N+1)]

while True :
  if len(nums) == 2 :
    break
  temp = []
  for i in range(len(nums)) :
    if i % 2 == 0 :
      temp.append(nums[i])
  nums = temp
print(nums[1])