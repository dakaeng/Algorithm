T = int(input())
for _ in range(T) :
  N = int(input())
  P = [1] * 101
  for i in range(4, N+1) :
    P[i] = P[i-3] + P[i-2]
  print(P[N])