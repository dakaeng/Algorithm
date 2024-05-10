N, S = map(int, input().split())
nums = list(map(int, input().split()))

# N과 M 문제들과 유사하게 풀이
# nums의 index들로 조합의 경우들을 모두 구하고, 그 합이 S가 되는지 체크하는 방식으로 작성
def dfs(start, M) :
  global count
  if len(s) == M :
    sum = 0
    for idx in s :
      sum += nums[idx-1]
    if sum == S :
      count += 1
    return

  for i in range(start, N+1) :
    if visited[i] == True :
      continue
    visited[i] = True
    s.append(i)
    dfs(i+1, M)
    s.pop()
    visited[i] = False
    
s = []
visited = [False] * (N+1)
count = 0
for i in range(1, N+1) :
  dfs(1, i)
print(count)