n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()

answer = 0
while True :
  temp = a.pop()  
  # 첫 번째 멀티탭에 포함된 콘센트 개수만큼 두 번째 멀티탭 꽂기
  for _ in range(temp) :
    if b :
      answer += b.pop()
    else :
      break
  
  if a and b :  # 두 번째 멀티탭에 첫 번째 멀티탭을 또 꽂을 수 있는 경우
    answer -= 1
  else :
    break
print(answer)