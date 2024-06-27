N = int(input())
K = int(input())

for _ in range(K) :
  a, b = map(int, input().split())

  if a > (N//2 + 1) :
    a = N + 1 - a

  if b > (N//2 + 1) :
    b = N + 1 - b
  
  if a >= b :
    answer = b % 3
  else :
    answer = a % 3
  
  if answer == 0 :
    answer = 3
  print(answer)