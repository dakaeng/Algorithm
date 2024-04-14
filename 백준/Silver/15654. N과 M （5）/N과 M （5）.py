from itertools import permutations

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

combs = list(permutations(range(N), M))
for c in combs :
  for i in c :
    print(nums[i], end = ' ')
  print()