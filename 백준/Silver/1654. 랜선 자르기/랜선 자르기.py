K, N = map(int, input().split())
lists = []
for _ in range(K) :
  lists.append(int(input()))

start, end = 1, max(lists)
result = 0
while (start <= end) :
  mid = (start + end) // 2
  count = 0
  for i in lists :
    count += (i // mid)
  if count < N :
    end = mid - 1
  else :
    result = mid
    start = mid + 1
print(result)