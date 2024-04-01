N, M = map(int, input().split())
maps = []

for _ in range(N) :
  maps.append(list(map(int, input().split())))  # 0 : 바다, 1 : 땅

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 모든 섬에 번호 붙이기 : bfs
from collections import deque

visited = [[False] * M for _ in range(N)]

def numbering(x, y, number) :
  queue = deque()
  queue.append([x, y])
  maps[x][y] = number
  visited[x][y] = True
  while queue :
    x, y = queue.popleft()
    for i in range(4) :
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < N and 0 <= ny < M :
        if maps[nx][ny] and not visited[nx][ny] :
          maps[nx][ny] = number
          visited[nx][ny] = True
          queue.append([nx, ny])

number = 1
for i in range(N) :
  for j in range(M) :
    if maps[i][j] and not visited[i][j] :
      numbering(i, j, number)
      number += 1
        
# 좌표 탐색해가며 다리 만들기
def bridge(a, b, num) :
  queue = deque()

  # 한 방향으로만 이동
  for i in range(4) :
    queue.append([a, b])
    visited = [[False] * M for _ in range(N)]
    length = [[0] * M for _ in range(N)]  # 다리 길이 저장
    visited[a][b] = True

    while queue :
      x, y = queue.popleft()
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < N and 0 <= ny < M :
        if not visited[nx][ny] :
          if maps[nx][ny] == 0 :  # 바다인 경우 다리 생성
            length[nx][ny] = length[x][y] + 1
            queue.append([nx, ny])
          elif maps[nx][ny] != num and length[x][y] >= 2:  # 현재 섬의 번호와 다르고, 다리 길이가 2 이상이면 (다리길이, 섬1 번호, 섬2 번호)를 edges에 저장
            edges.append((length[x][y], num, maps[nx][ny]))
            
edges = []  # 모든 간선을 담을 리스트 (length, 섬1, 섬2)

for i in range(N) :
  for j in range(M) :
    num = maps[i][j]
    if num != 0 :
      bridge(i, j, num)
edges.sort()

# 크루스칼 알고리즘으로 모든 섬 연결하는 최소 다리 길이 합 구하기
def find_parent(parent, x) :
  if parent[x] != x :
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

def union_parent(parent, a, b) :
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b :
    parent[b] = a
  else :
    parent[a] = b
    
parent = [0] * (number)
for i in range(1, number) :
  parent[i] = i

result = 0

count = 1
for edge in edges :
  length, a, b = edge
  if find_parent(parent, a) != find_parent(parent, b) :
    union_parent(parent, a, b)
    result += length
    count += 1

if count != (number - 1) :
  print(-1)
else :
  print(result)