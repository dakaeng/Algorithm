while True :
  N, *nums = map(int, input().split())
  if not nums :
    break

  count = nums.count(0)

  nums.sort()
  num1 = []
  num2 = []
  for i in range(count, N) :
    if i % 2 == 0 :
      num1.append(nums[i])
    else :
      num2.append(nums[i])

  for _ in range(count) :
    if len(num1) < len(num2) :
      num1.insert(1, 0)
    elif len(num1) > len(num2) :
      num2.insert(1, 0)
    else :
      if num1 > num2 :
        num2.insert(1, 0)
      else :
        num1.insert(1, 0)

  print(int(''.join(map(str, num1))) + int(''.join(map(str, num2))))