N = int(input())
d = [0] * (N+1)  # d[i] : i자리 이친수의 개수

d[1] = 1
if N > 1 :
  d[2] = 1
if N > 2 :
  for i in range(3, N+1) :
    d[i] = d[i-1] + d[i-2]
print(d[N])