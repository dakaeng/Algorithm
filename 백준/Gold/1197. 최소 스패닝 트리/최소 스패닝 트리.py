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

V, E = map(int, input().split())
parent = [0] * (V+1)

for i in range(1, V+1) :
  parent[i] = i

edges = []
result = 0

for _ in range(E) :
  A, B, C = map(int, input().split())
  edges.append((C, A, B))
edges.sort()

for edge in edges :
  C, A, B = edge
  if find_parent(parent, A) != find_parent(parent, B) :
    union_parent(parent, A, B)
    result += C
print(result)