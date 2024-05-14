T = int(input())
for _ in range(T) :
  n = int(input())
  sticker = []
  for _ in range(2) :
    sticker.append(list(map(int, input().split())))

  d = [[0, 0] for _ in range(n)]
  d[0] = [sticker[0][0], sticker[1][0]]
  if n > 1 :
    d[1] = [d[0][1] + sticker[0][1], d[0][0] + sticker[1][1]]
  if n > 2 :
    for i in range(2, n) :
      d[i][0] = sticker[0][i] + max(d[i-2][1], d[i-1][1])
      d[i][1] = sticker[1][i] + max(d[i-2][0], d[i-1][0])
  print(max(d[n-1]))