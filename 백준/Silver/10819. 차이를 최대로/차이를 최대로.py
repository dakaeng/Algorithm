N = int(input())
A = list(map(int, input().split()))

# N개중에 중복 없이 N개를 뽑는 경우
def dfs() :
  global answer

  if len(temp) == N :
    # 식의 값 계산
    plus = 0
    for i in range(N-1) :
      plus += max(temp[i] - temp[i+1], temp[i+1] - temp[i])
    answer = max(answer, plus)

  for i in range(N) :
    if visited[i] == False :
      temp.append(A[i])
      visited[i] = True
      dfs()
      temp.pop()
      visited[i] = False

temp = []
visited = [False] * N
answer = 0
dfs()
print(answer)