board = []
nums = []
for _ in range(5) :
  board.append(list(map(int, input().split())))
for _ in range(5) :
  nums.extend(list(map(int, input().split())))

check = [[0 for _ in range(5)] for _ in range(5)]  # 빙고 여부 체크용

# 가로 빙고 개수 체크
def row_bingo(check) :
  count = 0
  for row in check :
    if sum(row) == 5 :
      count += 1
  return count

# 세로 빙고 개수 체크
def col_bingo(check) :
  count = 0
  check_t = list(map(list, zip(*check)))
  for col in check_t :
    if sum(col) == 5 :
      count += 1
  return count

# 오른쪽 대각선 빙고 체크
def r_cross_bingo(check) :
  temp = 0
  for i in range(5) :
    temp += check[i][i]
  if temp == 5 :
    return 1
  return 0

# 왼쪽 대각선 빙고 체크
def l_cross_bingo(check) :
  temp = 0
  for i in range(5) :
    temp += check[i][5-i-1]
  if temp == 5 :
    return 1
  return 0

# 빙고 : 가로, 세로, 대각선
for idx, n in enumerate(nums) :
  for i in range(5) :
    for j in range(5) :
      if board[i][j] == n :
        check[i][j] = 1
  # 빙고 여부 확인하기
  if idx >= 4 :  # 숫자를 5개 미만으로 불렀을 때는 절대로 빙고를 외칠 수 없음
    count = row_bingo(check) + col_bingo(check) + r_cross_bingo(check) + l_cross_bingo(check)
    if count >= 3 :
      print(idx + 1)
      break