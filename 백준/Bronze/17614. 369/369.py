N = int(input())

count = 0
for n in range(1, N+1) :
  n = str(n)
  for i in n :
    if (i != '0' ) and (int(i) % 3 == 0) :
      count += 1
print(count)