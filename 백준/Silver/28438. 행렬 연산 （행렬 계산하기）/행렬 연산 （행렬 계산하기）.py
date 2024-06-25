import sys
input = sys.stdin.readline

N, M, Q = map(int, input().split())
row = [0 for _ in range(N)]
col = [0 for _ in range(M)]

for _ in range(Q) :
  i, j, k = map(int, input().split())
  if i == 1 :
    r, v = j-1, k
    row[r] += v
  else :
    c, v = j-1, k
    col[c] += v

for i in range(N) :
  for j in range(M) :
    print(row[i] + col[j], end = ' ')
  print()