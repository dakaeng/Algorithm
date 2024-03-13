import heapq

INF = int(1e9)

def dijkstra(node, graph) :
  q = []
  heapq.heappush(q, (0, node))
  distance = [INF] * (n+1)
  distance[node] = 0
  while q :
    dist, now = heapq.heappop(q)
    for i in graph[now] :
      cost = dist + i[1]
      if cost < distance[i[0]] :
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))
  return distance
  
T = int(input())
for _ in range(T) :
  # n : 교차로 개수, m : 도로 개수, t : 목적지 후보 개수
  n, m, t = map(int, input().split())
  # s : 예술가 출발지, g&h : 예술가들이 지난 교차로
  s, g, h = map(int, input().split())
  # 연결된 도로
  graph = [[] for _ in range(n+1)]
  for _ in range(m) :
    a, b, d = map(int, input().split())  # a와 b 사이에 길이 d의 양방향 도로
    graph[a].append((b, d))
    graph[b].append((a, d))

  # s에서 출발하는 경우, 각 노드까지의 최단거리
  s_s = dijkstra(s, graph)
  s_g = dijkstra(g, graph)
  s_h = dijkstra(h, graph)

  possible = []  # 가능한 목적지 후보 저장
  for _ in range(t) :
    x = int(input())
    count_1 = s_s[g] + s_g[h] + s_h[x]
    count_2 = s_s[h] + s_h[g] + s_g[x]
    if min(count_1, count_2) > s_s[x] :
      continue
    else :
      possible.append(x)
  possible.sort()
  print(*possible)