from collections import deque

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M) :
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

def dfs(v) :
  check_d[v] = True
  answer_d.append(v)
  graph[v].sort()
  for i in graph[v] :
    if not check_d[i] :
      dfs(i)

def bfs(v) :
  queue = deque([v])
  check_b[v] = True
  while queue :
    v = queue.popleft()
    answer_b.append(v)
    graph[v].sort()
    for i in graph[v] :
      if not check_b[i] :
        queue.append(i)
        check_b[i] = True

check_d = [False] * (N+1)
answer_d = []
check_b = [False] * (N+1)
answer_b = []
dfs(V)
bfs(V)
print(*answer_d)
print(*answer_b)