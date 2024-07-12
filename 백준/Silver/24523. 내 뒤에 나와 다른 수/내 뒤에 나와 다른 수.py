N = int(input())
A = list(map(int, input().split()))

answer = [-1] * N
i = 0

for j in range(1, N) :
  if A[i] != A[j] :
    answer[i:j] = [j+1] * (j-i)
    i = j
print(*answer)