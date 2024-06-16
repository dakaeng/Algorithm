S = int(input())

# 작은 수부터
n = 0
while (S >= 0) :
  S -= (n+1)
  n += 1
print(n-1)