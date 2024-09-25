T = int(input())
for _ in range(T) :
  N = int(input())
  L = list(map(int, input().split()))
  L.sort()
  L_sort = []
  # 홀수번째 숫자
  for i in range(0, N, 2) :
    L_sort.append(L[i])
  # 짝수번째 숫자 저장
  if N % 2 == 0 :
    for i in range(N-1, -1, -2) :
      L_sort.append(L[i])
  else :
    for i in range(N-2, -1, -2) :
      L_sort.append(L[i])
  # 통나무 간의 길이차이 계산
  answer = 0
  for i in range(1, N) :
    lv = L_sort[i] - L_sort[i-1]
    if lv < 0 :
      lv = lv * (-1)
    answer = max(answer, lv)
  answer = max(answer, L_sort[-1] - L_sort[0])
  print(answer)