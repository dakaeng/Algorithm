N = int(input())
Ns = list(map(int, input().split()))
Ns.sort()

# 모든 용액의 특성값이 음수이거나, 양수인 경우 -> 절댓값이 가장 작은 값 2개를 더해야 함
if Ns[-1] < 0 :  # 특성값이 모두 음수 (모두 알칼리성 용액)
  print(Ns[-2], Ns[-1])
elif Ns[0] > 0 :  # 특성값이 모두 양수 (모두 산성 용액)
  print(Ns[0], Ns[1])

# 특성값에 음수와 양수가 섞여있는 경우
else :
  sum = 1e9
  left, right = 0, N-1
  while (left < right) :
    temp = Ns[left] + Ns[right]
    if abs(sum) > abs(temp) :  # 현재 두 용액의 합이 기존의 합보다 0에 더 가까운 경우 -> 정답 후보 갱신
      sum = temp
      answer = [Ns[left], Ns[right]]
    if temp < 0 :  # 합이 0보다 작다 -> 합이 더 커져야 한다 -> 더 큰 수를 더해야 한다 -> 왼쪽 인덱스 증가
      left += 1
    elif temp > 0 :  # 합이 0보다 크다 -> 합이 더 작아져야 한다 -> 더 작은 수를 더해야 한다 -> 오른쪽 인덱스 감소
      right -= 1
    else :  # temp == 0  # 합이 0이므로 더 볼 필요 없음
      break
  print(*answer)