import heapq

N = int(input())
card = []
for _ in range(N) :
  heapq.heappush(card, int(input()))

if N == 1 :
  print(0)
else :
  answer = 0
  while True :
    if len(card) == 1 :
      break
    n1 = heapq.heappop(card)
    n2 = heapq.heappop(card)
    answer += (n1 + n2)
    heapq.heappush(card, n1 + n2)
  print(answer)