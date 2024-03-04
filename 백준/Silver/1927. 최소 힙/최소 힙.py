import heapq
import sys
input = sys.stdin.readline

N = int(input())
q = []
for _ in range(N) :
  x = int(input())
  if x == 0 :
    if len(q) == 0 :
      print(0)
    else :
      minimum = heapq.heappop(q)
      print(minimum)
  else :
    heapq.heappush(q, x)