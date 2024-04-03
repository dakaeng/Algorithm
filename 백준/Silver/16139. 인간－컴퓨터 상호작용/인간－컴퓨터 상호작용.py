import sys
input = sys.stdin.readline

S = list(input())
q = int(input())
for _ in range(q) :
  a, l, r = input().split()
  l, r = int(l), int(r)
  count = [0] * (len(S))
  for i, s in enumerate(S) :
    if s == a :
      count[i] = 1
  print(sum(count[l:(r+1)]))