N = int(input())
nums = []
for n in range(N) :
    num = int(input())
    nums.append(num)
nums.sort()
for i in nums :
    print(i)