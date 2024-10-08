import sys
input = sys.stdin.readline

R, C = map(int, input().split())
board = []
for _ in range(R) :
  board.append(list(input()))

def dfs(x, y) :

  global answer, count

  if (0 <= x < R and 0 <= y < C) and (visited[ord(board[x][y]) - ord('A')] == False) :
    visited[ord(board[x][y]) - ord('A')] = True
    count += 1

    dfs(x-1, y)
    dfs(x+1, y)
    dfs(x, y-1)
    dfs(x, y+1)

    # 모든 경우를 탐색하기 위해 필요
    answer = max(answer, count)
    visited[ord(board[x][y]) - ord('A')] = False
    count -= 1
    
visited = [False for _ in range(26)]
count = 0
answer = 1
dfs(0, 0)
print(answer)