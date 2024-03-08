import heapq
import sys
input = sys.stdin.readline

q = []
N = int(input())
for _ in range(N) :
  x = (-1) * int(input())
  if x == 0 :
    if q :
      minimum = heapq.heappop(q)
      print(-minimum)
    else :
      print(0)
  else :
    heapq.heappush(q, x)