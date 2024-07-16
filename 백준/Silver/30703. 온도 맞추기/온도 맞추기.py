N = int(input())
A = list(map(int, input().split()))  # 초기 온도
B = list(map(int, input().split()))  # 목표 온도
X = list(map(int, input().split()))  # 온도 변화 값

# 모든 i에 대해서 온도가 한 번에 조절되는게 핵심
answer = 0

for i in range(N) :
  diff = A[i] - B[i]
  if diff < 0 :
    diff = -diff

  count = diff // X[i]
  if i == 0 :
    even = count % 2
  
  if (diff % X[i] == 0) and even == (count % 2) :
    answer = max(answer, diff // X[i])
  else :
    answer = -1
    break
print(answer)