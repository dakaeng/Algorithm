N, M = map(int, input().split())
A = list(map(int, input().split()))

count = 0
left = 0
right = 0

while (right < N) :
  sums = sum(A[left:(right+1)])
  if sums == M :
    count += 1
    right += 1
  elif sums > M :
    left += 1
  else :
    right += 1
print(count)