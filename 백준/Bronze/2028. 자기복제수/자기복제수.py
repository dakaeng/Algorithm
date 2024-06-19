T = int(input())

for _ in range(T) :
  N = int(input())
  square = N**2
  len_N = len(str(N))
  if str(square)[-len_N:] == str(N) :
    print('YES')
  else :
    print('NO')