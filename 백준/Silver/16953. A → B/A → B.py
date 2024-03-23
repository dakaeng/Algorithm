from collections import deque

A, B = map(int, input().split())
queue = deque()
queue.append([A, 1])

while queue :
  v, count = queue.popleft()
  if v > B :
    continue
  if v == B :
    print(count)
    break
  queue.append([v*2, count + 1])
  queue.append([v*10 + 1, count + 1])
else :
  print(-1)