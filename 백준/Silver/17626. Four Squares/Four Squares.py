import sys
input = sys.stdin.readline

n = int(input())
d = [0 for _ in range(n+1)]
d[1] = 1
for i in range(2, n+1) :
  minimum = 1e9
  if d[i] == 0 :
    for j in range(1, int(i**0.5)+1) :
      minimum = min(minimum, d[i-j**2])
    d[i] = minimum + 1
print(d[n])