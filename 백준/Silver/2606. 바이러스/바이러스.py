from collections import deque

N = int(input())
n_pair = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(n_pair) :
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

answer = [0] * (N+1)
queue = deque([1])
answer[1] = 1
while queue :
  v = queue.popleft()
  for i in graph[v] :
    if answer[i] == 0 :
      queue.append(i)
      answer[i] = 1
print(sum(answer) - 1)