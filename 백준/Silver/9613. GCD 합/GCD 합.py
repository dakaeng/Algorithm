# 두 수의 최대공약수 구하는 함수
def GCD(n1, n2) :
  rem = 1
  while (rem != 0) :
    rem = n1 % n2  # n2로 나누어 떨어지면, n2가 곧 최대공약수
    n1 = n2
    n2 = rem
  return n1  # n1 = n2 처리했기 때문

t = int(input())

for _ in range(t) :
  n, *nums = map(int, input().split())
  answer = 0
  for i in range(n-1) :
    for j in range(i+1, n) :
      answer += GCD(nums[i], nums[j])
  print(answer)