N, K = map(int, input().split())
pos = list(input())

count = 0
for i in range(N) :
  if pos[i] != 'P' :
    continue
  for j in range(i-K, i+K+1) :
    if 0 <= j < N :
      if pos[j] == 'H' :
        pos[j] = '0'
        count += 1
        break
print(count)