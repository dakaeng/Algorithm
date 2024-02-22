from collections import deque

N = int(input())
graph = []
for _ in range(N) :
  graph.append(list(map(int, input())))

# 상하좌우 움직임
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs_find(x, y) :
  house_sum = 1
  queue = deque()
  queue.append([x, y])
  graph[x][y] = 0
  while queue :
    x, y = queue.popleft()
    for i in range(4) :
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < N and 0 <= ny < N :
        if graph[nx][ny] == 1 :
          graph[nx][ny] = 0
          queue.append([nx, ny])
          house_sum += 1
  answer.append(house_sum)

count = 0
answer = []
for i in range(N) :
  for j in range(N) :
    if graph[i][j] == 1 :
      bfs_find(i, j)
      count += 1
answer.sort()

print(count)
for i in answer :
  print(i)