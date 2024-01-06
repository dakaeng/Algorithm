N = int(input())
time = []
for _ in range(N) :
  A, B = map(int, input().split())
  if A <= B :
    time.append(B)

if time :
  print(min(time))
else :
  print(-1)