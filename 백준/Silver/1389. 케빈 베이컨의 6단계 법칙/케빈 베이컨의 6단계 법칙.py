import heapq
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M) :
  A, B = map(int, input().split())
  graph[A].append(B)
  graph[B].append(A)

# 다익스트라 알고리즘으로 모든 유저에 대해 케빈 베이컨 수 구한 후, 그 수가 가장 작은 사람 구하기
INF = 1e9

def dijkstra(start) :
  q = []
  heapq.heappush(q, (0, start))
  nums[start] = 0

  while q :
    dist, now = heapq.heappop(q)
    if nums[now] < dist :
      continue
    for i in graph[now] :
      cost = dist + 1
      if cost < nums[i] :
        nums[i] = cost
        heapq.heappush(q, (cost, i))
        
answer = [0] * (N+1)
for i in range(1, N+1) :
  nums = [INF] * (N+1)
  dijkstra(i)
  answer[i] = sum(nums[1:])
print(answer.index(min(answer[1:])))