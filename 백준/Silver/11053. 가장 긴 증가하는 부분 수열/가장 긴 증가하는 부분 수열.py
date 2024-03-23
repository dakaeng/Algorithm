N = int(input())
A = [0] + list(map(int, input().split()))

d = [1] * (N+1)
for i in range(2, N+1) :
  for j in range(i-1, 0, -1) :
    if A[j] < A[i] :
      d[i] = max(d[i], d[j] + 1)
print(max(d))