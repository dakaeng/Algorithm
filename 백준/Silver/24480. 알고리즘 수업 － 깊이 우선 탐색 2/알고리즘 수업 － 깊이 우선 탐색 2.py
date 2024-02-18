import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M) :
  u, v = map(int, input().split())
  graph[u].append(v)
  graph[v].append(u)

def dfs(v) :
  global count
  visited[v] = True
  answer[v] = count
  graph[v].sort(reverse = True)
  for i in graph[v] :
    if not visited[i] :
      count += 1
      dfs(i)

visited = [False] * (N+1)
answer = [0] * (N+1)
count = 1
dfs(R)
for i in answer[1:] :
  print(i)