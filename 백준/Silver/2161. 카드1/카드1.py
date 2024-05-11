from collections import deque

N = int(input())
queue = deque()
for i in range(1, N+1) :
  queue.append(i)

while (len(queue) > 1) :
  print(queue.popleft(), end = ' ')  # 제일 위에 있는 카드 버리기
  a = queue.popleft()  # 제일 위에 있는 카드 뽑아서
  queue.append(a)  # 밑에 깔기
print(queue[0])