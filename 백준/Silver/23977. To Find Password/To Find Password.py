K, N = map(int, input().split())
A = list(map(int, input().split()))

# A의 원소들의 최소공배수 - K
def LCM(a, b) :
  mul = a * b

  if a < b :
    a, b = b, a
  
  rem = 1
  while (rem != 0) :
    rem = a % b
    a, b = b, rem
 
  return int(mul / a)

A.sort()
temp = A[0]
for i in range(1, N) :
  temp = LCM(temp, A[i])
print(temp - K)