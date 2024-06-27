nums = input()

N = 0  # 찾고자 하는 수
i = 0

while True :
  N += 1
  for n in str(N) :
    if nums[i] == n :
      i += 1
      if i >= len(nums) :
        print(N)
        break
  if i >= len(nums) :
    break