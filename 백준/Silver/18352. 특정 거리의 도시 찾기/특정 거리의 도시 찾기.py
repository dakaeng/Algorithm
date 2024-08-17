import heapq
import sys
input = sys.stdin.readline

N, M, K, X = map(int, input().split())
road = [[] for _ in range(N+1)]  # 두 도시를 잇는 도로 정보 저장
for _ in range(M) :
  A, B = map(int, input().split())
  road[A].append(B)
    
INF = 1e9
distance = [INF] * (N+1)

# 다익스트라 알고리즘
def dijkstra(start) :
	q = []
	heapq.heappush(q, (0, start))
	distance[start] = 0
  
	while q :
		# 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
		dist, now = heapq.heappop(q)  # 힙에서 가장 작은 항목 pop
		# 현재 노드가 이미 처리된 적 있는 노드라면 무시
		if distance[now] < dist :
			continue
		# 현재 노드와 연결된 다른 인접한 노드들을 확인
		for i in road[now] :
			cost = dist + 1
			# 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
			if cost < distance[i] :
				distance[i] = cost
				heapq.heappush(q, (cost, i))

dijkstra(X)
answer = False
for i in range(1, N+1) :
  if distance[i] == K :
    answer = True
    print(i)

if answer == False :
  print(-1)