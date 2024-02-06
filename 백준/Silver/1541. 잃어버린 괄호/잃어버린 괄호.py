func = input().split('-')
nums = []
for i in func :
  sum = 0
  temp = i.split('+')
  for j in temp :
    sum += int(j)
  nums.append(sum)
answer = nums[0]
for n in nums[1:] :
  answer -= n
print(answer)