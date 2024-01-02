from itertools import combinations

N, K = map(int, input().split())
x = [0] * N
y = [0] * N
for i in range(N) :
  x[i], y[i] = map(int, input().split())

answer = 1e10
for comb in combinations(range(N), K) :
  min_max = 0
  for i in range(N) :
    min_dist = 1e10
    for c in comb :
      dist = abs(x[i]-x[c]) + abs(y[i]-y[c])
      min_dist = min(min_dist, dist)
    min_max = max(min_max, min_dist)
  answer = min(answer, min_max)
print(answer)