from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M) :
  u, v = map(int, input().split())
  graph[u].append(v)
  graph[v].append(u)
      
def bfs(v) :
  queue = deque([v])
  visited[v] = True
  while queue :
    v = queue.popleft()
    for i in graph[v] :
      if not visited[i] :
        queue.append(i)
        visited[i] = True
        
visited = [False] * (N+1)
count = 0
for i in range(1, N+1) :
  if not visited[i] :
    bfs(i)
    count += 1
print(count)