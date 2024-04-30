N, M = map(int, input().split())

def dfs(start) :
  if len(s) == M :
    print(' '.join(map(str, s)))
    return

  for i in range(start, N+1) :
    if visited[i] == True :
      continue
    visited[i] = True
    s.append(i)
    dfs(i+1)
    s.pop()
    visited[i] = False
    
s = []
visited = [False] * (N+1)
dfs(1)