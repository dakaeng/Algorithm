N = int(input())  # 이동하고자 하는 채널
M = int(input())  # 고장난 버튼의 개수
if M != 0 :
  broken = list(map(int, input().split())) 
else :
  broken = []

min_count = abs(100 - N)  # +, - 버튼만 사용하여 이동하는 경우

for n in range(1000000) :  # n : 가능한 채널 번호 (고장나지 않은 버튼으로만 이루어진 숫자여야 함)
  for i in str(n) :
    if int(i) in broken :  # 고장난 버튼을 눌러야 이동할 수 있는 채널이라면, 가능한 번호가 아니므로 제외
      break
  else :  # n을 이루는 숫자 중 고장난 버튼이 한 개도 없다면 가능한 채널 번호이므로 이 경우에 대해서만 최소 입력 횟수 계산
    # len(str(n)) : 먼저 숫자 버튼을 눌러서 채널 n으로 이동하는데 필요한 입력 횟수
    # abs(n-N) : 현재 채널 n에서 우리가 가고자 하는 채널 N까지 +, - 버튼을 이용해서 이동하는데 필요한 입력 횟수
    min_count = min(min_count, len(str(n)) + abs(n-N))
print(min_count)