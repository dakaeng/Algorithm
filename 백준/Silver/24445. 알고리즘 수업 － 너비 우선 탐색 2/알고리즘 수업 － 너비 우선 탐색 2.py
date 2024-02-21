from collections import deque
import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M) :
  u, v = map(int, input().split())
  graph[u].append(v)
  graph[v].append(u)

def bfs(start) :
  global count
  queue = deque([start])
  answer[start] = count
  while queue :
    v = queue.popleft()
    graph[v].sort(reverse = True)
    for i in graph[v] :
      if answer[i] == 0 :
        queue.append(i)
        count += 1
        answer[i] = count

answer = [0] * (N+1)
count = 1
bfs(R)
for i in answer[1:] :
  print(i)