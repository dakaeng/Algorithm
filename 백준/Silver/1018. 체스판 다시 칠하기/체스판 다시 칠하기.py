N, M = map(int, input().split())
board = []
count = []

for _ in range(N) :
    board.append(input())

for i in range(N-7) :
  for j in range(M-7) :
    count1 = 0
    count2 = 0
    for x in range(i, i+8) :
      for y in range(j, j+8) :
        # 첫번째 시작이 W인 경우
        if (x+y) % 2 == 0 :
          if board[x][y] == 'B' :
            count1 += 1
        else :
          if board[x][y] == 'W' :
            count1 += 1

        # 첫번째 시작이 B인 경우
        if (x+y) % 2 == 0 :
          if board[x][y] == 'W' :
            count2 += 1
        else :
          if board[x][y] == 'B' :
            count2 += 1
    count.append(count1)
    count.append(count2)
print(min(count))