t = int(input())

for _ in range(t) :
  n = int(input())
  X = list(map(int, input().split()))
  X.sort()
  print(2 * (X[-1] - X[0]))