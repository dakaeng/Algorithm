import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M) :
  u, v = map(int, input().split())
  graph[u].append(v)
  graph[v].append(u)

def dfs(v) :
  global count  # 함수 밖에서 선언한 count를 함수 내에서도 사용
  answer[v] = count  # v번째 index에 순서 저장
  graph[v].sort(reverse = True)
  for i in graph[v] :
    if answer[i] == 0 :
      count += 1
      dfs(i)

answer = [0] * (N+1)
count = 1
dfs(R)
for i in answer[1:] :
  print(i)