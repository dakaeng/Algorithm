N = list(input())

# 30의 배수 : 3의 배수이면서 일의 자리가 0인 수
# 3의 배수 : 각 자리 수의 합이 3의 배수인 수
sum = 0
for n in N :
  sum += int(n)

if sum % 3 != 0 or '0' not in N :  # 30의 배수가 아니다.
  print(-1)
else : 
  # 30의 배수가 될 수 있는 경우 중 가장 큰 수를 만들기 위해서는 등장하는 숫자들을 모두 내림차순으로 정렬하면 된다.
  N.sort(reverse = True)
  answer = ''
  for n in N :
    answer += n
  print(int(answer))