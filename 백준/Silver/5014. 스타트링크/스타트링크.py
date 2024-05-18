# [1697번 숨바꼭질] 문제와 유사하게 풀이. bfs 사용해서
from collections import deque

F, S, G, U, D = map(int, input().split())
count = [0] * (F+1)

def bfs() :
  queue = deque()
  queue.append(S)
  count[S] = 1

  while queue :
    x = queue.popleft()
    if x == G :
      return (count[x] - 1)
    for nx in (x+U, x-D) :
      if 1 <= nx <= F and count[nx] == 0 :
        count[nx] = count[x] + 1
        queue.append(nx)
  if count[G] == 0 :
    return "use the stairs"

print(bfs())