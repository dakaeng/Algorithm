A, B = map(int, input().split())

def GCD(a, b) :
  if a < b :
    a, b = b, a
  
  rem = 1
  while (rem != 0) :
    rem = a % b
    a, b = b, rem

  return a

print(int((A * B) / GCD(A, B)))