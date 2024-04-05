N = int(input())

d = [[0] * 10 for _ in range(N+1)]  # d[n][i] : n번째 자리 수(앞에서부터 셀 때)가 i인 계단수의 개수 
d[1] = [0] + [1] * 9

for n in range(2, N+1) :
  for i in range(10) :
    if i == 0 :
      d[n][i] = d[n-1][1]
    elif i == 9 :
      d[n][i] = d[n-1][8]
    else :
      d[n][i] = d[n-1][i-1] + d[n-1][i+1]
print(sum(d[N]) % 1000000000)