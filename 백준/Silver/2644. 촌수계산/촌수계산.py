import sys
sys.setrecursionlimit(10**6)

n = int(input())
p1, p2 = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m) :
  x, y = map(int, input().split())
  graph[x].append(y)
  graph[y].append(x)

visited = [False] * (n+1)
answer = []

def dfs(v, count) :
  count += 1
  visited[v] = True

  if v == p2 :
    answer.append(count)
    return

  for i in graph[v] :
    if not visited[i] :  # 이전에 방문하지 않은 경우
      dfs(i, count)

dfs(p1, 0)
if not answer :
  print(-1)
else :
  print(answer[0] - 1)