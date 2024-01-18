N, M = map(int, input().split())
lesson = list(map(int, input().split()))

# 블루레이 크기로 이분 탐색
start, end = max(lesson), sum(lesson)
while (start <= end) :
  mid = (start + end) // 2  # 블루레이 크기 후보
  count = 1  # 블루레이 크기가 mid일 때 블루레이 개수
  total = 0  # 각 블루레이 크기
  for i in lesson :
    if (total + i) > mid :
      count += 1
      total = 0
    total += i
      
  if count <= M :
    end = mid - 1
  else :
    start = mid + 1
print(start)