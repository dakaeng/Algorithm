from collections import deque
import sys
input = sys.stdin.readline

M, N = map(int, input().split())
tomato = []
for _ in range(N) :
  tomato.append(list(map(int, input().split())))

queue = deque()

for i in range(N) :
  for j in range(M) :
    if tomato[i][j] == 1 :
      queue.append([i, j])
    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs() :
  while queue :
    x, y = queue.popleft()
    for i in range(4) :
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < N and 0 <= ny < M and tomato[nx][ny] == 0 :
        tomato[nx][ny] = tomato[x][y] + 1
        queue.append([nx, ny])
        
bfs()
answer = 0
for i in range(N) :
  for j in range(M) :
    if tomato[i][j] == 0 :
      print(-1)
      exit()
  answer = max(max(tomato[i]), answer)
print(answer - 1)