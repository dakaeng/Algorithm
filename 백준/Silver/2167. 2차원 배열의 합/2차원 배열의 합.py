N, M = map(int, input().split())
mat = []
for _ in range(N) :
  mat.append(list(map(int, input().split())))

K = int(input())
d = [[0 for _ in range(M+1)] for _ in range(N+1)]

# d[i][j] : (0, 0)부터 (i, j)까지의 합을 저장해놓기
for i in range(1, N+1) :
  for j in range(1, M+1) :
    d[i][j] = mat[i-1][j-1] + d[i][j-1] + d[i-1][j] - d[i-1][j-1]

for _ in range(K) :
  i, j, x, y = map(int, input().split())
  answer = 0
  print(d[x][y] - d[x][j-1] - d[i-1][y] + d[i-1][j-1])