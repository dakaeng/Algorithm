import sys
sys.setrecursionlimit(10**6)

N = int(input())
picture = []
for _ in range(N) :
  picture.append(list(input()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, c) :
  visited[x][y] = 1

  for i in range(4) :
    nx = x + dx[i]
    ny = y + dy[i]

    if (0 <= nx < N) and (0 <= ny < N) and visited[nx][ny] == 0 :
      if picture[nx][ny] == c :
        dfs(nx, ny, c)
        
# 색약이 아닌 사람
visited = [[0 for _ in range(N)] for _ in range(N)]
sum1 = 0

for c in ['R', 'G', 'B'] :
  for i in range(N) :
    for j in range(N) :
      if visited[i][j] == 0 and picture[i][j] == c :
        dfs(i, j, c)
        sum1 += 1
        
# 적록색약인 사람
for i in range(N) :
  for j in range(N) :
    if picture[i][j] == 'R' :
      picture[i][j] = 'G'
visited = [[0 for _ in range(N)] for _ in range(N)]
sum2 = 0

for c in ['G', 'B'] :
  for i in range(N) :
    for j in range(N) :
      if visited[i][j] == 0 and picture[i][j] == c :
        dfs(i, j, c)
        sum2 += 1
        
print(sum1, sum2)