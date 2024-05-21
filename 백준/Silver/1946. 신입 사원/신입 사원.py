import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T) :
  N = int(input())
  A = []  # 지원자들 [서류 성적, 면접 성적] 저장
  for _ in range(N) :
    A.append(list(map(int, input().split())))
  
  # 서류 성적 기준으로 정렬
  A.sort()

  # 서류 성적, 면접 성적 모두 나보다 높은 지원자가 있으면 선발 x
  top = A[0][1]
  count = 1
  for i in range(1, N) :
    if A[i][1] < top :
      count += 1
      top = A[i][1]
  print(count)