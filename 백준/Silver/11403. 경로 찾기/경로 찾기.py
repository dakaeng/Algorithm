from collections import deque

N = int(input())
graph = [[] for _ in range(N+1)]

for i in range(1, N+1) :
  n = list(map(int, input().split()))
  for idx, j in enumerate(n) :
    if j == 1 :
      graph[i].append(idx+1)

def bfs(v) :
  queue = deque([v])
  while queue :
    v = queue.popleft()
    for i in graph[v] :
      if answer[i] == 0 :
        queue.append(i)
        answer[i] = 1
        
for i in range(1, N+1) :
  answer = [0 for _ in range(N+1)]
  bfs(i)
  print(*answer[1:])