from collections import deque

N, M = map(int, input().split())
campus = []
for i in range(N) :
  input_i = list(input())
  if 'I' in input_i :
    x = i
    y = input_i.index('I')
  campus.append(input_i)

answer = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()
queue.append([x, y])
while queue :
  x, y = queue.popleft()
  for i in range(4) :
    nx = x + dx[i]
    ny = y + dy[i]
    if nx < 0 or nx >= N or ny < 0 or ny >= M :
      continue
    if campus[nx][ny] != 'X' :
      queue.append([nx, ny])
      if campus[nx][ny] == 'P' :
        answer += 1
      campus[nx][ny] = 'X'
    
if answer == 0 :
  print('TT')
else :
  print(answer)