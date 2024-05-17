import sys
sys.setrecursionlimit(10**6)

def dfs(x, y) :
  if x < 0 or x >= h or y < 0 or y >= w :
    return False
  if maps[x][y] == 1 :  # 땅
    maps[x][y] = 0
    dfs(x-1, y)  # 상
    dfs(x+1, y)  # 하
    dfs(x, y-1)  # 좌
    dfs(x, y+1)  # 우
    # 대각선들
    dfs(x-1, y-1)
    dfs(x-1, y+1)
    dfs(x+1, y-1)
    dfs(x+1, y+1)
    return True
  return False

while True :
  w, h = map(int, input().split())
  if w == h == 0 :
    break

  maps = []
  for _ in range(h) :
    maps.append(list(map(int, input().split())))

  answer = 0
  for i in range(h) :
    for j in range(w) :
      if dfs(i, j) == True :
        answer += 1
  print(answer)