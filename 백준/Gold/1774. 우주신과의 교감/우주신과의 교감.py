def distance(a, b) :
  x1 = gods[a][0]
  y1 = gods[a][1]
  x2 = gods[b][0]
  y2 = gods[b][1]

  return ((x1-x2)**(2) + (y1-y2)**(2))**(0.5)

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

N, M = map(int, input().split())
parent = [0] * (N+1)

for i in range(1, N+1) :
  parent[i] = i

gods = [[] for _ in range(N+1)]  # gods[i] : i번째 우주신의 좌표
edges = []  # (dist, a, b) 저장
result = 0

for i in range(1, N+1) :
  X, Y = map(int, input().split())
  gods[i] = [X, Y]

for _ in range(M) :
  a, b = map(int, input().split())  # 이미 연결되어있는 우주신 번호
  union_parent(parent, a, b)

for i in range(1, N+1) :
  for j in range(1, N+1) :
    if j > i :
      cost = distance(i, j)
      edges.append((cost, i, j))
edges.sort()

for edge in edges :
  dist, a, b = edge
  if find_parent(parent, a) != find_parent(parent, b) :
    union_parent(parent, a, b)
    result += dist

print(format(round(result, 2), '.2f'))