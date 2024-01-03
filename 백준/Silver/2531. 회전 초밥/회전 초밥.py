N, d, k, c = map(int, input().split())
n = []
for _ in range(N) :
  n.append(int(input()))

answer = [0] * N
for i in range(N) :
  if i < (N-k+1) :
    dish = n[i:(i+k)]
  else :
    dish = n[i:] + n[0:(k-N+i)]
  num = len(set(dish))
  answer[i] = max(answer[i], num)
  if c not in dish :
    answer[i] += 1
print(max(answer))