X, Y, W, S = map(int, input().split())

answer = 0
# 2 * W < S 이면 -> W * (X + Y)
if (2 * W) <= S :
  answer = W * (X + Y)
# 2 * W > S 이면 -> 대각선으로 최대한 이동 후, 나머지 직선 이동
else :
  temp1, temp2 = 1e9, 1e9
  # 대각선으로만 이동 가능한 경우 -> (X + Y)가 짝수인 경우
  if (X + Y) % 2 == 0 :
    temp1 = S * max(X, Y)
  # X, Y 중 하나는 홀수, 하나는 짝수인 경우
  else :
    temp1 = S * (max(X, Y) - 1) + W
  # 대각선, 직선이동 섞어야 하는 경우
  temp2 = S * min(X, Y) + W * (X + Y - 2 * min(X, Y))
  answer = min(temp1, temp2)

print(answer)