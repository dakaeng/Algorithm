N, M = map(int, input().split())
trees = list(map(int, input().split()))

start, end = 1, max(trees)
result = 0
while (start <= end) :
  mid = (start + end) // 2
  count = 0
  for i in trees :
    if i > mid :
      count += (i - mid)
  if count < M :
    end = mid - 1
  else :
    result = mid
    start = mid + 1
print(result)