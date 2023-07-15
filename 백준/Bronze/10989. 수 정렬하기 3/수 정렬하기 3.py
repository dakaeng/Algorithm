import sys
input = sys.stdin.readline

N = int(input())

nums = [0 for i in range(10000)]
for n in range(N) :
    num = int(input())
    nums[num-1] += 1
for idx, count in enumerate(nums) :
    if count != 0 :
        for i in range(count) :
            print(idx + 1)