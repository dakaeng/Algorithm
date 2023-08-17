import sys
input = sys.stdin.readline

N = int(input())
nums = []
num_dict = {}
for _ in range(N) :
    num = int(input())
    nums.append(num)
    if num in num_dict :
        num_dict[num] += 1
    else :
        num_dict[num] = 1

nums.sort()

print(round(sum(nums)/len(nums)))  # 산술평균
print(nums[len(nums)//2])  # 중앙값

num_dict_sort = dict(sorted(num_dict.items()))
mx = max(num_dict_sort.values())
max_nums = []
for i in num_dict_sort :
    if num_dict_sort[i] == mx :
        max_nums.append(i)

if len(max_nums) > 1 :  # 최빈값
    print(max_nums[1])
else :
    print(max_nums[0])
    
print(nums[-1]-nums[0])  # 범위