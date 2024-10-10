N = int(input())
answer = 0

while (N > 0) :
  if N % 5 == 0 :
    answer += (N//5)
    N -= N
  else :  # 5의 배수가 될 때까지 3을 빼주기!
    answer += 1
    N -= 3

if N == 0 :
  print(answer)
else :
  print(-1)