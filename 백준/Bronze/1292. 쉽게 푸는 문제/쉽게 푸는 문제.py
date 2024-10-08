A, B = map(int, input().split())
nums = []
for i in range(1, 2*B) :
  nums.extend([i] * i)
print(sum(nums[(A-1):B]))