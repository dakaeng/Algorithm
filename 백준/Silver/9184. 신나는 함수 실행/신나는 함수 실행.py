w = [[[1 for _ in range(51)] for _ in range(51)] for _ in range(51)]
for a in range(1, 51) :
  for b in range(1, 51) :
    for c in range(1, 51) :
      if a < b and b < c :
        w[a][b][c] = w[a][b][c-1] + w[a][b-1][c-1] - w[a][b-1][c]
      else :
        w[a][b][c] = w[a-1][b][c] + w[a-1][b-1][c] + w[a-1][b][c-1] - w[a-1][b-1][c-1]

while True :
  a, b, c = map(int, input().split())
  if a == -1 and b == -1 and c == -1 :
    break
  if a <= 0 or b <= 0 or c <= 0 :
    answer = w[0][0][0]
  elif a > 20 or b > 20 or c > 20 :
    answer = w[20][20][20]
  else :
    answer = w[a][b][c]
  print('w({}, {}, {}) = {}'.format(a, b, c, answer))