N = int(input())
nums = list(map(int, input().split()))
M = int(input())
check = list(map(int, input().split()))
nums.sort()

for c in check :
  start, end = 0, N - 1
  answer = 0
  while (start <= end) :
    mid = (start + end) // 2
    if nums[mid] < c :
      start = mid + 1
    elif nums[mid] > c :
      end = mid - 1
    else :
      answer = 1
      break
  print(answer)