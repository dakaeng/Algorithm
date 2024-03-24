import sys
input = sys.stdin.readline

def find_parent(parent, x) :
  if parent[x] != x :
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

def union_parent(parent, a, b) :
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b :
    parent[b] = a
  else :
    parent[a] = b
    
while True :
  m, n = map(int, input().split())  # m : 집의 수, n : 길의 수
  if m == 0 and n == 0 :
    break
  
  parent = [0] * (m+1)
  for i in range(1, m+1) :
    parent[i] = i
  
  edges = []
  sum_ = 0
  result = 0

  for _ in range(n) :
    x, y, z = map(int, input().split())
    edges.append((z, x, y))
  edges.sort()

  for edge in edges :
    cost, a, b = edge
    sum_ += cost
    if find_parent(parent, a) != find_parent(parent, b) :
      union_parent(parent, a, b)
      result += cost
  print(sum_ - result)