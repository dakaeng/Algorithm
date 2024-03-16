import heapq
import sys
input = sys.stdin.readline

N = int(input())
q = []
for _ in range(N) :
  x = int(input())

  if x > 0 :
    heapq.heappush(q, [x, x])
  elif x < 0 :
    heapq.heappush(q, [-x, x])
  else :
    if not q :
      print(0)
    else :
      pop = heapq.heappop(q)
      print(pop[1])