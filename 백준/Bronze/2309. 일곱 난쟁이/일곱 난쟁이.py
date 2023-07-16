nums = []
for i in range(9) :
    height = int(input())
    nums.append(height)
nums.sort()
sums = sum(nums)
for i in range(8) :
    if len(nums) == 9 :
        for j in range(i, 9) :
            if (sums - nums[i] - nums[j]) == 100 :
                del nums[i]
                del nums[j-1]
                break
    else :
        break
for num in nums :
    print(num)