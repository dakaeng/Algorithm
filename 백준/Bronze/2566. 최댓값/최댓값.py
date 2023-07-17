max_num = 0
for i in range(9) :
    nums = list(map(int, input().split()))
    if max(nums) >= max_num :
        max_num = max(nums)
        xy = [i+1, (nums.index(max_num)+1)]
print(max_num)
print(*xy)