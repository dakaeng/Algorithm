# 플로이드 워셜 사용 시 시간초과
import heapq

def solution(n, edge):
    answer = 0
    INF = 1e9
    graph = [[] for _ in range(n+1)]  # graph[i] : i번 노드와 연결된 노드 저장
    distance = [INF for _ in range(n+1)]  # dist[i] : 1번 노드와 i번 노드 사이의 최단거리
    
    for i in edge :
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])
    
    def dijkstra(v) :
        q = []
        heapq.heappush(q, (0, v))
        distance[v] = 0
        
        while q :
            dist, now = heapq.heappop(q)
            if distance[now] < dist :  # 방문했던 경우 : 이미 최소이므로 넘김
                continue
            for i in graph[now] :
                if (dist + 1) < distance[i] :
                    distance[i] = min(distance[i], dist + 1)
                    heapq.heappush(q, (dist + 1, i))
    
    dijkstra(1)
    max_dist = max(distance[1:])
    for i in distance[1:] :
        if i == max_dist :
            answer += 1
    
    return answer