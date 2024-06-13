t = int(input())

for _ in range(t) :
  n = int(input())
  A = list(map(int, input().split()))

  dic = {}
  for a in A :
    if a in dic :
      dic[a] += 1
    else :
      dic[a] = 1
  
  if 2 in dic :
    n = dic[2]

    if n % 2 == 1 :
      print(-1)
    else :
      n = n//2
      count = 0
      for idx, a in enumerate(A) :
        if a == 2 :
          count += 1
        if count == n :
          print(idx+1)
          break
  else :
    print(1)