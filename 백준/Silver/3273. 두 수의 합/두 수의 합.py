import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
x = int(input())

nums.sort()

count = 0
left = 0
right = n-1
while (left < right) :
  a = nums[left]
  b = nums[right]
  if (a + b) == x :
    count += 1
    left += 1
  elif (a + b) > x :
    right -= 1
  else :
    left += 1
print(count)