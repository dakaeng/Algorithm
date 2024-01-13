N, K = map(int, input().split())
temp = list(map(int, input().split()))
sums = []
total = 0
for t in temp :
  total += t
  sums.append(total)

result = sums[K-1]
for i in range(K, N) :
  result = max(result, sums[i] - sums[i-K])
print(result)