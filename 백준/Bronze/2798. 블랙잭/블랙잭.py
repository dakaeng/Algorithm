N, M = map(int, input().split())
nums = list(map(int, input().split()))

sums = []
for i in range(N-2) :
    for j in range(i+1, N-1) :
        for k in range(j+1, N) :
            sum = nums[i] + nums[j] + nums[k]
            diff = M - sum
            if diff >= 0 :
                sums.append([sum, diff])
sums.sort(key = lambda x: x[1])
print(sums[0][0])