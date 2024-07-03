T = int(input())

# A : 300초, B : 60초, C : 10초

if T % 10 != 0 :
  print(-1)
else :
  for i in [300, 60, 10] :
    print(T // i, end = ' ')
    T = T % i