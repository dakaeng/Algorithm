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
    
def distance(a, b) :  # 별 번호 입력
  x1 = stars[a][0]
  y1 = stars[a][1]
  x2 = stars[b][0]
  y2 = stars[b][1]

  return ((x1-x2)**(2) + (y1-y2)**(2))**(0.5)

n = int(input())
parent = [0] * (n+1)

for i in range(1, n+1) :
  parent[i] = i

stars = [[] for _ in range(n+1)]
edges = []  # (a, b, cost) 저장
result = 0

for i in range(1, n+1) :
  x, y = map(float, input().split())
  stars[i] = [x, y]

for i in range(1, n+1) :
  for j in range(1, n+1) :
    if j > i :
      cost = distance(i, j)
      edges.append((cost, i, j))
edges.sort()

for edge in edges :
  cost, a, b = edge
  if find_parent(parent, a) != find_parent(parent, b) :
    union_parent(parent, a, b)
    result += cost
print(round(result, 2))