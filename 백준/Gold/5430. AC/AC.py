from collections import deque

T = int(input())

for _ in range(T) :
  p = input()
  n = int(input())
  X_list = input()

  queue = deque()
  for num in X_list[1:-1].split(',') :
    queue.append(num)
  error = 0

  if n == 0 :
    queue = []

  count = 0
  for func in p :
    if func == 'R' :
      count += 1
    if func == 'D' :
      if not queue :
        print('error')
        error = 1
        break
      else :
        if count % 2 == 0 :  # ex. RR -> 두 번 뒤집는 것 == 뒤집지 않는 것
          queue.popleft()
        else :  # 한 번 뒤집고 첫 번째 원소 제거하기 == 뒤집지 않고 마지막 원소 제거하기
          queue.pop()

  if error == 0 :
    if count % 2 == 1 :
      queue.reverse()
    print('[' + ','.join(queue) + ']')