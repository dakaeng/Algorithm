from collections import deque

N, K = map(int, input().split())
time = [0] * (max(N, K) * 2 + 1)
queue = deque()
queue.append(N)
while queue :
  x = queue.popleft()
  if x == K :
    print(time[x])
    break
  for nx in (x-1, x+1, 2*x) :
    if 0 <= nx <= max(N, K) * 2 and time[nx] == 0 :
      time[nx] = time[x] + 1
      queue.append(nx)