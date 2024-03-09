import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

T = int(input())
for _ in range(T) :
  M, N, K = map(int, input().split())
  graph = [[0 for _ in range(M)] for _ in range(N)]
  for _ in range(K) :
    X, Y = map(int, input().split())
    graph[Y][X] = 1

  def dfs(x, y) :
    if x < 0 or x >= M or y < 0 or y >= N :
      return False
    if graph[y][x] == 1 :
      graph[y][x] = 0
      dfs(x-1, y)
      dfs(x, y-1)
      dfs(x+1, y)
      dfs(x, y+1)
      return True
    return False

  answer = 0
  for i in range(M) :
    for j in range(N) :
      if dfs(i, j) == True :
        answer += 1
  print(answer)