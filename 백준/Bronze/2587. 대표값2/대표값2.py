nums = []
for i in range(5) :
    num = int(input())
    nums.append(num)
nums.sort()
print(int(sum(nums)/5))
print(nums[2])