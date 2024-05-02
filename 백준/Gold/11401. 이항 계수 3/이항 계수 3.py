N, K = map(int, input().split())
p = 1000000007

# 팩토리얼 값 계산
def factorial(n) :
  result = 1
  for i in range(2, n+1) :
    result = (result * i) % p
  return result

# 거듭제곱 계산
def power(n, k) :  # n^k
  if k == 0 :
    return 1
  elif k == 1 :
    return n

  tmp = power(n, k//2)
  if k % 2 :  # k가 홀수이면
    return tmp * tmp * n % p  # ex. 2^5 = 2^2 * 2^2 * 2
  else :  # k가 짝수이면
    return tmp * tmp % p

top = factorial(N)  # n!
bot = factorial(N-K) * factorial(K) % p  # (n-l)!k!

# 페르마의 소정리 활용
print(top * power(bot, p-2) % p)