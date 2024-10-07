N, M = map(int, input().split())
castle = []
for _ in range(N) :
  castle.append(list(input()))

# 행과 열 각각에서 경비원이 한 명도 없는 개수 세기
count_row = 0
count_col = 0
for i in range(N) :
  if 'X' not in castle[i] :
    count_row += 1
for j in range(M) :
  temp = []
  for i in range(N) :
    temp.append(castle[i][j])
  if 'X' not in temp :
    count_col += 1
print(max(count_row, count_col))