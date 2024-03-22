import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
graph = [[] for _ in range(N+1)]
parent = [0] * (N+1)

for _ in range(N-1) :
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

visited = [False] * (N+1)

def dfs(v) :
  visited[v] = True
  for i in graph[v] :
    if not visited[i] :
      parent[i] = v
      dfs(i)
      
dfs(1)
for i in parent[2:] :
  print(i)