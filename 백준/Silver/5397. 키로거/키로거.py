from collections import deque

T = int(input())

for _ in range(T) :
  L = input()

  # 커서 위치 기준으로 왼쪽, 오른쪽 문자 나누기
  left = []
  right = deque()

  for w in L :
    if w == '<' :
      if left :
        right.appendleft(left.pop())
    elif w == '>' :
      if right :
        left.append(right.popleft())
    elif w == '-' :
      if left :
        left.pop()
    else :
      left.append(w)

  print(''.join(left) + ''.join(right))