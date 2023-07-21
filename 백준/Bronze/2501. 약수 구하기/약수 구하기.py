N, K = map(int, input().split())
nums = []
for i in range(1, N+1) :
    if N % i == 0 :
        nums.append(i)
nums.sort()
if len(nums) >= K :
    print(nums[K-1])
else :
    print(0)