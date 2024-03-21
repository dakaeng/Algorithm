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
    
T = int(input())

for _ in range(T) :
  N, M = map(int, input().split())
  parent = [0] * (N+1)
  result = 0

  for i in range(1, N+1) :
    parent[i] = i
  
  for _ in range(M) :
    a, b = map(int, input().split())
    if find_parent(parent, a) != find_parent(parent, b) :
      union_parent(parent, a, b)
      result += 1
  print(result)