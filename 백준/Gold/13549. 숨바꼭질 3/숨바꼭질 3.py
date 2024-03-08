import heapq
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
INF = 1e9
graph = [[] for _ in range(100002)]
time = [INF] * (100002)
graph[0].append((1, 1))
graph[1] = [(0, 1), (2, 0)]
up = max(N, K)
for i in range(2, up+1) :
  if i*2 <= 100000 :
    graph[i].append((i*2, 0))
  if (i+1) <= 100000 :
    graph[i].append((i+1, 1))
    graph[i+1].append((i, 1))
  graph[i].append((i-1, 1))
for i in range(100002) :
  graph[i] = list(set(graph[i]))
  graph[i].sort()

def dijkstra(start) :
  q = []
  heapq.heappush(q, (0, start))
  time[start] = 0
  while q :
    dist, now = heapq.heappop(q)
    if time[now] < dist :
      continue
    for i in graph[now] :
      cost = dist + i[1]
      if cost < time[i[0]] :
        time[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))

dijkstra(N)
print(time[K])