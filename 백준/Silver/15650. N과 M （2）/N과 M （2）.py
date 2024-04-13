from itertools import combinations

N, M = map(int, input().split())
combs = list(combinations(range(1, N+1), M))
for c in combs :
  for i in c :
    print(i, end = ' ')