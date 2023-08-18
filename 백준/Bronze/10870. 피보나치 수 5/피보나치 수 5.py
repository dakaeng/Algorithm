def fibo(n) :
  if n == 0 :
    answer = 0
  elif n == 1 :
    answer = 1
  else :
    answer = fibo(n-1) + fibo(n-2)
  return answer

n = int(input())
print(fibo(n))