nums = []
for i in range(28) :
    n = int(input())
    nums.append(n)
n_sub = list( set([i for i in range(1, 31)]) - set(nums) )
n_sub.sort()
print(n_sub[0])
print(n_sub[1])