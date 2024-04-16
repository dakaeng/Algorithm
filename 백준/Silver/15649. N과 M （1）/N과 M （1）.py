from itertools import permutations

N, M = map(int, input().split())
perms = list(permutations(range(1, N+1), M))
for p in perms :
  print(*p)