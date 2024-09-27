N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

def dfs() :
  check = 0
  if len(s) == M :
    print(*s)
    return
  
  for i in range(N) :
    if check != nums[i] and visited[i] == False :
      s.append(nums[i])
      visited[i] = True
      check = nums[i]
      dfs()
      s.pop()
      visited[i] = False
        
s = []
visited = [False] * N
dfs()