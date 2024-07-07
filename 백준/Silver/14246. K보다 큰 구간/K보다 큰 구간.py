n = int(input())
nums = list(map(int, input().split()))
k = int(input())

left, right = 0, 0
sum = 0
count = 0

while (left <= right) :
  if sum > k :
    count += (n - right + 1)
    sum -= nums[left]
    left += 1
  elif right == n :
    break
  else :  # sum <= k
    sum += nums[right]
    right += 1
print(count)