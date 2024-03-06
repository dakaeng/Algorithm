import sys
input = sys.stdin.readline
import heapq

N, E = map(int, input().split())
INF = 1e9
graph = [[] for _ in range(N+1)]

for _ in range(E) :
  a, b, c = map(int, input().split())
  graph[a].append((b, c))
  graph[b].append((a, c))
v1, v2 = map(int, input().split())

def dijkstra(node) :
  distance = [INF] * (N+1)
  q = []
  heapq.heappush(q, (0, node))
  distance[node] = 0
  while q :
    dist, now = heapq.heappop(q)
    if distance[now] < dist :
      continue
    for i in graph[now] :
      cost = dist + i[1]
      if cost < distance[i[0]] :
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))
  return distance

len1 = dijkstra(1)[v1] + dijkstra(v1)[v2] + dijkstra(v2)[N]
len2 = dijkstra(1)[v2] + dijkstra(v2)[v1] + dijkstra(v1)[N]
answer = min(len1, len2)
if answer < INF :
  print(answer)
else :
  print(-1)