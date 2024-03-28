from collections import deque

N, M = map(int, input().split())  # N : 학생 수, M : 입력 수
indegree = [0] * (N+1)
graph = [[] for _ in range(N+1)]

for _ in range(M) :
  A, B = map(int, input().split())
  graph[A].append(B)
  indegree[B] += 1

def topology_sort() :
  result = []
  q = deque()
  q.append
  
  for i in range(1, N+1) :
    if indegree[i] == 0 :
      q.append(i)

  while q :
    now = q.popleft()
    result.append(now)
    for i in graph[now] :
      indegree[i] -= 1
      if indegree[i] == 0 :
        q.append(i)
  
  for i in result :
    print(i, end = ' ')

topology_sort()