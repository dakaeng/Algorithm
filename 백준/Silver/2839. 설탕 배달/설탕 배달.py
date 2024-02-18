N = int(input())

answer = 0
while (N > 0) :
  if N % 5 == 0 :
    answer += N // 5
    N = 0
  else :
    answer += 1
    N -= 3  # 5의 배수가 될 때까지 3씩 빼준다고 생각하면 됨
    
if N == 0 :
  print(answer)
else :
  print(-1)