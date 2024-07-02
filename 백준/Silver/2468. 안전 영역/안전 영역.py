import sys
sys.setrecursionlimit(10**6)

N = int(input())
maps = []
max_h = 0
for _ in range(N) :
  temp = list(map(int, input().split()))
  maps.append(temp)
  max_h = max(max_h, max(temp))


def dfs(x, y) :

  if (0 <= x < N) and (0 <= y < N) and n_maps[x][y] == 1 :
    n_maps[x][y] = 0
    dfs(x-1, y)
    dfs(x, y-1)
    dfs(x+1, y)
    dfs(x, y+1)
    return True

  return False


h = 0
answer = 0

while (h < max_h) :
  n_maps = [[0 for _ in range(N)] for _ in range(N)]
  for i in range(N) :
    for j in range(N) :
      if maps[i][j] > h :
        n_maps[i][j] = 1
      else :
        n_maps[i][j] = 0

  count = 0
  for i in range(N) :
    for j in range(N) :
      if dfs(i, j) == True :
        count += 1
  
  answer = max(answer, count)
  h += 1

print(answer)