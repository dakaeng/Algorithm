import sys
sys.setrecursionlimit(10**6)

M, N, K = map(int, input().split())
maps = [[0 for _ in range(N)] for _ in range(M)]

# 직사각형이 그려진 부분을 -1로 표시한다.
for _ in range(K) :
  x1, y1, x2, y2 = map(int, input().split())
  for i in range(x1, x2) :
    for j in range(y1, y2) :
      maps[j][i] = -1

# 한 영역의 넓이를 구하기 위한 dfs 함수
def dfs(x, y) :
  global count  # 한 영역의 넓이

  if (0 <= x < M) and (0 <= y < N) and maps[x][y] == 0 :
    maps[x][y] = -1
    count += 1
    dfs(x-1, y)
    dfs(x+1, y)
    dfs(x, y-1)
    dfs(x, y+1)
    return True
  return False

nums = []
count = 0
for i in range(M) :
  for j in range(N) :
    if dfs(i, j) == True :
      nums.append(count)
      # 한 영역의 넓이를 구한 후, 다른 영역의 넓이를 구하기 전에 다시 0으로 초기화해준다.
      count = 0  
    
nums.sort()
print(len(nums))
print(*nums)